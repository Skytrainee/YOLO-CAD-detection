# import os
# import random
#
# trainval_percent = 0.9
# train_percent = 0.9
# xmlfilepath = 'data/Annotations2'
# # xmlfilepath = 'C:\\Users\\lsk12\\Desktop\\测试中文标签\\Annotations'
#
# txtsavepath = 'data/ImageSets'
# total_xml = os.listdir(xmlfilepath)
#
# num = len(total_xml)
# list = range(num)
# tv = int(num * trainval_percent)
# tr = int(tv * train_percent)
# trainval = random.sample(list, tv)
# train = random.sample(trainval, tr)
#
# ftrainval = open('data/ImageSets/trainval.txt', 'w')
# ftest = open('data/ImageSets/test.txt', 'w')
# ftrain = open('data/ImageSets/train.txt', 'w')
# fval = open('data/ImageSets/val.txt', 'w')
#
# for i in list:
#     name = total_xml[i][:-4] + '\n'
#     if i in trainval:
#         ftrainval.write(name)
#         if i in train:
#             ftrain.write(name)
#         else:
#             fval.write(name)
#     else:
#         ftest.write(name)
#
# ftrainval.close()
# ftrain.close()
# fval.close()
# ftest.close()



# 2、过滤掉txt文件中没有坐标的图片（没有物体的图片）

import os
import random
import xml.etree.ElementTree as ET

trainval_percent = 0.9
train_percent = 0.9
xmlfilepath = 'data/Annotations'
txtsavepath = 'data/ImageSets'
os.makedirs(txtsavepath, exist_ok=True)
total_xml = os.listdir(xmlfilepath)

# 检查标注文件是否包含有效的 box 标注
def is_xml_file_empty(xml_file_path):
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # 遍历文件中的 box 标签
        for box in root.iter('box'):
            name_element = box.find('attribute[@name="名称"]')  # 检查属性名称为 "名称" 的标签
            if name_element is not None and name_element.text and name_element.text.strip():  # name 属性存在且不为空
                return False  # 文件中有有效的标注
        return True  # 没有找到有效的物体标注

    except ET.ParseError:
        return True  # 如果 XML 文件解析失败，则视为无效文件


# 筛选掉没有有效标注的 XML 文件
valid_xml_files = []
for xml_file in total_xml:
    xml_file_path = os.path.join(xmlfilepath, xml_file)

    if not is_xml_file_empty(xml_file_path):
        valid_xml_files.append(xml_file)

num = len(valid_xml_files)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

# 创建 txt 文件存储训练集、验证集和测试集的文件名
ftrainval = open(os.path.join(txtsavepath, 'trainval.txt'), 'w')
ftest = open(os.path.join(txtsavepath, 'test.txt'), 'w')
ftrain = open(os.path.join(txtsavepath, 'train.txt'), 'w')
fval = open(os.path.join(txtsavepath, 'val.txt'), 'w')

for i in list:
    name = valid_xml_files[i][:-4] + '\n'  # 去除 .xml 后缀
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
