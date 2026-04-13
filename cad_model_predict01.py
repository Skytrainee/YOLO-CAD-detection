import argparse

from ultralytics import YOLO


def parse_args():
    parser = argparse.ArgumentParser(description="Run YOLO prediction on an image or directory.")
    parser.add_argument("--model", required=True, help="Path to a trained YOLO weights file.")
    parser.add_argument("--source", required=True, help="Image, directory, video, or glob pattern.")
    parser.add_argument("--save-conf", action="store_true", help="Save confidence values in the results.")
    return parser.parse_args()


def main():
    args = parse_args()
    model = YOLO(args.model)
    model.predict(source=args.source, save=True, save_conf=args.save_conf)


if __name__ == "__main__":
    main()
