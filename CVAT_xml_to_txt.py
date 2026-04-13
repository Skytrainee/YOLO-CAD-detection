# -*- coding: utf-8 -*-
# import os
# import xml.etree.ElementTree as ET
#
# # 设置数据集的分类
# sets = ['train', 'test', 'val']
# classes = ['三通', '上料系统', '人孔', '仓', '仓壁振动器', '出料口', '变径', '变送器', '吸尘罩', '四通', '圆盘', '圆风管立管托座', '圆风管立管支撑', '垂直拉紧装置', '埋件', '基础', '墙皮', '小便池', '底座', '托座', '振动器', '支座', '料仓', '未知', '柱', '标高', '栏杆', '楼梯', '檩托', '法兰', '法斗', '洗手池', '洞', '混合室', '溜槽', '漏斗', '灭火器', '牛腿节点', '电子秤', '电缆支架', '皮带机', '盲板', '空气炮', '窗', '管道', '给料机', '耐磨件', '胶带机', '节点', '螺栓', '衬板', '蹲厕', '轴网', '进料口', '通廊', '通风器', '通风器支座节点', '配电器', '配管图', '钢板', '钢梯', '钢衬板', '钢链', '门', '阀门', '除尘器', '除尘点', '除铁器', '隔离器']
#
# # 进行归一化操作
# def convert(size, box):
#     dw = 1. / size[0]  # 1/width
#     dh = 1. / size[1]  # 1/height
#     x = (box[0] + box[1]) / 2.0 * dw  # 中心x坐标标准化
#     y = (box[2] + box[3]) / 2.0 * dh  # 中心y坐标标准化
#     w = (box[1] - box[0]) * dw  # 宽度标准化
#     h = (box[3] - box[2]) * dh  # 高度标准化
#     return (x, y, w, h)
#
# # 将CVAT生成的xml文件转化为YOLO的label文件
# def convert_annotation(image_id, image_format):
#     in_file = open(f'data/Annotations/{image_id}.xml', encoding='utf-8')
#     out_file = open(f'data/labels/{image_id}.txt', 'w', encoding='utf-8')
#     tree = ET.parse(in_file)
#     root = tree.getroot()
#     size = (int(root.find('image').get('width')), int(root.find('image').get('height')))
#
#     for box in root.iter('box'):
#         cls = box.get('label')
#         if cls not in classes:
#             continue
#         cls_id = classes.index(cls)
#         b = (float(box.get('xtl')), float(box.get('xbr')),
#              float(box.get('ytl')), float(box.get('ybr')))
#         bb = convert(size, b)
#         if any(coord < 0 or coord > 1 for coord in bb):
#             print(f"Warning: Coordinates out of bounds in image {image_id}. Check annotation data.")
#         out_file.write(f"{cls_id} {' '.join(map(str, bb))}\n")
#
# # 获取工作目录
# def get_working_directory():
#     return os.getcwd()
#
# # 主函数
# def main():
#     wd = get_working_directory()
#     print(wd)
#
#     for image_set in sets:
#         # 创建labels文件夹，如果不存在则创建
#         if not os.path.exists('data/labels/'):
#             os.makedirs('data/labels/')
#
#         # 读取ImageSets/Main 中的train、test、val文件的内容
#         image_ids = open(f'data/ImageSets/{image_set}.txt').read().strip().split()
#         list_file = open(f'data/{image_set}.txt', 'w')
#
#         # 检测图像格式
#         image_format = None
#         for fmt in ['.png', '.jpg', '.jpeg']:
#             if os.path.exists(f'data/images/{image_ids[0]}{fmt}'):
#                 image_format = fmt
#                 break
#
#         if image_format is None:
#             raise Exception("Unsupported image format or image not found!")
#
#         # 遍历图像ID，进行标注转换
#         for image_id in image_ids:
#             list_file.write(f'data/images/{image_id}{image_format}\n')
#             convert_annotation(image_id, image_format)
#
#         list_file.close()
#
# if __name__ == "__main__":
#     main()



