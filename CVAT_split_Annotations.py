import xml.etree.ElementTree as ET
import os


def split_annotation(annotation_path, output_dir, tile_size):
    tree = ET.parse(annotation_path)
    root = tree.getroot()

    # 针对 CVAT XML 结构，找到图像的尺寸
    img_tag = root.find('image')
    img_width = int(img_tag.get('width'))
    img_height = int(img_tag.get('height'))
    base_name = os.path.basename(annotation_path).split('.')[0]

    for i in range(0, img_width, tile_size):
        for j in range(0, img_height, tile_size):
            annotation_copy = ET.ElementTree(ET.fromstring(ET.tostring(root)))
            root_copy = annotation_copy.getroot()
            objects_to_remove = []

            # 遍历 CVAT XML 中的 box 标签
            for box in root_copy.findall('.//box'):
                xmin = int(float(box.get('xtl')))
                xmax = int(float(box.get('xbr')))
                ymin = int(float(box.get('ytl')))
                ymax = int(float(box.get('ybr')))

                # 检查边界框是否与当前tile相交
                if xmax <= i or xmin >= i + tile_size or ymax <= j or ymin >= j + tile_size:
                    objects_to_remove.append(box)
                else:
                    # 调整边界框以适应当前的tile
                    if xmin < i: xmin = i
                    if xmax > i + tile_size: xmax = i + tile_size
                    if ymin < j: ymin = j
                    if ymax > j + tile_size: ymax = j + tile_size

                    box.set('xtl', str(xmin - i))
                    box.set('xbr', str(xmax - i))
                    box.set('ytl', str(ymin - j))
                    box.set('ybr', str(ymax - j))

                # 移除不在当前tile内的对象
                for box in objects_to_remove:
                    if box in root_copy:
                        root_copy.remove(box)

            # 如果当前tile中有对象，则保存分割后的标注文件
            if len(root_copy.findall('.//box')) > 0:
                img_tag.set('width', str(min(tile_size, img_width - i)))
                img_tag.set('height', str(min(tile_size, img_height - j)))
                annotation_copy.write(os.path.join(output_dir, f'{base_name}_{i}_{j}.xml'))


def batch_split_annotations(input_dir, output_dir, tile_size):
    os.makedirs(output_dir, exist_ok=True)
    for annotation_file in os.listdir(input_dir):
        if annotation_file.endswith('.xml'):
            annotation_path = os.path.join(input_dir, annotation_file)
            split_annotation(annotation_path, output_dir, tile_size)


input_dir = 'C:\\Users\\lsk12\\Desktop\\8.31-test\\Annotations'
output_dir = 'C:\\Users\\lsk12\\Desktop\\8.31-test\\small_Annotations'
tile_size = 640  # Adjust tile size according to your needs

batch_split_annotations(input_dir, output_dir, tile_size)
