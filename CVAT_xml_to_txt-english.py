# -*- coding: utf-8 -*-
#三、过滤掉数量较少的物体




import os
import xml.etree.ElementTree as ET

# 设置数据集的分类
sets = ['train', 'test', 'val']
# classes = ['wz-242', 'wz-243', '三通', '上料系统', '人孔', '人孔盖板', '仓', '仓壁振动器', '低压配电室', '储气罐', '出料口', '出灰口', '刮板机', '卸灰插板阀', '卸灰阀', '变压器室', '变径', '变径管', '变送器', '含铁料仓', '吸尘罩', '吸排罐车接头', '四通', '圆环板', '圆环版', '圆盘', '圆风管立管托座', '圆风管立管支撑', '垂直拉紧装置', '埋件', '基础', '墙皮', '小便池', '底座', '截止阀', '扁钢', '托座', '抽风机', '振动器', '接地体', '提手', '插板阀', '支座', '斗提机', '料仓', '料槽', '旋流型屋顶自然通风器', '未知', '机头电除尘器接地系统', '机尾除尘', '机尾除尘低压配电室', '机尾除尘缓冲仓', '机尾除尘高压变频室', '柱', '柱头', '标高', '栏杆', '楼梯', '檩托', '止回阀', '气力输会仓泵', '气力输灰储气罐', '法兰', '法斗', '洗手池', '洞', '洞口', '消防控制室', '消音器', '混合室', '溜槽', '漏斗', '灭火器', '烧结室', '烧结机', '燃料仓', '牛腿节点', '生产辅助用房', '生石灰仓', '电子秤', '电机', '电气备件间', '电缆夹层', '电缆支架', '男更衣室', '白云石仓', '皮带机', '盲板', '石灰石仓', '破碎机', '空气炮', '空调室内机', '空调室外机', '窗', '管道', '管道盲板', '给料机', '耐磨件', '胶带机', '节点', '螺栓', '衬板', '蹲厕', '轴网', '输送机', '边墙排风机', '边墙送风机', '进出口', '进料口', '通廊', '通风器', '通风器支座节点', '配电器', '配管图', '钢板', '钢梯', '钢衬板', '钢链', '门', '阀门', '除尘器', '除尘灰仓', '除尘灰缓冲仓卸灰管', '除尘点', '除尘管', '除尘管道', '除尘设备', '除铁器', '隔离器', '风管支撑']

#58类，大于50
# classes = [
#   '三通', '上料系统',  '人孔盖板',  '刮板机',  '卸灰阀', '变径',  '变送器', '吸尘罩',
#   '圆风管立管托座', '圆风管立管支撑', '墙皮', '底座', '托座', '抽风机',  '料仓', '旋流型屋顶自然通风器',
#   '未知', '机头电除尘器接地系统',  '柱', '柱头', '标高', '楼梯',  '法兰',  '洞',  '混合室', '漏斗', '灭火器',
#   '烧结室', '烧结机', '燃料仓', '牛腿节点', '生石灰仓', '电子秤',  '电缆支架',  '皮带机', '石灰石仓',  '空气炮',
#   '窗', '管道',  '耐磨件', '胶带机',  '螺栓',  '轴网', '输送机',  '通廊', '通风器',  '配电器', '配管图', '钢板',
#   '门',  '除尘器', '除尘灰仓',  '除尘点', '除尘管', '除尘管道', '除尘设备',  '隔离器', '风管支撑'
# ]


#36类，大于100，并删去“未知”
classes = [
  '三通', '刮板机', '变径',  '变送器', '吸尘罩',
  '圆风管立管托座', '墙皮',  '料仓',
  '柱', '柱头', '标高', '楼梯',   '洞',
  '灭火器',
  '烧结机', '生石灰仓', '电缆支架',  '皮带机',
  '窗', '管道',  '耐磨件', '胶带机',  '螺栓',  '轴网', '输送机',  '通廊',  '配电器', '配管图', '钢板',
  '门',  '除尘器', '除尘灰仓',  '除尘点', '除尘管', '除尘设备',  '隔离器',
]