#
# import os
# import xml.etree.ElementTree as ET
#
# # 设置数据集的分类
# sets = ['train', 'test', 'val']
# classes = ['三通', '上料系统', '人孔', '仓', '仓壁振动器', '出料口', '变径', '变送器', '吸尘罩', '四通', '圆盘', '圆风管立管托座', '圆风管立管支撑', '垂直拉紧装置', '埋件', '基础', '墙皮', '小便池', '底座', '托座', '振动器', '支座', '料仓', '未知', '柱', '标高', '栏杆', '楼梯', '檩托', '法兰', '法斗', '洗手池', '洞', '混合室', '溜槽', '漏斗', '灭火器', '牛腿节点', '电子秤', '电缆支架', '皮带机', '盲板', '空气炮', '窗', '管道', '给料机', '耐磨件', '胶带机', '节点', '螺栓', '衬板', '蹲厕', '轴网', '进料口', '通廊', '通风器', '通风器支座节点', '配电器', '配管图', '钢板', '钢梯', '钢衬板', '钢链', '门', '阀门', '除尘器', '除尘点', '除铁器', '隔离器']
#
# # 进行归一化操作
# def convert(size, box):
#     dw = 1. / size[0]  # 1/width
#     dh = 1. / size[1]  # 1/height
#     x = (box[0] + box[1]) / 2.0 * dw  # 中心x坐标标准化
#     y = (box[2] + box[3]) / 2.0 * dh  # 中心y坐标标准化
#     w = (box[1] - box[0]) * dw  # 宽度标准化
#     h = (box[3] - box[2]) * dh  # 高度标准化
#     return (x, y, w, h)
#
# # 将CVAT生成的xml文件转化为YOLO的label文件
# def convert_annotation(image_id, image_format):
#     in_file = open(f'data/Annotations/{image_id}.xml', encoding='utf-8')
#     out_file = open(f'data/labels/{image_id}.txt', 'w', encoding='utf-8')
#     tree = ET.parse(in_file)
#     root = tree.getroot()
#     size = (int(root.find('image').get('width')), int(root.find('image').get('height')))
#
#     for box in root.iter('box'):
#         cls = box.find('attribute[@name="名称"]').text  # 获取box中的名称属性值，例如"轴网"
#         if cls not in classes:
#             print(f"Warning: Class '{cls}' not found in 'classes' list.")
#             continue
#         cls_id = classes.index(cls)  # 获取对应的类别ID
#         b = (float(box.get('xtl')), float(box.get('xbr')),
#              float(box.get('ytl')), float(box.get('ybr')))
#         bb = convert(size, b)
#         if any(coord < 0 or coord > 1 for coord in bb):
#             print(f"Warning: Coordinates out of bounds in image {image_id}. Check annotation data.")
#         out_file.write(f"{cls_id} {' '.join(map(str, bb))}\n")
#
# # 获取工作目录
# def get_working_directory():
#     return os.getcwd()
#
# # 主函数
# def main():
#     wd = get_working_directory()
#     print(f"Working Directory: {wd}")
#
#     for image_set in sets:
#         # 创建labels文件夹，如果不存在则创建
#         if not os.path.exists('data/labels/'):
#             os.makedirs('data/labels/')
#
#         # 读取ImageSets/Main 中的train、test、val文件的内容
#         image_ids = open(f'data/ImageSets/{image_set}.txt').read().strip().split()
#         list_file = open(f'data/{image_set}.txt', 'w')
#
#         # 设置图像格式为 .png
#         image_format = '.png'  # 如果是其他格式，可以修改为 .jpg 或 .jpeg
#
#         # 遍历图像ID，进行标注转换
#         for image_id in image_ids:
#             list_file.write(f'data/images/{image_id}{image_format}\n')
#             convert_annotation(image_id, image_format)
#
#         list_file.close()
#
# if __name__ == "__main__":
#     main()



####################################################
####################################################
#一、打印出空白的标签

