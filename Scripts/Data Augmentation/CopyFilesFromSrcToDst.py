import os
import os.path
from shutil import copyfile

def findPNGFiles(folder_src_path):
    files_list = []
    file_names = []
    for src_path, _, filenames in os.walk(folder_src_path):
        for filename in [f for f in filenames if f.endswith('.png')]:
            files_list.append(src_path + "\\" + filename)
            #category + name
            file_names.append(src_path.replace(folder_src_path + "\\", "") + "\\" + filename)
    return files_list, file_names


src_path = "C:\\Users\\arist\\Desktop\\Dataset2\\Augmentations\\PiecewiseAffineSketches"
dst_path = "C:\\Users\\arist\\Desktop\\Dataset2\\Augmentations\\sketches"

files_list, file_names = findPNGFiles(src_path)
for i in range(0, len(files_list)):
    src = files_list[i]
    name = file_names[i].replace(".png","") + "_ab.png"
    dst = dst_path + "\\" + name
    copyfile(src, dst)


