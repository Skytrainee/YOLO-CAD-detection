import argparse
import subprocess

import torch


def clear_memory():
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def build_train_command(args):
    return [
        "yolo",
        "task=detect",
        "mode=train",
        f"model={args.model}",
        f"data={args.data}",
        f"batch={args.batch}",
        f"epochs={args.epochs}",
        f"imgsz={args.imgsz}",
        f"workers={args.workers}",
        f"device={args.device}",
    ]


def parse_args():
    parser = argparse.ArgumentParser(description="Train a YOLO model for CAD object detection.")
    parser.add_argument("--model", default="yolov8n.pt", help="Base model or model yaml.")
    parser.add_argument("--data", required=True, help="Dataset yaml file.")
    parser.add_argument("--batch", type=int, default=8, help="Batch size.")
    parser.add_argument("--epochs", type=int, default=100, help="Number of training epochs.")
    parser.add_argument("--imgsz", type=int, default=640, help="Training image size.")
    parser.add_argument("--workers", type=int, default=2, help="Number of dataloader workers.")
    parser.add_argument("--device", default="0", help="Training device, for example 0 or cpu.")
    return parser.parse_args()


def main():
    args = parse_args()
    subprocess.run(build_train_command(args), check=True)
    clear_memory()


if __name__ == "__main__":
    main()
