import os
import shutil
import re

# 定义原始文件夹和目标文件夹的路径
# folder_A = "C:\\Users\\lsk12\\Desktop\\CAD项目\\8.31CAD数据集和测试结果\\8.31完整文件"  # 替换为你的文件夹A路径
# annotations_output_folder = "C:\\Users\\lsk12\\Desktop\\CAD项目\\8.31CAD数据集和测试结果\\数据分类合并\\Annotations4"  # 替换为你想保存annotations.xml文件的路径


folder_A = "C:\\Users\\lsk12\\Desktop\\CAD项目\\9.3CAD数据集和测试结果\\9.3完整文件"  # 替换为你的文件夹A路径
annotations_output_folder = "C:\\Users\\lsk12\\Desktop\\CAD项目\\9.3CAD数据集和测试结果\\9.3数据分类合并\\Annotations"  # 替换为你想保存annotations.xml文件的路径


# 创建目标文件夹（如果不存在）
os.makedirs(annotations_output_folder, exist_ok=True)

# 自然排序函数，用于处理名称中包含数字的文件夹
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]

# 初始化标注文件的编号
annotation_number = 1

# 获取文件夹A中的所有子文件夹，并按自然顺序排序
subfolders = sorted(os.listdir(folder_A), key=natural_sort_key)

# 遍历排序后的文件夹
for subfolder in subfolders:
    subfolder_path = os.path.join(folder_A, subfolder)

    if os.path.isdir(subfolder_path):
        # 查找annotations.xml文件并复制到目标文件夹
        annotation_file = os.path.join(subfolder_path, "annotations.xml")
        if os.path.exists(annotation_file):
            new_annotation_name = f"{annotation_number}_9.3.xml"
            shutil.copy(annotation_file, os.path.join(annotations_output_folder, new_annotation_name))
            annotation_number += 1  # 更新标注文件编号

print(f"处理完成，复制了 {annotation_number - 1} 个 annotations.xml 文件。")
