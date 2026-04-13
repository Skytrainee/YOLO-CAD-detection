# import cv2
# import numpy as np
# import torch
#
#
# # 定义滑动窗口函数
# def sliding_window(image, step_size, window_size):
#     for y in range(0, image.shape[0] - window_size[1] + 1, step_size):
#         for x in range(0, image.shape[1] - window_size[0] + 1, step_size):
#             yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])
#
#
# # 非极大值抑制（NMS）函数
# def nms(boxes, scores, iou_threshold=0.5):
#     # 将检测框的列表转换为 NumPy 数组
#     boxes = np.array(boxes)
#     scores = np.array(scores)
#
#     indices = cv2.dnn.NMSBoxes(boxes.tolist(), scores.tolist(), score_threshold=0.5, nms_threshold=iou_threshold)
#     indices = indices.flatten() if len(indices) > 0 else []
#
#     return [boxes[i] for i in indices]
#
#
# # 大图的滑动窗口预测和结果合并
# def predict_on_large_image(model, image, step_size, window_size):
#     result_image = np.zeros_like(image)
#     all_boxes = []  # 保存所有窗口中的检测框
#     all_scores = []  # 保存所有窗口中的置信度分数
#
#     for (x, y, window) in sliding_window(image, step_size, window_size):
#         # 对小图进行预测，得到预测框和置信度
#         predictions = model.predict(window)  # 预测的结果
#         for pred in predictions:
#             x1, y1, x2, y2 = pred['bbox']  # 小图中的检测框坐标
#             score = pred['confidence']  # 置信度得分
#
#             # 将检测框坐标转换回大图中的坐标
#             x1 += x
#             y1 += y
#             x2 += x
#             y2 += y
#
#             # 保存到总的检测框列表中
#             all_boxes.append([x1, y1, x2, y2])
#             all_scores.append(score)
#
#     # 应用非极大值抑制，去除重复框
#     final_boxes = nms(all_boxes, all_scores, iou_threshold=0.5)
#
#     # 在大图上绘制最终的检测结果
#     for (x1, y1, x2, y2) in final_boxes:
#         cv2.rectangle(result_image, (int(x1), int(y1)), (int(x2), int(y2)), color=(0, 255, 0), thickness=2)
#
#     return result_image
#
#
# # 加载训练好的模型
# def load_model(model_path):
#     # 加载模型
#     model = torch.load(model_path)
#     return model
#
#
# # 进行检测
# image = cv2.imread('C:/Users/lsk12/Desktop/CAD项目/9.6cad文件备份/images/117_9.3.png')
# model = load_model('C:/Users/lsk12/Desktop/py_learn/YOLO_Project/runs/detect/train113/weights/best.pt')
# result = predict_on_large_image(model, image, step_size=320, window_size=(640, 640))
#
# # 展示结果
# cv2.imshow('Prediction', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
# from ultralytics import YOLO
#
#
# # 定义滑动窗口函数
# def sliding_window(image, step_size, window_size):
#     if image is None:
#         raise ValueError("Image not loaded correctly.")
#
#     for y in range(0, image.shape[0] - window_size[1] + 1, step_size):
#         for x in range(0, image.shape[1] - window_size[0] + 1, step_size):
#             yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])
#
#
# # 非极大值抑制（NMS）函数
# def nms(boxes, scores, iou_threshold=0.5):
#     boxes = np.array(boxes)
#     scores = np.array(scores)
#
#     indices = cv2.dnn.NMSBoxes(boxes.tolist(), scores.tolist(), score_threshold=0.5, nms_threshold=iou_threshold)
#     indices = indices.flatten() if len(indices) > 0 else []
#
#     return [boxes[i] for i in indices]
#
#
# # 大图的滑动窗口预测和结果合并
# def predict_on_large_image(model, image, step_size, window_size):
#     result_image = np.zeros_like(image)
#     all_boxes = []  # 保存所有窗口中的检测框
#     all_scores = []  # 保存所有窗口中的置信度分数
#
#     for (x, y, window) in sliding_window(image, step_size, window_size):
#         # 对小图进行预测
#         results = model(window)  # YOLOv8 的预测结果
#
#         # 遍历每个检测结果（每个小图的预测结果）
#         for result in results:
#             boxes = result.boxes.xyxy.cpu().numpy()  # 提取边界框坐标
#             confidences = result.boxes.conf.cpu().numpy()  # 提取置信度
#
#             for box, conf in zip(boxes, confidences):
#                 x1, y1, x2, y2 = box  # 边界框坐标
#                 # 将检测框坐标转换回大图中的坐标
#                 x1 += x
#                 y1 += y
#                 x2 += x
#                 y2 += y
#
#                 # 保存到总的检测框列表中
#                 all_boxes.append([x1, y1, x2, y2])
#                 all_scores.append(conf)
#
#     # 应用非极大值抑制，去除重复框
#     final_boxes = nms(all_boxes, all_scores, iou_threshold=0.5)
#
#     # 在大图上绘制最终的检测结果
#     for (x1, y1, x2, y2) in final_boxes:
#         cv2.rectangle(result_image, (int(x1), int(y1)), (int(x2), int(y2)), color=(0, 255, 0), thickness=2)
#
#     return result_image
#
#
# # 加载训练好的模型
# def load_model(model_path):
#     # 加载 YOLOv8 模型
#     model = YOLO(model_path)  # 使用 ultralytics YOLO 加载模型
#     return model
#
#
# # 进行检测
# image_path = '100.png'  # 确保路径正确
# image = cv2.imread(image_path)
#
# if image is None:
#     raise ValueError(f"Failed to load image at path: {image_path}")
#
# model = load_model('C:/Users/lsk12/Desktop/py_learn/YOLO_Project/runs/detect/train113/weights/best.pt')
# result = predict_on_large_image(model, image, step_size=320, window_size=(640, 640))
#
# # 展示结果
# cv2.imshow('Prediction', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()