# import os
# import xml.etree.ElementTree as ET
#
# # 设置数据集的分类
# sets = ['train', 'test', 'val']
# classes = ['三通', '上料系统', '人孔', '仓', '仓壁振动器', '出料口', '变径', '变送器', '吸尘罩', '四通', '圆盘', '圆风管立管托座', '圆风管立管支撑', '垂直拉紧装置', '埋件', '基础', '墙皮', '小便池', '底座', '托座', '振动器', '支座', '料仓', '未知', '柱', '标高', '栏杆', '楼梯', '檩托', '法兰', '法斗', '洗手池', '洞', '混合室', '溜槽', '漏斗', '灭火器', '牛腿节点', '电子秤', '电缆支架', '皮带机', '盲板', '空气炮', '窗', '管道', '给料机', '耐磨件', '胶带机', '节点', '螺栓', '衬板', '蹲厕', '轴网', '进料口', '通廊', '通风器', '通风器支座节点', '配电器', '配管图', '钢板', '钢梯', '钢衬板', '钢链', '门', '阀门', '除尘器', '除尘点', '除铁器', '隔离器']
#
# # 进行归一化操作
# def convert(size, box):
#     dw = 1. / size[0]  # 1/width
#     dh = 1. / size[1]  # 1/height
#     x = (box[0] + box[1]) / 2.0 * dw  # 中心x坐标标准化
#     y = (box[2] + box[3]) / 2.0 * dh  # 中心y坐标标准化
#     w = (box[1] - box[0]) * dw  # 宽度标准化
#     h = (box[3] - box[2]) * dh  # 高度标准化
#     return (x, y, w, h)
#
# # 将CVAT生成的xml文件转化为YOLO的label文件
# def convert_annotation(image_id, image_format):
#     in_file = open(f'data/Annotations/{image_id}.xml', encoding='utf-8')
#     out_file = open(f'data/labels/{image_id}.txt', 'w', encoding='utf-8')
#     tree = ET.parse(in_file)
#     root = tree.getroot()
#     size = (int(root.find('image').get('width')), int(root.find('image').get('height')))
#
#     # 遍历每个box元素
#     for box in root.iter('box'):
#         # 尝试获取box中的attribute "名称"的值
#         attribute = box.find('attribute[@name="名称"]')
#         if attribute is None:
#             print(f"Warning: Attribute '名称' not found in box for image {image_id}.")
#             # 仅在遇到问题时打印当前box结构
#             print("Problematic box structure:")
#             print(ET.tostring(box, encoding='utf-8').decode('utf-8'))
#             continue
#
#         cls = attribute.text
#         if cls not in classes:
#             print(f"Warning: Class '{cls}' not found in 'classes' list for image {image_id}.")
#             # 仅在遇到问题时打印当前box结构
#             print("Problematic box structure:")
#             print(ET.tostring(box, encoding='utf-8').decode('utf-8'))
#             continue
#
#         cls_id = classes.index(cls)
#         b = (float(box.get('xtl')), float(box.get('xbr')),
#              float(box.get('ytl')), float(box.get('ybr')))
#         bb = convert(size, b)
#         if any(coord < 0 or coord > 1 for coord in bb):
#             print(f"Warning: Coordinates out of bounds in image {image_id}. Check annotation data.")
#             continue
#         out_file.write(f"{cls_id} {' '.join(map(str, bb))}\n")
#
# # 获取工作目录
# def get_working_directory():
#     return os.getcwd()
#
# # 主函数
# def main():
#     wd = get_working_directory()
#     print(f"Working Directory: {wd}")
#
#     for image_set in sets:
#         # 创建labels文件夹，如果不存在则创建
#         if not os.path.exists('data/labels/'):
#             os.makedirs('data/labels/')
#
#         # 读取ImageSets/Main 中的train、test、val文件的内容
#         image_ids = open(f'data/ImageSets/{image_set}.txt').read().strip().split()
#         list_file = open(f'data/{image_set}.txt', 'w')
#
#         # 设置图像格式为 .png
#         image_format = '.png'  # 如果是其他格式，可以修改为 .jpg 或 .jpeg
#
#         # 遍历图像ID，进行标注转换
#         for image_id in image_ids:
#             list_file.write(f'data/images/{image_id}{image_format}\n')
#             convert_annotation(image_id, image_format)
#
#         list_file.close()
#
# if __name__ == "__main__":
#     main()



