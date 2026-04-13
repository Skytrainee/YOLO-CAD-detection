import argparse
import os

import cv2
from ultralytics import YOLO


def draw_detections(image, detections, class_names, confidence_threshold=0.7):
    for x1, y1, x2, y2, conf, class_id in detections:
        if conf < confidence_threshold:
            continue
        label = f"{class_names[int(class_id)]}: {conf:.2f}"
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(image, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return image


def detect_large_image(image_path, model, block_size=640):
    if not os.path.exists(image_path):
        print(f"File does not exist: {image_path}")
        return [], None

    large_image = cv2.imread(image_path)
    if large_image is None:
        print(f"Failed to load image: {image_path}")
        return [], None

    height, width, _ = large_image.shape
    all_detections = []

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            block = large_image[y : y + block_size, x : x + block_size]
            results = model.predict(block)
            detections = results[0].boxes.xyxy.cpu().numpy()
            confidences = results[0].boxes.conf.cpu().numpy()
            class_ids = results[0].boxes.cls.cpu().numpy()

            for det, conf, cls_id in zip(detections, confidences, class_ids):
                det[0] += x
                det[1] += y
                det[2] += x
                det[3] += y
                all_detections.append([det[0], det[1], det[2], det[3], conf, cls_id])

    return all_detections, large_image


def process_images(image_paths, model, block_size=2048, output_dir="output", confidence_threshold=0.7):
    os.makedirs(output_dir, exist_ok=True)
    class_names = model.names
    for image_path in image_paths:
        detections, large_image = detect_large_image(image_path, model, block_size)
        if large_image is None:
            continue
        result_image = draw_detections(large_image, detections, class_names, confidence_threshold)
        output_path = os.path.join(output_dir, os.path.basename(image_path))
        cv2.imwrite(output_path, result_image)
        print(f"Processed {image_path}, results saved to {output_path}")


def parse_args():
    parser = argparse.ArgumentParser(description="Run block-wise detection on one or more large images.")
    parser.add_argument("--model", required=True, help="Path to a trained YOLO weights file.")
    parser.add_argument("--images", nargs="+", required=True, help="One or more image paths to process.")
    parser.add_argument("--block-size", type=int, default=640, help="Block size for large-image inference.")
    parser.add_argument("--output-dir", default="output", help="Directory for result images.")
    parser.add_argument("--confidence-threshold", type=float, default=0.7, help="Minimum confidence to draw detections.")
    return parser.parse_args()


def main():
    args = parse_args()
    model = YOLO(args.model)
    process_images(args.images, model, args.block_size, args.output_dir, args.confidence_threshold)


if __name__ == "__main__":
    main()