# import cv2
# import numpy as np
# from ultralytics import YOLO
#
#
# # 定义滑动窗口函数
# def sliding_window(image, step_size, window_size):
#     if image is None:
#         raise ValueError("Image not loaded correctly.")
#
#     for y in range(0, image.shape[0] - window_size[1] + 1, step_size):
#         for x in range(0, image.shape[1] - window_size[0] + 1, step_size):
#             yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])
#
#
# # 非极大值抑制（NMS）函数
# def nms(boxes, scores, iou_threshold=0.5):
#     boxes = np.array(boxes)
#     scores = np.array(scores)
#
#     indices = cv2.dnn.NMSBoxes(boxes.tolist(), scores.tolist(), score_threshold=0.5, nms_threshold=iou_threshold)
#     indices = indices.flatten() if len(indices) > 0 else []
#
#     return [boxes[i] for i in indices]
#
#
# # 大图的滑动窗口预测和结果合并
# def predict_on_large_image(model, image, step_size, window_size):
#     result_image = image.copy()  # 创建结果图像的副本以绘制检测框
#     all_boxes = []  # 保存所有窗口中的检测框
#     all_scores = []  # 保存所有窗口中的置信度分数
#
#     for (x, y, window) in sliding_window(image, step_size, window_size):
#         # 对小图进行预测
#         results = model(window)  # YOLOv8 的预测结果
#
#         # 遍历每个检测结果（每个小图的预测结果）
#         for result in results:
#             boxes = result.boxes.xyxy.cpu().numpy()  # 提取边界框坐标
#             confidences = result.boxes.conf.cpu().numpy()  # 提取置信度
#
#             for box, conf in zip(boxes, confidences):
#                 x1, y1, x2, y2 = box  # 边界框坐标
#                 # 将检测框坐标转换回大图中的坐标
#                 x1 += x
#                 y1 += y
#                 x2 += x
#                 y2 += y
#
#                 # 保存到总的检测框列表中
#                 all_boxes.append([x1, y1, x2, y2])
#                 all_scores.append(conf)
#
#     # 应用非极大值抑制，去除重复框
#     final_boxes = nms(all_boxes, all_scores, iou_threshold=0.5)
#
#     # 在大图上绘制最终的检测结果
#     for (x1, y1, x2, y2) in final_boxes:
#         cv2.rectangle(result_image, (int(x1), int(y1)), (int(x2), int(y2)), color=(0, 255, 0), thickness=2)
#
#     return result_image
#
#
# # 加载训练好的模型
# def load_model(model_path):
#     # 加载 YOLOv8 模型
#     model = YOLO(model_path)  # 使用 ultralytics YOLO 加载模型
#     return model
#
#
# # 进行检测
# image_path = 'C:/Users/lsk12/Desktop/CAD项目/9.6cad文件备份/images/100.png'  # 确保路径正确
# image = cv2.imread(image_path)
#
# if image is None:
#     raise ValueError(f"Failed to load image at path: {image_path}")
#
# model = load_model('C:/Users/lsk12/Desktop/py_learn/YOLO_Project/runs/detect/train113/weights/best.pt')
# result = predict_on_large_image(model, image, step_size=320, window_size=(640, 640))
#
# # 展示结果
# cv2.imshow('Prediction', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # 保存结果图像
# cv2.imwrite('C:/Users/lsk12/Desktop/100_predicted_result.png', result)  # 将结果保存为文件


