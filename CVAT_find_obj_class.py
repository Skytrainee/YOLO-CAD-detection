# import os
# import xml.etree.ElementTree as ET
#
# def extract_classes_from_xml(xml_folder):
#     classes = set()
#     for xml_file in os.listdir(xml_folder):
#         if xml_file.endswith('.xml'):
#             tree = ET.parse(os.path.join(xml_folder, xml_file))
#             root = tree.getroot()
#             # 遍历所有的box标签，提取label属性值作为类别名称
#             for box in root.iter('box'):
#                 class_name = box.get('label')
#                 classes.add(class_name)
#     return classes
#
# # 示例用法
# xml_folder = 'data/Annotations'
# # xml_folder = 'C:\\Users\\lsk12\\Desktop\\测试中文标签\\Annotations'
#
# classes = extract_classes_from_xml(xml_folder)
# classes = sorted(classes)  # 排序以确保一致性
#
# # 打印类别列表
# print(classes)
#
# # 将类别列表保存到文件中
# with open('classes.txt', 'w', encoding='utf-8') as f:
#     for cls in classes:
#         f.write(f"{cls}\n")



import os
import xml.etree.ElementTree as ET

def extract_classes_from_xml(xml_folder):
    classes = set()
    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            tree = ET.parse(os.path.join(xml_folder, xml_file))
            root = tree.getroot()
            # 遍历所有的box标签，提取attribute标签中的名称属性值
            for box in root.iter('box'):
                for attribute in box.iter('attribute'):
                    class_name = attribute.text  # 获取attribute标签的文本内容
                    if class_name:  # 确保不是空值
                        classes.add(class_name)
    return classes

# 示例用法
# xml_folder = 'data/Annotations'
xml_folder = 'C:/Users/lsk12/Desktop/CAD项目/8.31+9.3数据合并/Annotations'

classes = extract_classes_from_xml(xml_folder)
classes = sorted(classes)  # 排序以确保一致性

# 打印类别列表
print(classes)

# 将类别列表保存到文件中
with open('classes.txt', 'w', encoding='utf-8') as f:
    for cls in classes:
        f.write(f"{cls}\n")
