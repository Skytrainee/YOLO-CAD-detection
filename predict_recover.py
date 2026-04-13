import argparse
import os

import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from ultralytics import YOLO


def get_colors(num_colors):
    colors = plt.cm.get_cmap("hsv", num_colors)
    return [tuple(int(channel * 255) for channel in colors(i)[:3]) for i in range(num_colors)]


def predict_and_merge(model_path, image_dir, output_dir, original_image_dir, tile_size):
    model = YOLO(model_path)
    os.makedirs(output_dir, exist_ok=True)

    colors = get_colors(len(model.names))

    for original_image_file in os.listdir(original_image_dir):
        if original_image_file.lower().endswith((".png", ".jpg", ".jpeg")):
            original_image_path = os.path.join(original_image_dir, original_image_file)
            original_image = Image.open(original_image_path)
            img_width, img_height = original_image.size
            draw = ImageDraw.Draw(original_image)

            for i in range(0, img_width, tile_size):
                for j in range(0, img_height, tile_size):
                    tile_name = f"{os.path.splitext(original_image_file)[0]}_{i}_{j}.png"
                    img_path = os.path.join(image_dir, tile_name)
                    if not os.path.exists(img_path):
                        continue

                    result = model(img_path)[0]
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

            output_image_path = os.path.join(output_dir, original_image_file)
            original_image.save(output_image_path)


def parse_args():
    parser = argparse.ArgumentParser(description="Merge tile predictions back onto the original image.")
    parser.add_argument("--model", required=True, help="Path to a trained YOLO weights file.")
    parser.add_argument("--tiles-dir", required=True, help="Directory containing tiled images.")
    parser.add_argument("--original-dir", required=True, help="Directory containing original images.")
    parser.add_argument("--output-dir", default="output", help="Directory for merged prediction images.")
    parser.add_argument("--tile-size", type=int, default=640, help="Tile size used during splitting.")
    return parser.parse_args()


def main():
    args = parse_args()
    predict_and_merge(args.model, args.tiles_dir, args.output_dir, args.original_dir, args.tile_size)


if __name__ == "__main__":
    main()
