#对标注好的大图的annotation文件进行分割

import xml.etree.ElementTree as ET
import os


def split_annotation(annotation_path, output_dir, tile_size):
    tree = ET.parse(annotation_path)
    root = tree.getroot()
    size = root.find('size')
    img_width = int(size.find('width').text)
    img_height = int(size.find('height').text)
    base_name = os.path.basename(annotation_path).split('.')[0]

    for i in range(0, img_width, tile_size):
        for j in range(0, img_height, tile_size):
            annotation_copy = ET.ElementTree(ET.fromstring(ET.tostring(root)))
            root_copy = annotation_copy.getroot()
            objects_to_remove = []

            for obj in root_copy.findall('object'):
                xmlbox = obj.find('bndbox')
                xmin = int(xmlbox.find('xmin').text)
                xmax = int(xmlbox.find('xmax').text)
                ymin = int(xmlbox.find('ymin').text)
                ymax = int(xmlbox.find('ymax').text)

                if xmax <= i or xmin >= i + tile_size or ymax <= j or ymin >= j + tile_size:
                    objects_to_remove.append(obj)
                else:
                    if xmin < i: xmin = i
                    if xmax > i + tile_size: xmax = i + tile_size
                    if ymin < j: ymin = j
                    if ymax > j + tile_size: ymax = j + tile_size

                    xmlbox.find('xmin').text = str(xmin - i)
                    xmlbox.find('xmax').text = str(xmax - i)
                    xmlbox.find('ymin').text = str(ymin - j)
                    xmlbox.find('ymax').text = str(ymax - j)

            for obj in objects_to_remove:
                root_copy.remove(obj)

            size.find('width').text = str(tile_size)
            size.find('height').text = str(tile_size)

            annotation_copy.write(os.path.join(output_dir, f'{base_name}_{i}_{j}.xml'))


def batch_split_annotations(input_dir, output_dir, tile_size):
    os.makedirs(output_dir, exist_ok=True)
    for annotation_file in os.listdir(input_dir):
        if annotation_file.endswith('.xml'):
            annotation_path = os.path.join(input_dir, annotation_file)
            split_annotation(annotation_path, output_dir, tile_size)


input_dir = 'C:\\Users\\lsk12\\Desktop\\8-5整图标注\\整图标注\\Annotations'
output_dir = 'C:\\Users\\lsk12\\Desktop\\8-5整图标注\\整图标注\\smallAnnotations'
tile_size = 640  # Adjust tile size according to your needs

batch_split_annotations(input_dir, output_dir, tile_size)
