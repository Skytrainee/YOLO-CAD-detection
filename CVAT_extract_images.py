import os
import shutil
import re

# 定义原始文件夹和目标文件夹的路径
# folder_A = "C:\\Users\\lsk12\\Desktop\\CAD项目\\8.31CAD数据集和测试结果\\8.31完整文件"  # 替换为你的文件夹A路径
# images_output_folder = "C:\\Users\\lsk12\\Desktop\\CAD项目\\8.31CAD数据集和测试结果\\数据分类合并\\images4"  # 替换为你想保存图片文件的路径

folder_A = "C:\\Users\\lsk12\\Desktop\\CAD项目\\9.3CAD数据集和测试结果\\9.3完整文件"  # 替换为你的文件夹A路径
images_output_folder = "C:\\Users\\lsk12\\Desktop\\CAD项目\\9.3CAD数据集和测试结果\\9.3数据分类合并\\images"  # 替换为你想保存annotations.xml文件的路径
# 创建目标文件夹（如果不存在）
os.makedirs(images_output_folder, exist_ok=True)

# 自然排序函数，用于处理名称中包含数字的文件夹
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]

# 初始化图片文件的编号
image_number = 1

# 获取文件夹A中的所有子文件夹，并按自然顺序排序
subfolders = sorted(os.listdir(folder_A), key=natural_sort_key)

# 遍历排序后的文件夹
for subfolder in subfolders:
    subfolder_path = os.path.join(folder_A, subfolder)

    if os.path.isdir(subfolder_path):
        # 查找image或images文件夹中的图片文件并复制到目标文件夹
        image_folder_name = "image" if os.path.exists(os.path.join(subfolder_path, "image")) else "images"
        image_folder = os.path.join(subfolder_path, image_folder_name)
        if os.path.exists(image_folder):
            for image_file in os.listdir(image_folder):
                image_file_path = os.path.join(image_folder, image_file)
                if os.path.isfile(image_file_path):
                    new_image_name = f"{image_number}_9.3.png"  # 假设图片格式是.png，如果不是，请替换
                    shutil.copy(image_file_path, os.path.join(images_output_folder, new_image_name))
                    image_number += 1  # 更新图片文件编号
                    break  # 只复制一张图片

print(f"处理完成，复制了 {image_number - 1} 张图片文件。")