# import cv2
# import numpy as np
# from ultralytics import YOLO
# from PIL import Image, ImageDraw, ImageFont
#
#
# # 定义滑动窗口函数
# def sliding_window(image, step_size, window_size):
#     if image is None:
#         raise ValueError("Image not loaded correctly.")
#
#     for y in range(0, image.shape[0] - window_size[1] + 1, step_size):
#         for x in range(0, image.shape[1] - window_size[0] + 1, step_size):
#             yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])
#
#
# # 非极大值抑制（NMS）函数
# def nms(boxes, scores, iou_threshold=0.5):
#     boxes = np.array(boxes)
#     scores = np.array(scores)
#
#     indices = cv2.dnn.NMSBoxes(boxes.tolist(), scores.tolist(), score_threshold=0.5, nms_threshold=iou_threshold)
#     indices = indices.flatten() if len(indices) > 0 else []
#
#     return [boxes[i] for i in indices]
#
#
# # 使用 Pillow 绘制中文和置信度
# def draw_label_with_chinese(image, text, position):
#     # 将 OpenCV 图像转换为 Pillow 图像
#     image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#     draw = ImageDraw.Draw(image_pil)
#
#     # 加载一个支持中文的字体文件，这里假设已经有一个 ttf 字体文件
#     font_path = 'C:/Windows/Fonts/simsun.ttc'  # 你需要指定正确的字体路径
#     font = ImageFont.truetype(font_path, 40)  # 设置字体大小
#
#     # 绘制中文文本
#     draw.text(position, text, font=font, fill=(255, 0, 0, 255))
#
#     # 将 Pillow 图像转换回 OpenCV 格式
#     return cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
#
#
# # 大图的滑动窗口预测和结果合并
# def predict_on_large_image(model, image, step_size, window_size):
#     result_image = image.copy()  # 创建结果图像的副本以绘制检测框
#     all_boxes = []  # 保存所有窗口中的检测框
#     all_scores = []  # 保存所有窗口中的置信度分数
#     all_classes = []  # 保存检测到的类别
#
#     for (x, y, window) in sliding_window(image, step_size, window_size):
#         # 对小图进行预测
#         results = model(window)  # YOLOv8 的预测结果
#
#         # 遍历每个检测结果（每个小图的预测结果）
#         for result in results:
#             boxes = result.boxes.xyxy.cpu().numpy()  # 提取边界框坐标
#             confidences = result.boxes.conf.cpu().numpy()  # 提取置信度
#             class_ids = result.boxes.cls.cpu().numpy()  # 提取类别 ID
#
#             for box, conf, class_id in zip(boxes, confidences, class_ids):
#                 x1, y1, x2, y2 = box  # 边界框坐标
#                 # 将检测框坐标转换回大图中的坐标
#                 x1 += x
#                 y1 += y
#                 x2 += x
#                 y2 += y
#
#                 # 保存到总的检测框列表中
#                 all_boxes.append([x1, y1, x2, y2])
#                 all_scores.append(conf)
#                 all_classes.append(int(class_id))
#
#     # 应用非极大值抑制，去除重复框
#     final_boxes = nms(all_boxes, all_scores, iou_threshold=0.5)
#
#     # 在大图上绘制最终的检测结果
#     for i, (x1, y1, x2, y2) in enumerate(final_boxes):
#         # 绘制检测框
#         cv2.rectangle(result_image, (int(x1), int(y1)), (int(x2), int(y2)), color=(0, 255, 0), thickness=2)
#
#         # 绘制标签和置信度，使用 Pillow 处理中文
#         label = f"{model.names[all_classes[i]]}: {all_scores[i]:.2f}"
#         result_image = draw_label_with_chinese(result_image, label, (int(x1), int(y1) - 10))
#
#     return result_image
#
#
# # 加载训练好的模型
# def load_model(model_path):
#     # 加载 YOLOv8 模型
#     model = YOLO(model_path)  # 使用 ultralytics YOLO 加载模型
#     return model
#
#
# # 进行检测
# image_path = 'C:/Users/lsk12/Desktop/CAD项目/9.6cad文件备份/images/87.png'  # 确保路径正确
# image = cv2.imread(image_path)
#
# if image is None:
#     raise ValueError(f"Failed to load image at path: {image_path}")
#
# model = load_model('C:/Users/lsk12/Desktop/py_learn/YOLO_Project/runs/detect/train113/weights/best.pt')
# result = predict_on_large_image(model, image, step_size=320, window_size=(640, 640))
#
# # 保存结果图像
# cv2.imwrite('C:/Users/lsk12/Desktop/87_predicted_result.png', result)  # 将结果保存为文件

