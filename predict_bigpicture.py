import argparse
import os
import tempfile

from PIL import Image, ImageDraw
from ultralytics import YOLO


def get_colors(num_colors):
    import matplotlib.pyplot as plt

    colors = plt.cm.get_cmap("hsv", num_colors)
    return [tuple(int(channel * 255) for channel in colors(i)[:3]) for i in range(num_colors)]


def split_and_predict(model, image_path, output_path, tile_size):
    image = Image.open(image_path)
    img_width, img_height = image.size
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    draw = ImageDraw.Draw(image)
    colors = get_colors(len(model.names))

    with tempfile.TemporaryDirectory() as temp_dir:
        for i in range(0, img_width, tile_size):
            for j in range(0, img_height, tile_size):
                box = (i, j, min(i + tile_size, img_width), min(j + tile_size, img_height))
                img_cropped = image.crop(box)
                img_cropped_path = os.path.join(temp_dir, f"{base_name}_{i}_{j}.png")
                img_cropped.save(img_cropped_path)

                result = model(img_cropped_path)[0]

                for det in result.boxes:
                    x1, y1, x2, y2 = det.xyxy[0].clone()
                    conf = det.conf[0].item()
                    cls = det.cls[0].item()
                    color = colors[int(cls)]
                    x1 += i
                    y1 += j
                    x2 += i
                    y2 += j
                    draw.rectangle([x1, y1, x2, y2], outline=color, width=2)
                    draw.text((x1, y1), f"{model.names[int(cls)]} {conf:.2f}", fill=color)

    image.save(output_path)


def process_images(model_path, input_dir, output_dir, tile_size):
    model = YOLO(model_path)
    os.makedirs(output_dir, exist_ok=True)

    for image_file in os.listdir(input_dir):
        if image_file.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_dir, image_file)
            output_path = os.path.join(output_dir, image_file)
            split_and_predict(model, image_path, output_path, tile_size)


def parse_args():
    parser = argparse.ArgumentParser(description="Run tiled prediction on large CAD images.")
    parser.add_argument("--model", required=True, help="Path to a trained YOLO weights file.")
    parser.add_argument("--input-dir", required=True, help="Directory containing input images.")
    parser.add_argument("--output-dir", default="output", help="Directory for prediction images.")
    parser.add_argument("--tile-size", type=int, default=640, help="Tile size for sliding prediction.")
    return parser.parse_args()


def main():
    args = parse_args()
    process_images(args.model, args.input_dir, args.output_dir, args.tile_size)


if __name__ == "__main__":
    main()