# ####################################################
# ####################################################
# #二、跳过空白标签，不保存到txt的标签文件中
#
# import os
# import xml.etree.ElementTree as ET
#
# # 设置数据集的分类
# sets = ['train', 'test', 'val']
# classes = ['wz-242', 'wz-243', '三通', '上料系统', '人孔', '人孔盖板', '仓', '仓壁振动器', '低压配电室', '储气罐', '出料口', '出灰口', '刮板机', '卸灰插板阀', '卸灰阀', '变压器室', '变径', '变径管', '变送器', '含铁料仓', '吸尘罩', '吸排罐车接头', '四通', '圆环板', '圆环版', '圆盘', '圆风管立管托座', '圆风管立管支撑', '垂直拉紧装置', '埋件', '基础', '墙皮', '小便池', '底座', '截止阀', '扁钢', '托座', '抽风机', '振动器', '接地体', '提手', '插板阀', '支座', '斗提机', '料仓', '料槽', '旋流型屋顶自然通风器', '未知', '机头电除尘器接地系统', '机尾除尘', '机尾除尘低压配电室', '机尾除尘缓冲仓', '机尾除尘高压变频室', '柱', '柱头', '标高', '栏杆', '楼梯', '檩托', '止回阀', '气力输会仓泵', '气力输灰储气罐', '法兰', '法斗', '洗手池', '洞', '洞口', '消防控制室', '消音器', '混合室', '溜槽', '漏斗', '灭火器', '烧结室', '烧结机', '燃料仓', '牛腿节点', '生产辅助用房', '生石灰仓', '电子秤', '电机', '电气备件间', '电缆夹层', '电缆支架', '男更衣室', '白云石仓', '皮带机', '盲板', '石灰石仓', '破碎机', '空气炮', '空调室内机', '空调室外机', '窗', '管道', '管道盲板', '给料机', '耐磨件', '胶带机', '节点', '螺栓', '衬板', '蹲厕', '轴网', '输送机', '边墙排风机', '边墙送风机', '进出口', '进料口', '通廊', '通风器', '通风器支座节点', '配电器', '配管图', '钢板', '钢梯', '钢衬板', '钢链', '门', '阀门', '除尘器', '除尘灰仓', '除尘灰缓冲仓卸灰管', '除尘点', '除尘管', '除尘管道', '除尘设备', '除铁器', '隔离器', '风管支撑']
#
# # 进行归一化操作
# def convert(size, box):
#     dw = 1. / size[0]  # 1/width
#     dh = 1. / size[1]  # 1/height
#     x = (box[0] + box[1]) / 2.0 * dw  # 中心x坐标标准化
#     y = (box[2] + box[3]) / 2.0 * dh  # 中心y坐标标准化
#     w = (box[1] - box[0]) * dw  # 宽度标准化
#     h = (box[3] - box[2]) * dh  # 高度标准化
#     return (x, y, w, h)
#
# # 将CVAT生成的xml文件转化为YOLO的label文件
# def convert_annotation(image_id, image_format):
#     in_file = open(f'data/Annotations/{image_id}.xml', encoding='utf-8')
#     out_file = open(f'data/labels/{image_id}.txt', 'w', encoding='utf-8')
#     tree = ET.parse(in_file)
#     root = tree.getroot()
#     size = (int(root.find('image').get('width')), int(root.find('image').get('height')))
#
#     # 遍历每个box元素
#     for box in root.iter('box'):
#         # 尝试获取box中的attribute "名称"的值
#         attribute = box.find('attribute[@name="名称"]')
#         if attribute is None or not attribute.text:
#             print(f"Warning: Attribute '名称' is missing or empty in box for image {image_id}.")
#             # 仅在遇到问题时打印当前box结构
#             print("Problematic box structure:")
#             print(ET.tostring(box, encoding='utf-8').decode('utf-8'))
#             continue
#
#         cls = attribute.text
#         if cls not in classes:
#             print(f"Warning: Class '{cls}' not found in 'classes' list for image {image_id}.")
#             continue
#                         #####继续跳过空白标签： 当满足上述条件时，代码执行 continue，这意味着程序将跳过这个 box 元素，继续处理下一个标注。
#         cls_id = classes.index(cls)
#         b = (float(box.get('xtl')), float(box.get('xbr')),
#              float(box.get('ytl')), float(box.get('ybr')))
#         bb = convert(size, b)
#         if any(coord < 0 or coord > 1 for coord in bb):
#             print(f"Warning: Coordinates out of bounds in image {image_id}. Check annotation data.")
#             continue
#         out_file.write(f"{cls_id} {' '.join(map(str, bb))}\n")
#
# # 获取工作目录
# def get_working_directory():
#     return os.getcwd()
#
# # 主函数
# def main():
#     wd = get_working_directory()
#     print(f"Working Directory: {wd}")
#
#     for image_set in sets:
#         # 创建labels文件夹，如果不存在则创建
#         if not os.path.exists('data/labels/'):
#             os.makedirs('data/labels/')
#
#         # 读取ImageSets/Main 中的train、test、val文件的内容
#         image_ids = open(f'data/ImageSets/{image_set}.txt').read().strip().split()
#         list_file = open(f'data/{image_set}.txt', 'w')
#
#         # 设置图像格式为 .png
#         image_format = '.png'  # 如果是其他格式，可以修改为 .jpg 或 .jpeg
#
#         # 遍历图像ID，进行标注转换
#         for image_id in image_ids:
#             list_file.write(f'data/images/{image_id}{image_format}\n')
#             convert_annotation(image_id, image_format)
#
#         list_file.close()
#
# if __name__ == "__main__":
#     main()





