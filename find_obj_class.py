import os
import xml.etree.ElementTree as ET

def extract_classes_from_xml(xml_folder):
    classes = set()
    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            tree = ET.parse(os.path.join(xml_folder, xml_file))
            root = tree.getroot()
            for obj in root.findall('object'):
                class_name = obj.find('name').text
                classes.add(class_name)
    return classes

# 示例用法
xml_folder = 'data/Annotations'
# xml_folder = 'C:\\Users\\lsk12\\Desktop\\测试中文标签\\Annotations'

classes = extract_classes_from_xml(xml_folder)
classes = sorted(classes)  # 排序以确保一致性

# 打印类别列表
print(classes)

# 将类别列表保存到文件中
with open('classes.txt', 'w', encoding='utf-8') as f:
    for cls in classes:
        f.write(f"{cls}\n")
