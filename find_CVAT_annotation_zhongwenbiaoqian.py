# import os
# import xml.etree.ElementTree as ET
#
# # 将此路径替换为实际包含XML文件的文件夹路径
# xml_folder = 'C:\\Users\\lsk12\\Desktop\\CAD项目\\8.31CAD数据集和测试结果\\数据分类合并\\Annotations2'
#
# # 存储符合条件的文件名
# valid_files = []
#
# # 遍历文件夹中的所有文件
# for file in os.listdir(xml_folder):
#     if file.endswith('.xml'):  # 确保处理的是xml文件
#         file_path = os.path.join(xml_folder, file)
#         tree = ET.parse(file_path)
#         root = tree.getroot()
#
#         # 假设所有的<box>标签都在<image>标签下
#         for image in root.findall('image'):
#             all_chinese = True  # 假设所有属性值都是中文
#             for box in image.findall('box'):
#                 attribute = box.find('attribute')
#                 if attribute is not None and attribute.get('name') == '名称':
#                     value = attribute.get('value')
#                     # 确保 value 不是 None
#                     if value is not None:
#                         # 检查值是否只包含中文字符
#                         if not all('\u4e00' <= char <= '\u9fff' for char in value):
#                             all_chinese = False
#                             break
#                     else:
#                         # 如果 value 是 None，可以设置 all_chinese 为 False 或进行其他处理
#                         all_chinese = False
#                         break
#
#             if all_chinese:
#                 valid_files.append(file)
#
# # 输出符合条件的文件名
# for vf in valid_files:
#     print(vf)


import os
import xml.etree.ElementTree as ET
import glob
import re


def is_chinese(string):
    """
    检查字符串是否只包含中文字符
    """
    for char in string:
        if not re.match(r'[\u4e00-\u9fff]', char):
            return False
    return True


def check_chinese_in_xml(indir):
    # 提取xml文件列表
    annotations = glob.glob(os.path.join(indir, '*.xml'))

    chinese_only_files = []  # 用于存放符合条件的文件名

    for file in annotations:  # 遍历xml文件
        all_chinese = True  # 假设该文件中的所有属性都只包含中文
        # 解析XML文件
        with open(file, encoding='utf-8') as in_file:
            tree = ET.parse(in_file)
            root = tree.getroot()

            # 遍历文件的所有box标签
            for box in root.iter('box'):
                for attribute in box.iter('attribute'):
                    name = attribute.text  # 获取attribute标签的文本内容
                    if name and not is_chinese(name):  # 如果不是只包含中文字符
                        all_chinese = False
                        break
                if not all_chinese:
                    break

        if all_chinese:
            chinese_only_files.append(os.path.basename(file))  # 只包含中文的文件名加入列表

    # 打印符合条件的文件名
    print("文件中所有<box>属性值只包含中文的文件名如下：")
    for filename in chinese_only_files:
        print(filename)

    return chinese_only_files


if __name__ == '__main__':
    # xml文件所在的目录，修改此处
    # indir = 'C:\\Users\\lsk12\\Desktop\\CAD项目\\8.31CAD数据集和测试结果\\数据分类合并\\Annotations2'
    indir = 'C:\\Users\\lsk12\\Desktop\\CAD项目\\9.3CAD数据集和测试结果\\9.3数据分类合并\\Annotations'
    check_chinese_in_xml(indir)  # 调用函数