####################################################
####################################################
#三、过滤掉数量较少的物体




import os
import xml.etree.ElementTree as ET

# 设置数据集的分类
sets = ['train', 'test', 'val']
# classes = ['wz-242', 'wz-243', '三通', '上料系统', '人孔', '人孔盖板', '仓', '仓壁振动器', '低压配电室', '储气罐', '出料口', '出灰口', '刮板机', '卸灰插板阀', '卸灰阀', '变压器室', '变径', '变径管', '变送器', '含铁料仓', '吸尘罩', '吸排罐车接头', '四通', '圆环板', '圆环版', '圆盘', '圆风管立管托座', '圆风管立管支撑', '垂直拉紧装置', '埋件', '基础', '墙皮', '小便池', '底座', '截止阀', '扁钢', '托座', '抽风机', '振动器', '接地体', '提手', '插板阀', '支座', '斗提机', '料仓', '料槽', '旋流型屋顶自然通风器', '未知', '机头电除尘器接地系统', '机尾除尘', '机尾除尘低压配电室', '机尾除尘缓冲仓', '机尾除尘高压变频室', '柱', '柱头', '标高', '栏杆', '楼梯', '檩托', '止回阀', '气力输会仓泵', '气力输灰储气罐', '法兰', '法斗', '洗手池', '洞', '洞口', '消防控制室', '消音器', '混合室', '溜槽', '漏斗', '灭火器', '烧结室', '烧结机', '燃料仓', '牛腿节点', '生产辅助用房', '生石灰仓', '电子秤', '电机', '电气备件间', '电缆夹层', '电缆支架', '男更衣室', '白云石仓', '皮带机', '盲板', '石灰石仓', '破碎机', '空气炮', '空调室内机', '空调室外机', '窗', '管道', '管道盲板', '给料机', '耐磨件', '胶带机', '节点', '螺栓', '衬板', '蹲厕', '轴网', '输送机', '边墙排风机', '边墙送风机', '进出口', '进料口', '通廊', '通风器', '通风器支座节点', '配电器', '配管图', '钢板', '钢梯', '钢衬板', '钢链', '门', '阀门', '除尘器', '除尘灰仓', '除尘灰缓冲仓卸灰管', '除尘点', '除尘管', '除尘管道', '除尘设备', '除铁器', '隔离器', '风管支撑']