import os
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import ImageFont, ImageDraw, Image
import colorsys


# 定义滑动窗口函数
def sliding_window(image, step_size, window_size):
    if image is None:
        raise ValueError("Image not loaded correctly.")

    for y in range(0, image.shape[0] - window_size[1] + 1, step_size):
        for x in range(0, image.shape[1] - window_size[0] + 1, step_size):
            yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])


# 非极大值抑制（NMS）函数
def nms(boxes, scores, iou_threshold=0.5):
    boxes = np.array(boxes)
    scores = np.array(scores)

    indices = cv2.dnn.NMSBoxes(boxes.tolist(), scores.tolist(), score_threshold=0.5, nms_threshold=iou_threshold)
    indices = indices.flatten() if len(indices) > 0 else []

    return [boxes[i] for i in indices]


# 动态生成 RGB 颜色
def generate_color_by_id(class_id, num_classes):
    hue = class_id / num_classes  # 根据类别 ID 生成不同的色调
    rgb_float = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  # HSV 转 RGB
    rgb = tuple([int(x * 255) for x in rgb_float])  # 将浮点数转为整数 (0-255)
    return rgb


# 使用 Pillow 绘制中文和置信度
def draw_label_with_chinese(image, text, position, color):
    # 将 OpenCV 图像转换为 Pillow 图像
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image_pil)

    # 加载一个支持中文的字体文件，例如 Windows 中的 simsun.ttc
    font_path = 'C:/Windows/Fonts/SimHei.ttf'  # 替换为您本地的字体路径
    try:
        font = ImageFont.truetype(font_path, 20)  # 设置字体大小
    except OSError:
        raise ValueError(f"Failed to load font from path: {font_path}")

    # 绘制中文文本
    draw.text(position, text, font=font, fill=color)

    # 将 Pillow 图像转换回 OpenCV 格式
    return cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)


