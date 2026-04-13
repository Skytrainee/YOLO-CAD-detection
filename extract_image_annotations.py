# import os
# import shutil
#
#
# # 定义源文件夹路径和目标文件夹路径
# source_folder = 'C:\\Users\\lsk12\\Desktop\\CAD项目\\8.31CAD数据集和测试结果\\8.31完整文件'  # 替换为你的源文件夹路径
# images_destination = 'C:\\Users\\lsk12\\Desktop\\CAD项目\\8.31CAD数据集和测试结果\\数据分类合并\\images'  # 替换为目标图片文件夹路径
# annotations_destination = 'C:\\Users\\lsk12\\Desktop\\CAD项目\\8.31CAD数据集和测试结果\\数据分类合并\\Annotations'  # 替换为目标注释文件夹路径
#
# folders_without_images = []
#
# # 遍历 source_folder 下的所有文件夹和子文件夹
# for root, dirs, files in os.walk(source_folder):
#     has_image = False
#     print(f"正在检查文件夹: {root}")  # 打印当前检查的文件夹
#     for file in files:
#         print(f"找到文件: {file}")  # 打印文件名
#         if file.lower().endswith('.png'):  # 忽略大小写检查 .png 扩展名
#             has_image = True
#             # 找到 .png 图片文件并复制到目标文件夹
#             image_file_path = os.path.join(root, file)
#             shutil.copy(image_file_path, os.path.join(images_destination, file))
#             print(f"复制图片: {image_file_path}")  # 打印复制操作
#
#         if file == 'annotations.xml':
#             # 找到 annotations.xml 文件并复制到目标文件夹
#             annotation_file_path = os.path.join(root, file)
#             shutil.copy(annotation_file_path,
#                         os.path.join(annotations_destination, f"{os.path.basename(root)}_annotations.xml"))
#             print(f"复制注释文件: {annotation_file_path}")  # 打印复制操作
#
#     if not has_image:
#         folders_without_images.append(root)
#
# # 输出没有图片的文件夹名称
# if folders_without_images:
#     print("以下文件夹没有找到图片:")
#     for folder in folders_without_images:
#         print(folder)
# else:
#     print("所有文件夹都包含图片。")


import os
import shutil

# 定义源文件夹路径和目标文件夹路径
source_folder = 'C:\\Users\\lsk12\\Desktop\\CAD项目\\8.31CAD数据集和测试结果\\8.31完整文件'  # 替换为你的源文件夹路径
images_destination = 'C:\\Users\\lsk12\\Desktop\\CAD项目\\8.31CAD数据集和测试结果\\数据分类合并\\images'  # 替换为目标图片文件夹路径

# 创建目标文件夹，如果它不存在
os.makedirs(images_destination, exist_ok=True)

# 计数器，用于检查提取的图片数量
image_count = 0

# 遍历 source_folder 下的所有文件夹和子文件夹
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.lower().endswith('.png'):  # 忽略大小写检查 .png 扩展名
            image_count += 1
            # 找到 .png 图片文件并复制到目标文件夹
            image_file_path = os.path.join(root, file)
            shutil.copy(image_file_path, os.path.join(images_destination, file))
            print(f"复制图片: {image_file_path}")

# 打印提取的图片总数
print(f"总共提取了 {image_count} 张图片。")







#image_count = 0
# # 遍历 source_folder 下的所有文件夹和子文件夹
# for root, dirs, files in os.walk(source_folder):
#     for file in files:
#         if file.lower().endswith('.png'):  # 忽略大小写检查 .png 扩展名
#             image_count += 1
#             # 生成唯一的数字标识符文件名
#             unique_filename = f"image_{image_count:03d}.png"  # 使用三位数字表示，例如 image_001.png
#             # 找到 .png 图片文件并复制到目标文件夹
#             image_file_path = os.path.join(root, file)
#             shutil.copy(image_file_path, os.path.join(images_destination, unique_filename))
#             print(f"复制图片: {unique_filename}")
#
# # 打印提取的图片总数
# print(f"总共提取了 {image_count} 张图片。")