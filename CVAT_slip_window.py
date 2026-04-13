import os
import xml.etree.ElementTree as ET
import cv2

# 滑动窗口生成器
def sliding_window(image, step_size, window_size):
    for y in range(0, image.shape[0] - window_size[1] + 1, step_size):
        for x in range(0, image.shape[1] - window_size[0] + 1, step_size):
            yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])

# 调整边界框以适应当前窗口
def adjust_bounding_box(x_offset, y_offset, box, window_size):
    xmin = max(0, box[0] - x_offset)
    xmax = min(box[1] - x_offset, window_size[0])
    ymin = max(0, box[2] - y_offset)
    ymax = min(box[3] - y_offset, window_size[1])

    if xmin >= xmax or ymin >= ymax:
        return None  # 如果物体的部分完全不在窗口内，则忽略

    return (xmin, xmax, ymin, ymax)

# 处理标注文件，调整边界框并生成对应的小XML文件
def process_annotation(annotation_path, x_offset, y_offset, window_size, output_xml_path):
    tree = ET.parse(annotation_path)
    root = tree.getroot()

    image_node = root.find('image')
    image_width = int(image_node.get('width'))
    image_height = int(image_node.get('height'))

    # 创建新的XML结构
    annotation = ET.Element('annotations')
    meta = ET.SubElement(annotation, 'meta')
    task = ET.SubElement(meta, 'task')
    ET.SubElement(task, 'width').text = str(window_size[0])
    ET.SubElement(task, 'height').text = str(window_size[1])

    image_element = ET.SubElement(annotation, 'image', {
        'id': image_node.get('id'),
        'name': image_node.get('name'),
        'width': str(window_size[0]),
        'height': str(window_size[1])
    })

    for box in image_node.findall('box'):
        # 获取边界框坐标
        xtl = float(box.get('xtl'))
        xbr = float(box.get('xbr'))
        ytl = float(box.get('ytl'))
        ybr = float(box.get('ybr'))

        adjusted_box = adjust_bounding_box(x_offset, y_offset, (xtl, xbr, ytl, ybr), window_size)

        if adjusted_box:
            xtl_adj, xbr_adj, ytl_adj, ybr_adj = adjusted_box
            box_element = ET.SubElement(image_element, 'box', {
                'label': box.get('label'),
                'occluded': box.get('occluded', '0'),
                'source': box.get('source', 'manual'),
                'xtl': str(xtl_adj),
                'ytl': str(ytl_adj),
                'xbr': str(xbr_adj),
                'ybr': str(ybr_adj),
            })
            for attribute in box.findall('attribute'):
                attribute_element = ET.SubElement(box_element, 'attribute', {
                    'name': attribute.get('name')
                })
                attribute_element.text = attribute.text

    # 将新的标注文件保存为小XML文件
    tree = ET.ElementTree(annotation)
    tree.write(output_xml_path, encoding='utf-8')

# 保存窗口图像
def save_window(image, output_image_dir, base_name, x, y, window_num):
    output_image_path = os.path.join(output_image_dir, f"{base_name}_{x}_{y}_{window_num}.png")
    cv2.imwrite(output_image_path, image)

# 主滑动窗口处理函数
def sliding_window_processing(image_dir, annotation_dir, output_image_dir, output_annotation_dir, window_size=(640, 640), step_size=320):
    os.makedirs(output_image_dir, exist_ok=True)
    os.makedirs(output_annotation_dir, exist_ok=True)

    for image_file in os.listdir(image_dir):
        if image_file.endswith('.png') or image_file.endswith('.jpg'):
            image_path = os.path.join(image_dir, image_file)
            base_name = os.path.splitext(image_file)[0]
            annotation_file = f"{base_name}.xml"
            annotation_path = os.path.join(annotation_dir, annotation_file)

            if not os.path.exists(annotation_path):
                print(f"Warning: Annotation file '{annotation_path}' not found. Skipping.")
                continue  # 如果标注文件不存在，跳过这个文件

            # 读取图像
            image = cv2.imread(image_path)
            window_num = 0

            # 滑动窗口遍历图像
            for (x, y, window) in sliding_window(image, step_size, window_size):
                if window.shape[0] != window_size[1] or window.shape[1] != window_size[0]:
                    continue  # 如果窗口大小不符合，跳过

                # 保存滑动窗口图像
                save_window(window, output_image_dir, base_name, x, y, window_num)

                # 生成新的XML文件
                output_xml_path = os.path.join(output_annotation_dir, f"{base_name}_{x}_{y}_{window_num}.xml")
                process_annotation(annotation_path, x, y, window_size, output_xml_path)

                window_num += 1

# 参数和文件夹路径
image_dir = 'data/images'  # 原始图片文件夹
annotation_dir = 'data/Annotations'  # 原始标注文件夹
output_image_dir = 'data/images2'  # 输出小图文件夹
output_annotation_dir = 'data/Annotations2'  # 输出标注文件夹
window_size = (640, 640)  # 滑动窗口大小
step_size = 320  # 滑动步长

# 执行滑动窗口处理
sliding_window_processing(image_dir, annotation_dir, output_image_dir, output_annotation_dir, window_size, step_size)