chinese_to_english = {
    '三通': 'Tee',
    '上料系统': 'Feeding_System',
    '人孔盖板': 'Manhole_Cover',
    '刮板机': 'Scraper_Conveyor',
    '卸灰阀': 'Ash_Discharge_Valve',
    '变径': 'Reducer',
    '变送器': 'Transmitter',
    '吸尘罩': 'Dust_Hood',
    '圆风管立管托座': 'Round_Duct_Riser_Bracket',
    '圆风管立管支撑': 'Round_Duct_Riser_Support',
    '墙皮': 'Wall_Skin',
    '底座': 'Base',
    '托座': 'Bracket',
    '抽风机': 'Exhaust_Fan',
    '料仓': 'Silo',
    '旋流型屋顶自然通风器': 'Swirl_Roof_Ventilator',
    '未知': 'Unknown',
    '机头电除尘器接地系统': 'Head_Electrostatic_Precipitator_Grounding_System',
    '柱': 'Column',
    '柱头': 'Column_Head',
    '标高': 'Elevation',
    '楼梯': 'Staircase',
    '法兰': 'Flange',
    '洞': 'Hole',
    '混合室': 'Mixing_Chamber',
    '漏斗': 'Hopper',
    '灭火器': 'Fire_Extinguisher',
    '烧结室': 'Sintering_Room',
    '烧结机': 'Sintering_Machine',
    '燃料仓': 'Fuel_Bin',
    '牛腿节点': 'Corbel_Node',
    '生石灰仓': 'Quicklime_Silo',
    '电子秤': 'Electronic_Scale',
    '电缆支架': 'Cable_Support',
    '皮带机': 'Belt_Conveyor',
    '石灰石仓': 'Limestone_Bin',
    '空气炮': 'Air_Cannon',
    '窗': 'Window',
    '管道': 'Pipeline',
    '耐磨件': 'Wear_Resistant_Part',
    '胶带机': 'Tape_Conveyor',
    '螺栓': 'Bolt',
    '轴网': 'Grid',
    '输送机': 'Conveyor',
    '通廊': 'Corridor',
    '通风器': 'Ventilator',
    '配电器': 'Distributor',
    '配管图': 'Piping_Diagram',
    '钢板': 'Steel_Plate',
    '门': 'Door',
    '除尘器': 'Dust_Collector',
    '除尘灰仓': 'Dust_Ash_Bin',
    '除尘点': 'Dust_Collection_Point',
    '除尘管': 'Dust_Removal_Pipe',
    '除尘管道': 'Dust_Removal_Pipeline',
    '除尘设备': 'Dust_Removal_Equipment',
    '隔离器': 'Isolator',
    '风管支撑': 'Duct_Support'
}