# 大图的滑动窗口预测和结果合并
def predict_on_large_image(model, image, step_size, window_size):
    result_image = image.copy()  # 创建结果图像的副本以绘制检测框
    all_boxes = []  # 保存所有窗口中的检测框
    all_scores = []  # 保存所有窗口中的置信度分数
    all_classes = []  # 保存检测到的类别
    num_classes = len(model.names)  # 总类别数量

    for (x, y, window) in sliding_window(image, step_size, window_size):
        # 对小图进行预测
        results = model(window)  # YOLOv8 的预测结果

        # 遍历每个检测结果（每个小图的预测结果）
        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()  # 提取边界框坐标
            confidences = result.boxes.conf.cpu().numpy()  # 提取置信度
            class_ids = result.boxes.cls.cpu().numpy()  # 提取类别 ID

            for box, conf, class_id in zip(boxes, confidences, class_ids):
                x1, y1, x2, y2 = box  # 边界框坐标
                # 将检测框坐标转换回大图中的坐标
                x1 += x
                y1 += y
                x2 += x
                y2 += y

                # 保存到总的检测框列表中
                all_boxes.append([x1, y1, x2, y2])
                all_scores.append(conf)
                all_classes.append(int(class_id))

    # 应用非极大值抑制，去除重复框
    final_boxes = nms(all_boxes, all_scores, iou_threshold=0.5)

    # 在大图上绘制最终的检测结果
    for i, (x1, y1, x2, y2) in enumerate(final_boxes):
        class_id = all_classes[i]
        color = generate_color_by_id(class_id, num_classes)  # 动态生成颜色

        # 绘制检测框
        cv2.rectangle(result_image, (int(x1), int(y1)), (int(x2), int(y2)), color=color, thickness=2)

        # 绘制标签和置信度，使用 Pillow 处理中文
        label = f"{model.names[class_id]}: {all_scores[i]:.2f}"
        result_image = draw_label_with_chinese(result_image, label, (int(x1), int(y1) - 10), color)

    return result_image


# 加载训练好的模型
def load_model(model_path):
    # 加载 YOLOv8 模型
    model = YOLO(model_path)  # 使用 ultralytics YOLO 加载模型
    return model


# # 一、对单张图片进行检测
# image_path = 'C:/Users/lsk12/Desktop/CAD项目/9.6cad文件备份/images/156_9.3.png'  # 确保路径正确
# image = cv2.imread(image_path)
#
# if image is None:
#     raise ValueError(f"Failed to load image at path: {image_path}")
# # model = load_model('C:/Users/lsk12/Desktop/py_learn/YOLO_Project/runs/detect/train113/weights/best.pt')
# # model = load_model('C:/Users/lsk12/Desktop/best.pt')
# model = load_model('C:/Users/lsk12/Desktop/滑动窗口服务器训练结果/9.3训练结果/9.3迭代200次train105/weights/best.pt')
# result = predict_on_large_image(model, image, step_size=320, window_size=(640, 640))
#
# # 保存结果图像
# cv2.imwrite('C:/Users/lsk12/Desktop/滑动窗口服务器训练结果/预测结果测试/156_9.3predicted_result.png', result)  # 将结果保存为文件




# 二、同时对多张图片进行检测


def process_images_in_folder(model, input_folder, output_folder, step_size=320, window_size=(640, 640)):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有图片文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            if image is None:
                print(f"无法加载图片: {image_path}")
                continue

            # 对大图片进行预测
            result = predict_on_large_image(model, image, step_size=step_size, window_size=window_size)

            # 保存结果图像
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_predicted_result.png")
            cv2.imwrite(output_path, result)
            print(f"预测结果已保存: {output_path}")

# 使用模型对文件夹中的图片进行处理
input_folder = 'C:/Users/lsk12/Desktop/滑动窗口服务器训练结果/9.3训练结果/验证集图片'
output_folder = 'C:/Users/lsk12/Desktop/滑动窗口服务器训练结果/预测结果测试'
model_path = 'C:/Users/lsk12/Desktop/滑动窗口服务器训练结果/9.3训练结果/9.3迭代200次train105/weights/best.pt'

# 加载模型
model = load_model(model_path)

# 处理文件夹中的所有图片
process_images_in_folder(model, input_folder, output_folder)
