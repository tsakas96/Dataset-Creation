import os
import os.path
from shutil import copyfile

def findPNGFiles(folder_src_path):
    files_list = []
    file_partial_paths = []
    for src_path, _, filenames in os.walk(folder_src_path):
        for filename in [f for f in filenames if f.endswith('.png')]:
            files_list.append(src_path + "\\" + filename)
            #category + name
            file_partial_paths.append(src_path.replace(folder_src_path + "\\", "") + "\\" + filename)
    return files_list, file_partial_paths


src_path = "C:\\Users\\arist\\Desktop\\sketch"
dst_path = "C:\\Users\\arist\\Desktop\\Final Dataset\\sketch"

files_list, file_partial_paths = findPNGFiles(src_path)

partial_paths_dic = {}
for partial_path in file_partial_paths:
    name = partial_path.split("\\")[2]
    partial_paths_dic.setdefault(name, [])

for partial_path in file_partial_paths:
    name = partial_path.split("\\")[2]
    partial_paths_dic[name].append(partial_path)

for file_path_list in partial_paths_dic.values():
    index = 28
    for file_partial_path in file_path_list:
        src_file = src_path + "\\" + file_partial_path
        data = file_partial_path.split("\\")
        category = data[1]
        name = data[2].replace(".png", "_" + str(index) + ".png")
        dst_file = dst_path + "\\" + category + "\\" + name
        index = index + 1
        copyfile(src_file, dst_file)