import os
import shutil

def copy_and_rename_images(src_root, dst_folder):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    # Counter for naming the images
    counter = 1

    # Walk through the source directory
    for root, dirs, files in os.walk(src_root):
        for dir_name in dirs:
            if dir_name == '漏斗':
                stair_folder_path = os.path.join(root, dir_name)
                # Get all image files in the "楼梯" folder
                for file_name in os.listdir(stair_folder_path):
                    file_path = os.path.join(stair_folder_path, file_name)
                    if os.path.isfile(file_path):
                        # Get the file extension
                        _, file_extension = os.path.splitext(file_name)
                        # Create the new file name
                        new_file_name = f'LD{counter}{file_extension}'
                        new_file_path = os.path.join(dst_folder, new_file_name)
                        # Copy and rename the image
                        shutil.copy(file_path, new_file_path)
                        counter += 1

# Example usage:
#原文件夹
src_root = 'C:\\Users\\lsk12\\Desktop\\PDF版全图\\6月14位图'

#新文件夹
dst_folder = 'C:\\Users\\lsk12\\Desktop\\YOLO_picture_data\\task04\images2'
copy_and_rename_images(src_root, dst_folder)
