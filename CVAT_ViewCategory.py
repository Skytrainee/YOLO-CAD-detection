# import os
# import xml.etree.ElementTree as ET
# import glob
#
# def count_num(indir):
#     label_list = []
#     # 提取xml文件列表
#     annotations = glob.glob(os.path.join(indir, '*.xml'))
#
#     label_dict = {}  # 新建字典，用于存放各类标签名及其对应的数目
#     for file in annotations:  # 遍历xml文件
#         # 解析XML文件
#         with open(file, encoding='utf-8') as in_file:
#             tree = ET.parse(in_file)
#             root = tree.getroot()
#
#             # 遍历文件的所有box标签
#             for box in root.iter('box'):
#                 name = box.get('label')
#                 if name in label_dict.keys():
#                     label_dict[name] += 1  # 如果标签不是第一次出现，则+1
#                 else:
#                     label_dict[name] = 1  # 如果标签是第一次出现，则将该标签名对应的value初始化为1
#
#     # 打印结果
#     print("各类标签的数量分别为：")
#     for key in label_dict.keys():
#         print(f"{key}: {label_dict[key]}")
#         label_list.append(key)
#     print("标签类别如下：")
#     print(label_list)
#     return label_dict, label_list
#
# if __name__ == '__main__':
#     # xml文件所在的目录，修改此处
#     indir = 'data/Annotations'
#     count_num(indir)  # 调用函数统计各类标签数目

# import os
# import xml.etree.ElementTree as ET
# import glob
#
#
# def count_num(indir):
#     label_list = []
#     # 提取xml文件列表
#     annotations = glob.glob(os.path.join(indir, '*.xml'))
#
#     label_dict = {}  # 新建字典，用于存放各类标签名及其对应的数目
#     for file in annotations:  # 遍历xml文件
#         # 解析XML文件
#         with open(file, encoding='utf-8') as in_file:
#             tree = ET.parse(in_file)
#             root = tree.getroot()
#
#             # 遍历文件的所有box标签
#             for box in root.iter('box'):
#                 for attribute in box.iter('attribute'):
#                     name = attribute.text  # 获取attribute标签的文本内容
#                     if name:  # 确保不是空值
#                         if name in label_dict:
#                             label_dict[name] += 1  # 如果标签不是第一次出现，则+1
#                         else:
#                             label_dict[name] = 1  # 如果标签是第一次出现，则将该标签名对应的value初始化为1
#
#     # 打印结果
#     print("各类标签的数量分别为：")
#     for key in label_dict.keys():
#         print(f"{key}: {label_dict[key]}")
#         label_list.append(key)
#
#     print("标签类别如下：")
#     print(label_list)
#
#     # 打印不同种类的总数
#     total_classes = len(label_list)
#     print(f"总共有 {total_classes} 种不同的种类。")
#
#     return label_dict, label_list
#
#
# if __name__ == '__main__':
#     # xml文件所在的目录，修改此处
#     indir = 'data/Annotations'
#     count_num(indir)  # 调用函数统计各类标签数目

import os
import xml.etree.ElementTree as ET
import glob

def count_num(indir):
    label_set = set()  # 使用集合来去重标签名
    # 提取xml文件列表
    annotations = glob.glob(os.path.join(indir, '*.xml'))

    label_dict = {}  # 新建字典，用于存放各类标签名及其对应的数目
    for file in annotations:  # 遍历xml文件
        # 解析XML文件
        with open(file, encoding='utf-8') as in_file:
            tree = ET.parse(in_file)
            root = tree.getroot()

            # 遍历文件的所有box标签
            for box in root.iter('box'):
                for attribute in box.iter('attribute'):
                    name = attribute.text  # 获取attribute标签的文本内容
                    if name:  # 确保不是空值
                        if name in label_dict:
                            label_dict[name] += 1  # 如果标签不是第一次出现，则+1
                        else:
                            label_dict[name] = 1  # 如果标签是第一次出现，则将该标签名对应的value初始化为1
                        label_set.add(name)  # 将标签名加入集合，避免重复

    # 打印结果
    print("各类标签的数量分别为：")
    for key in label_dict.keys():
        print(f"{key}: {label_dict[key]}")
    # 打印结果为字典形式
    print("各类标签的数量分别为：")
    print(label_dict)

    # 将标签列表按字母顺序排序
    label_list = sorted(label_set)

    print("标签类别如下：")
    print(label_list)

    # 打印不同种类的总数
    total_classes = len(label_list)
    print(f"总共有 {total_classes} 种不同的种类。")

    return label_dict, label_list


if __name__ == '__main__':
    # xml文件所在的目录，修改此处
    # indir = 'data/Annotations'
    indir = 'C:/Users/lsk12/Desktop/CAD项目/8.31+9.3数据合并/Annotations'
    count_num(indir)  # 调用函数统计各类标签数目