#58类，大于50
classes = [
  '三通', '上料系统',  '人孔盖板',  '刮板机',  '卸灰阀', '变径',  '变送器', '吸尘罩',
  '圆风管立管托座', '圆风管立管支撑', '墙皮', '底座', '托座', '抽风机',  '料仓', '旋流型屋顶自然通风器',
  '未知', '机头电除尘器接地系统',  '柱', '柱头', '标高', '楼梯',  '法兰',  '洞',  '混合室', '漏斗', '灭火器',
  '烧结室', '烧结机', '燃料仓', '牛腿节点', '生石灰仓', '电子秤',  '电缆支架',  '皮带机', '石灰石仓',  '空气炮',
  '窗', '管道',  '耐磨件', '胶带机',  '螺栓',  '轴网', '输送机',  '通廊', '通风器',  '配电器', '配管图', '钢板',
  '门',  '除尘器', '除尘灰仓',  '除尘点', '除尘管', '除尘管道', '除尘设备',  '隔离器', '风管支撑'
]


#36类，大于100，删去“未知”
# classes = [
#   '三通', '上料系统',  '人孔盖板',  '刮板机',  '卸灰阀', '变径',  '变送器', '吸尘罩',
#   '圆风管立管托座', '圆风管立管支撑', '墙皮', '底座', '托座', '抽风机',  '料仓', '旋流型屋顶自然通风器',
#   '未知', '机头电除尘器接地系统',  '柱', '柱头', '标高', '楼梯',  '法兰',  '洞',  '混合室', '漏斗', '灭火器',
#   '烧结室', '烧结机', '燃料仓', '牛腿节点', '生石灰仓', '电子秤',  '电缆支架',  '皮带机', '石灰石仓',  '空气炮',
#   '窗', '管道',  '耐磨件', '胶带机',  '螺栓',  '轴网', '输送机',  '通廊', '通风器',  '配电器', '配管图', '钢板',
#   '门',  '除尘器', '除尘灰仓',  '除尘点', '除尘管', '除尘管道', '除尘设备',  '隔离器', '风管支撑'
# ]

# 进行归一化操作
def convert(size, box):
    dw = 1. / size[0]  # 1/width
    dh = 1. / size[1]  # 1/height
    x = (box[0] + box[1]) / 2.0 * dw  # 中心x坐标标准化
    y = (box[2] + box[3]) / 2.0 * dh  # 中心y坐标标准化
    w = (box[1] - box[0]) * dw  # 宽度标准化
    h = (box[3] - box[2]) * dh  # 高度标准化
    return (x, y, w, h)

