# '''
# 方法一：保存原文件名
# '''
# import os
# from pdf2image import convert_from_path
# from PIL import Image
#
# def convert_pdf_to_images(input_folder, output_folder, output_format='jpeg', dpi=300):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     for filename in os.listdir(input_folder):
#         if filename.endswith('.pdf'):
#             pdf_path = os.path.join(input_folder, filename)
#             images = convert_from_path(pdf_path, dpi=dpi)
#
#             for i, image in enumerate(images):
#                 output_file_format = 'JPEG' if output_format.lower() == 'jpg' else output_format.upper()
#                 output_path = os.path.join(
#                     output_folder, f"{os.path.splitext(filename)[0]}_page_{i + 1}.{output_format.lower()}"
#                 )
#                 image.save(output_path, output_file_format)
#                 print(f"Saved {output_path}")
#
# # 使用示例
# input_folder = 'C:\\Users\\lsk12\\Desktop\\PPP1\\PP1'  # 输入文件夹路径
# output_folder = 'C:\\Users\\lsk12\\Desktop\\PPP1\\PP2'  # 输出文件夹路径
# output_format = 'jpg'  # 你可以选择 'jpg' 或 'png'
# dpi = 300  # 设置DPI
#
# convert_pdf_to_images(input_folder, output_folder, output_format, dpi)





'''
方法二：按照顺序P1,P2,P3,...命名图片
'''
import os
from pdf2image import convert_from_path
from PIL import Image

Image.MAX_IMAGE_PIXELS = 1000000000
def convert_pdf_to_images(input_folder, output_folder, output_format='png', dpi=300):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_count = 1  # 全局计数器

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            images = convert_from_path(pdf_path, dpi=dpi)

            for i, image in enumerate(images):
                output_file_format = 'PNG' if output_format.lower() == 'png' else output_format.upper()
                output_path = os.path.join(
                    output_folder, f"P{image_count}.{output_format.lower()}"
                )
                image.save(output_path, output_file_format)
                print(f"Saved {output_path}")
                image_count += 1  # 更新计数器

# 使用示例
input_folder = 'C:\\Users\\lsk12\\Desktop\\pdf图片'  # 输入文件夹路径
output_folder = 'C:\\Users\\lsk12\\Desktop\\pdf转图片'  # 输出文件夹路径
output_format = 'png'  # 你可以选择 'jpg' 或 'png'
dpi = 300  # 设置DPI

convert_pdf_to_images(input_folder, output_folder, output_format, dpi)
