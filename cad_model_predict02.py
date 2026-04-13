import argparse
import os

import cv2
from ultralytics import YOLO


def resize_image(image, width=1280, height=720):
    return cv2.resize(image, (width, height))


def resize_images_in_dir(folder_path, width, height):
    for file_name in os.listdir(folder_path):
        if not file_name.lower().endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")):
            continue
        image_path = os.path.join(folder_path, file_name)
        img = cv2.imread(image_path)
        if img is None:
            continue
        img_resized = resize_image(img, width=width, height=height)
        cv2.imwrite(image_path, img_resized)


def parse_args():
    parser = argparse.ArgumentParser(description="Optionally resize images in a directory and run YOLO prediction on them.")
    parser.add_argument("--model", required=True, help="Path to a trained YOLO weights file.")
    parser.add_argument("--source", required=True, help="Directory containing images to process.")
    parser.add_argument("--width", type=int, default=1280, help="Resize width.")
    parser.add_argument("--height", type=int, default=720, help="Resize height.")
    parser.add_argument("--skip-resize", action="store_true", help="Run prediction without resizing source images first.")
    parser.add_argument("--save-conf", action="store_true", help="Save confidence values in the results.")
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.skip_resize:
        resize_images_in_dir(args.source, args.width, args.height)

    model = YOLO(args.model)
    model.predict(source=args.source, save=True, save_conf=args.save_conf)


if __name__ == "__main__":
    main()