# 将CVAT生成的xml文件转化为YOLO的label文件
# 将CVAT生成的xml文件转化为YOLO的label文件
def convert_annotation(image_id, image_format, label_counts, filter_threshold):
    in_file = open(f'data/Annotations/{image_id}.xml', encoding='utf-8')
    out_file = open(f'data/labels/{image_id}.txt', 'w', encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = (int(root.find('image').get('width')), int(root.find('image').get('height')))

    # 遍历每个box元素
    for box in root.iter('box'):
        attribute = box.find('attribute[@name="名称"]')
        if attribute is None or not attribute.text:
            print(f"Warning: Attribute '名称' is missing or empty in box for image {image_id}.")
            print("Problematic box structure:")
            print(ET.tostring(box, encoding='utf-8').decode('utf-8'))
            continue

        cls = attribute.text
        if cls not in classes:
            print(f"Warning: Class '{cls}' not found in 'classes' list for image {image_id}.")
            continue

        # 过滤掉出现次数较少的类别
        if cls in label_counts and label_counts[cls] < filter_threshold:
            print(f"Skipping class '{cls}' due to low occurrence in image {image_id}.")
            continue

        cls_id = classes.index(cls)
        b = (float(box.get('xtl')), float(box.get('xbr')),
             float(box.get('ytl')), float(box.get('ybr')))
        bb = convert(size, b)
        if any(coord < 0 or coord > 1 for coord in bb):
            print(f"Warning: Coordinates out of bounds in image {image_id}. Check annotation data.")
            continue
        out_file.write(f"{cls_id} {' '.join(map(str, bb))}\n")


# 获取工作目录
def get_working_directory():
    return os.getcwd()

# 主函数
def main():
    wd = get_working_directory()
    print(f"Working Directory: {wd}")

    # 假设你已经计算好了每种类别的数量
    label_counts = {'变送器': 425, '隔离器': 659, '配电器': 405, '管道': 1332, '轴网': 21088, '门': 694, '标高': 5927, '楼梯': 1034, '皮带机': 337, '胶带机': 473, '烧结机': 285, '管道盲板': 35, '提手': 12, '人孔盖板': 57, '耐磨件': 352, '吸尘罩': 472,
                    '风管支撑': 62, '除尘管': 120, '圆风管立管托座': 120, '柱': 714, '除尘点': 515, '消音器': 40, '螺栓': 396, '洞': 407, '窗': 845, '变径': 147, '除尘器': 161, '钢板': 464, '法兰': 97, '机尾除尘缓冲仓': 9, '机尾除尘': 30, '储气罐': 24,
                    '输送机': 168, '卸灰阀': 80, '三通': 406, '变径管': 6, '止回阀': 12, '截止阀': 9, '插板阀': 12, '未知': 109, '除尘管道': 548, '洞口': 48, '除尘设备': 124, '灭火器': 166, '蹲厕': 8, '小便池': 4, '洗手池': 8, '电机': 21, '破碎机': 24,
                    '料槽': 18, '托座': 57, '盲板': 28, '四通': 48, '圆风管立管支撑': 60, '旋流型屋顶自然通风器': 62, '混合室': 72, '通风器支座节点': 8, '通风器': 93, '机尾除尘低压配电室': 9, '机尾除尘高压变频室': 9, '空调室外机': 24, '底座': 76, '低压配电室': 15,
                    '空调室内机': 22, '生产辅助用房': 32, '消防控制室': 16, '男更衣室': 12, '变压器室': 27, '烧结室': 54, '电气备件间': 12, '通廊': 153, '支座': 9, '电缆夹层': 15, '边墙送风机': 12, '边墙排风机': 24, '钢梯': 31, '溜槽': 40, '除铁器': 48, '漏斗': 70,
                    '阀门': 27, '振动器': 30, '料仓': 807, '除尘灰仓': 54, '配管图': 192, '垂直拉紧装置': 21, '生石灰仓': 102, '法斗': 10, '给料机': 29, '圆盘': 9, '出料口': 31, '电子秤': 80, '进料口': 17, '仓': 38, '仓壁振动器': 12, '人孔': 30, '上料系统': 75,
                    '空气炮': 60, '衬板': 24, '钢衬板': 15, '石灰石仓': 54, '白云石仓': 48, '墙皮': 184, '檩托': 8, '电缆支架': 540, '抽风机': 70, '气力输灰储气罐': 4, '气力输灰仓泵': 4, '斗提机': 30, '刮板机': 247, '燃料仓': 96,
                    '牛腿节点': 86, '栏杆': 44, '钢链': 28, '基础': 18, '节点': 28, '埋件': 24, '出灰口': 6, '进出口': 6, '柱头': 116, '机头电除尘器接地系统': 50, '扁钢': 8, '接地体': 24, '圆环板': 6, '卸灰插板阀': 12, '除尘灰缓冲仓卸灰管': 12,
                    '吸排罐车接头': 32, '含铁料仓': 48, '圆环板': 12
                    }

    filter_threshold = 50  # 设定过滤的阈值

    for image_set in sets:
        if not os.path.exists('data/labels/'):
            os.makedirs('data/labels/')

        image_ids = open(f'data/ImageSets/{image_set}.txt').read().strip().split()
        list_file = open(f'data/{image_set}.txt', 'w')
        image_format = '.png'

        for image_id in image_ids:
            list_file.write(f'data/images/{image_id}{image_format}\n')
            convert_annotation(image_id, image_format, label_counts, filter_threshold)

        list_file.close()


if __name__ == "__main__":
    main()
