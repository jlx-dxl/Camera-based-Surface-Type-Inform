import os
import random

def generate_image_paths_txt(root_folder, output_txt):
    image_paths = []
    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'bmp')):
                image_paths.append(os.path.join(root, file))
    
    with open(output_txt, 'w') as f:
        for path in image_paths:
            f.write(path + '\n')

def split_txt_file(input_txt, train_txt, val_txt, test_txt, train_ratio=0.7, val_ratio=0.15):
    with open(input_txt, 'r') as f:
        lines = f.readlines()

    random.shuffle(lines)
    
    train_split = int(len(lines) * train_ratio)
    val_split = int(len(lines) * (train_ratio + val_ratio))

    train_lines = lines[:train_split]
    val_lines = lines[train_split:val_split]
    test_lines = lines[val_split:]

    with open(train_txt, 'w') as f:
        f.writelines(train_lines)
    
    with open(val_txt, 'w') as f:
        f.writelines(val_lines)
    
    with open(test_txt, 'w') as f:
        f.writelines(test_lines)

root_folder = 'Data/RawData/Videos202404/Images/'
output_txt = 'all_image_paths.txt'
train_txt = 'train_paths.txt'
val_txt = 'val_paths.txt'
test_txt = 'test_paths.txt'

generate_image_paths_txt(root_folder, output_txt)
split_txt_file(output_txt, train_txt, val_txt, test_txt)
