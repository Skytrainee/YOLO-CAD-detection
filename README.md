# YOLO-based Object Detection for CAD Images

Utilities for CAD image preprocessing, dataset conversion, YOLO training, and large-image inference.

## What This Repository Contains

This project mainly includes:

- image tiling scripts for large CAD drawings
- CVAT annotation extraction and conversion helpers
- YOLO training entry scripts
- prediction scripts for regular and large CAD images
- custom YOLO model yaml files

## What Is Not Included

To make the repository suitable for open source release, large local assets are excluded:

- trained weights such as `*.pt`
- training and prediction outputs such as `runs/` and `output/`
- local datasets and annotation folders
- IDE configuration and local environment files

If you want to share a trained model, upload it separately through GitHub Releases, Hugging Face, Google Drive, or another artifact hosting service.

## Environment

Python 3.10+ is recommended.

Install dependencies:

```bash
pip install -r requirements.txt
```

If you use `pdf2image`, you may also need to install Poppler separately on your system.

## Repository Structure

```text
.
├── RUN_YOLO.py                    # training entry script
├── bigtosmall.py                  # split large images into fixed-size tiles
├── bigtosmall2.py                 # split large images into multiple tile sizes
├── cad_model_predict01.py         # basic YOLO prediction entry
├── cad_model_predict02.py         # optional resize + YOLO prediction
├── predict_bigpicture.py          # tiled prediction on large images
├── predict_recover.py             # merge tile predictions back to full image
├── segment_predict.py             # block-wise inference on large images
├── CVAT_*.py                      # CVAT annotation conversion utilities
├── XML_to_TXT.py                  # VOC/XML to YOLO-style conversion helper
├── yolov8_custom.yaml             # custom YOLO model config
└── yolov8_CBAM.yaml               # custom YOLO model config with CBAM
```

## Quick Start

### 1. Train a model

```bash
python RUN_YOLO.py --data path/to/dataset.yaml --model yolov8n.pt --epochs 100 --imgsz 640
```

### 2. Split large CAD images

```bash
python bigtosmall.py --input-dir path/to/images --output-dir path/to/tiles --tile-size 640
```

### 3. Predict on a directory of images

```bash
python cad_model_predict01.py --model path/to/best.pt --source path/to/images --save-conf
```

### 4. Predict on very large CAD images by tiling

```bash
python predict_bigpicture.py --model path/to/best.pt --input-dir path/to/images --output-dir output --tile-size 640
```

### 5. Merge tile predictions back to original images

```bash
python predict_recover.py --model path/to/best.pt --tiles-dir path/to/tiles --original-dir path/to/originals --output-dir output --tile-size 640
```

## Data Preparation Notes

Several scripts in this repository are utility scripts written during experimentation. The most reusable way to work with this project is:

1. prepare images and annotations with the `CVAT_*.py` and XML conversion scripts
2. create a dataset yaml file for Ultralytics YOLO
3. train with `RUN_YOLO.py`
4. run prediction with one of the provided inference scripts

## Before Publishing To GitHub

Recommended final checks:

1. confirm you have the right to publish the code, dataset metadata, and any example images
2. keep large weights and private data out of the repository
3. replace placeholder paths in your own local commands with relative or user-provided paths
4. create the GitHub repository first, then push the local repository

## Suggested Git Commands

```bash
git init
git add .
git commit -m "Initial open-source release"
git branch -M main
git remote add origin https://github.com/<your-name>/<your-repo>.git
git push -u origin main
```

## License

This repository is released under the MIT License. See [LICENSE](LICENSE).