# classes = [
#     'Tee', 'Feeding_System', 'Manhole_Cover', 'Scraper_Conveyor', 'Ash_Discharge_Valve',
#     'Reducer', 'Transmitter', 'Dust_Hood', 'Round_Duct_Riser_Bracket', 'Round_Duct_Riser_Support',
#     'Wall_Skin', 'Base', 'Bracket', 'Exhaust_Fan', 'Silo', 'Swirl_Roof_Ventilator',
#     'Unknown', 'Head_Electrostatic_Precipitator_Grounding_System', 'Column', 'Column_Head',
#     'Elevation', 'Staircase', 'Flange', 'Hole', 'Mixing_Chamber', 'Hopper', 'Fire_Extinguisher',
#     'Sintering_Room', 'Sintering_Machine', 'Fuel_Bin', 'Corbel_Node', 'Quicklime_Silo',
#     'Electronic_Scale', 'Cable_Support', 'Belt_Conveyor', 'Limestone_Bin', 'Air_Cannon',
#     'Window', 'Pipeline', 'Wear_Resistant_Part', 'Tape_Conveyor', 'Bolt', 'Grid',
#     'Conveyor', 'Corridor', 'Ventilator', 'Distributor', 'Piping_Diagram', 'Steel_Plate',
#     'Door', 'Dust_Collector', 'Dust_Ash_Bin', 'Dust_Collection_Point', 'Dust_Removal_Pipe',
#     'Dust_Removal_Pipeline', 'Dust_Removal_Equipment', 'Isolator', 'Duct_Support'
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
# def convert_annotation(image_id, image_format, label_counts, filter_threshold):
#     in_file = open(f'data/Annotations/{image_id}.xml', encoding='utf-8')
#     out_file = open(f'data/labels/{image_id}.txt', 'w', encoding='utf-8')
#     tree = ET.parse(in_file)
#     root = tree.getroot()
#     size = (int(root.find('image').get('width')), int(root.find('image').get('height')))
#
#     # 遍历每个box元素
#     for box in root.iter('box'):
#         attribute = box.find('attribute[@name="名称"]')
#         if attribute is None or not attribute.text:
#             print(f"Warning: Attribute '名称' is missing or empty in box for image {image_id}.")
#             print("Problematic box structure:")
#             print(ET.tostring(box, encoding='utf-8').decode('utf-8'))
#             continue
#
#         cls = attribute.text
#         if cls not in classes:
#             print(f"Warning: Class '{cls}' not found in 'classes' list for image {image_id}.")
#             continue
#
#         # 过滤掉出现次数较少的类别
#         if cls in label_counts and label_counts[cls] < filter_threshold:
#             print(f"Skipping class '{cls}' due to low occurrence in image {image_id}.")
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
def convert_annotation(image_id, image_format, label_counts, filter_threshold):
    in_file = open(f'data/Annotations/{image_id}.xml', encoding='utf-8')
    out_file = open(f'data/labels/{image_id}.txt', 'w', encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = (int(root.find('image').get('width')), int(root.find('image').get('height')))

    for box in root.iter('box'):
        attribute = box.find('attribute[@name="名称"]')
        if attribute is None or not attribute.text:
            print(f"Warning: Attribute '名称' is missing or empty in box for image {image_id}.")
            continue

        chinese_label = attribute.text
        if chinese_label not in chinese_to_english:
            print(f"Warning: Chinese label '{chinese_label}' has no corresponding English mapping in image {image_id}.")
            continue
        english_label = chinese_to_english[chinese_label]

        # 如果需要对过滤条件也使用英文，可以考虑同时修改 label_counts 或建立对应的映射
        if chinese_label in label_counts and label_counts[chinese_label] < filter_threshold:
            print(f"Skipping class '{chinese_label}' due to low occurrence in image {image_id}.")
            continue

        # 假设你希望输出的是英文的类别索引，则需要一个英文的 classes 列表
        english_classes = [
            'Tee',  'Scraper_Conveyor',  'Reducer', 'Transmitter', 'Dust_Hood',
            'Round_Duct_Riser_Bracket',  'Wall_Skin', 'Silo',
            'Column', 'Column_Head', 'Elevation', 'Staircase', 'Hole',
            'Fire_Extinguisher',
            'Sintering_Machine',
            'Quicklime_Silo',  'Cable_Support', 'Belt_Conveyor',
            'Window', 'Pipeline', 'Wear_Resistant_Part', 'Tape_Conveyor', 'Bolt', 'Grid', 'Conveyor', 'Corridor',
            'Distributor', 'Piping_Diagram', 'Steel_Plate',
            'Door', 'Dust_Collector',  'Dust_Collection_Point', 'Dust_Removal_Pipe', 'Dust_Removal_Pipeline',
            'Dust_Removal_Equipment', 'Isolator'
        ]

        if english_label not in english_classes:
            print(f"Warning: English label '{english_label}' not found in english_classes for image {image_id}.")
            continue
        cls_id = english_classes.index(english_label)

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
    # label_counts = {'变送器': 425, '隔离器': 659, '配电器': 405, '管道': 1332, '轴网': 21088, '门': 694, '标高': 5927, '楼梯': 1034, '皮带机': 337, '胶带机': 473, '烧结机': 285, '管道盲板': 35, '提手': 12, '人孔盖板': 57, '耐磨件': 352, '吸尘罩': 472,
    #                 '风管支撑': 62, '除尘管': 120, '圆风管立管托座': 120, '柱': 714, '除尘点': 515, '消音器': 40, '螺栓': 396, '洞': 407, '窗': 845, '变径': 147, '除尘器': 161, '钢板': 464, '法兰': 97, '机尾除尘缓冲仓': 9, '机尾除尘': 30, '储气罐': 24,
    #                 '输送机': 168, '卸灰阀': 80, '三通': 406, '变径管': 6, '止回阀': 12, '截止阀': 9, '插板阀': 12, '未知': 109, '除尘管道': 548, '洞口': 48, '除尘设备': 124, '灭火器': 166, '蹲厕': 8, '小便池': 4, '洗手池': 8, '电机': 21, '破碎机': 24,
    #                 '料槽': 18, '托座': 57, '盲板': 28, '四通': 48, '圆风管立管支撑': 60, '旋流型屋顶自然通风器': 62, '混合室': 72, '通风器支座节点': 8, '通风器': 93, '机尾除尘低压配电室': 9, '机尾除尘高压变频室': 9, '空调室外机': 24, '底座': 76, '低压配电室': 15,
    #                 '空调室内机': 22, '生产辅助用房': 32, '消防控制室': 16, '男更衣室': 12, '变压器室': 27, '烧结室': 54, '电气备件间': 12, '通廊': 153, '支座': 9, '电缆夹层': 15, '边墙送风机': 12, '边墙排风机': 24, '钢梯': 31, '溜槽': 40, '除铁器': 48, '漏斗': 70,
    #                 '阀门': 27, '振动器': 30, '料仓': 807, '除尘灰仓': 54, '配管图': 192, '垂直拉紧装置': 21, '生石灰仓': 102, '法斗': 10, '给料机': 29, '圆盘': 9, '出料口': 31, '电子秤': 80, '进料口': 17, '仓': 38, '仓壁振动器': 12, '人孔': 30, '上料系统': 75,
    #                 '空气炮': 60, '衬板': 24, '钢衬板': 15, '石灰石仓': 54, '白云石仓': 48, '墙皮': 184, '檩托': 8, '电缆支架': 540, '抽风机': 70, '气力输灰储气罐': 4, '气力输灰仓泵': 4, '斗提机': 30, '刮板机': 247, '燃料仓': 96,
    #                 '牛腿节点': 86, '栏杆': 44, '钢链': 28, '基础': 18, '节点': 28, '埋件': 24, '出灰口': 6, '进出口': 6, '柱头': 116, '机头电除尘器接地系统': 50, '扁钢': 8, '接地体': 24, '圆环板': 6, '卸灰插板阀': 12, '除尘灰缓冲仓卸灰管': 12,
    #                 '吸排罐车接头': 32, '含铁料仓': 48, '圆环板': 12
    #                 }
    label_counts = {
        'Transmitter': 425, 'Isolator': 659, 'Distributor': 405, 'Pipeline': 1332, 'Grid': 21088, 'Door': 694,
        'Elevation': 5927, 'Staircase': 1034, 'Belt_Conveyor': 337, 'Tape_Conveyor': 473, 'Sintering_Machine': 285,
        'Pipeline_Blind_Plate': 35, 'Handle': 12, 'Manhole_Cover': 57, 'Wear_Resistant_Part': 352, 'Dust_Hood': 472,
        'Duct_Support': 62, 'Dust_Removal_Pipe': 120, 'Round_Duct_Riser_Bracket': 120, 'Column': 714,
        'Dust_Collection_Point': 515, 'Muffler': 40, 'Bolt': 396, 'Hole': 407, 'Window': 845, 'Reducer': 147,
        'Dust_Collector': 161, 'Steel_Plate': 464, 'Flange': 97, 'Tail_Dust_Buffer_Bin': 9, 'Tail_Dust_Removal': 30,
        'Air_Tank': 24, 'Conveyor': 168, 'Ash_Discharge_Valve': 80, 'Tee': 406, 'Reducer_Pipe': 6, 'Check_Valve': 12,
        'Globe_Valve': 9, 'Slide_Gate_Valve': 12, 'Unknown': 109, 'Dust_Removal_Pipeline': 548, 'Opening': 48,
        'Dust_Removal_Equipment': 124, 'Fire_Extinguisher': 166, 'Squat_Toilet': 8, 'Urinal': 4, 'Wash_Basin': 8,
        'Motor': 21, 'Crusher': 24, 'Feed_Chute': 18, 'Bracket': 57, 'Blind_Plate': 28, 'Cross': 48,
        'Round_Duct_Riser_Support': 60, 'Swirl_Roof_Ventilator': 62, 'Mixing_Chamber': 72, 'Ventilator_Support_Node': 8,
        'Ventilator': 93, 'Tail_Dust_Removal_LV_Distribution_Room': 9,
        'Tail_Dust_Removal_HV_Frequency_Conversion_Room': 9,
        'AC_Outdoor_Unit': 24, 'Base': 76, 'LV_Distribution_Room': 15, 'AC_Indoor_Unit': 22,
        'Production_Auxiliary_Room': 32, 'Fire_Control_Room': 16, 'Mens_Locker_Room': 12, 'Transformer_Room': 27,
        'Sintering_Room': 54, 'Electrical_Spare_Parts_Room': 12, 'Corridor': 153, 'Support': 9, 'Cable_Mezzanine': 15,
        'Side_Wall_Supply_Fan': 12, 'Side_Wall_Exhaust_Fan': 24, 'Steel_Ladder': 31, 'Chute': 40, 'Iron_Remover': 48,
        'Hopper': 70, 'Valve': 27, 'Vibrator': 30, 'Silo': 807, 'Dust_Ash_Bin': 54, 'Piping_Diagram': 192,
        'Vertical_Tensioning_Device': 21, 'Quicklime_Silo': 102, 'Fa_Dou': 10, 'Feeder': 29, 'Disc': 9,
        'Discharge_Outlet': 31, 'Electronic_Scale': 80, 'Feed_Inlet': 17, 'Bin': 38, 'Bin_Wall_Vibrator': 12,
        'Manhole': 30, 'Feeding_System': 75, 'Air_Cannon': 60, 'Liner_Plate': 24, 'Steel_Liner_Plate': 15,
        'Limestone_Bin': 54, 'Dolomite_Bin': 48, 'Wall_Skin': 184, 'Purlin_Bracket': 8, 'Cable_Support': 540,
        'Exhaust_Fan': 70, 'Pneumatic_Ash_Conveying_Air_Tank': 4, 'Pneumatic_Ash_Conveying_Bin_Pump': 4,
        'Bucket_Elevator': 30, 'Scraper_Conveyor': 247, 'Fuel_Bin': 96, 'Corbel_Node': 86, 'Railing': 44,
        'Steel_Chain': 28, 'Foundation': 18, 'Node': 28, 'Embedded_Part': 24, 'Ash_Discharge_Outlet': 6,
        'Inlet_Outlet': 6, 'Column_Head': 116, 'Head_Electrostatic_Precipitator_Grounding_System': 50,
        'Flat_Steel': 8, 'Grounding_Body': 24, 'Ring_Plate': 6, 'Ash_Discharge_Slide_Gate_Valve': 12,
        'Dust_Ash_Buffer_Bin_Discharge_Pipe': 12, 'Suction_Discharge_Tanker_Connector': 32,
        'Iron_Containing_Material_Bin': 48, 'Ring_Plate_Variant': 12
    }
    # filter_threshold = 50  # 设定过滤的阈值
    filter_threshold = 100  # 设定过滤的阈值

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
