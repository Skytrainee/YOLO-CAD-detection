import argparse
import os

from PIL import Image


def split_image(image_path, output_dir, tile_sizes):
    img = Image.open(image_path)
    img_width, img_height = img.size
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    os.makedirs(output_dir, exist_ok=True)

    for tile_size in tile_sizes:
        for i in range(0, img_width, tile_size):
            for j in range(0, img_height, tile_size):
                box = (i, j, min(i + tile_size, img_width), min(j + tile_size, img_height))
                img_cropped = img.crop(box)
                img_cropped.save(os.path.join(output_dir, f"{base_name}_{tile_size}_{i}_{j}.png"))


def batch_split_images(input_dir, output_dir, tile_sizes):
    os.makedirs(output_dir, exist_ok=True)
    for image_file in os.listdir(input_dir):
        if image_file.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_dir, image_file)
            split_image(image_path, output_dir, tile_sizes)


def parse_args():
    parser = argparse.ArgumentParser(description="Split large images into multiple tile sizes.")
    parser.add_argument("--input-dir", required=True, help="Directory containing source images.")
    parser.add_argument("--output-dir", required=True, help="Directory for generated tiles.")
    parser.add_argument("--tile-sizes", type=int, nargs="+", default=[320, 640, 800], help="One or more tile sizes in pixels.")
    return parser.parse_args()


def main():
    args = parse_args()
    batch_split_images(args.input_dir, args.output_dir, args.tile_sizes)


if __name__ == "__main__":
    main()
