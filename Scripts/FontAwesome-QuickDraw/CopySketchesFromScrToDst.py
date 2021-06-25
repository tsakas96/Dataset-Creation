import os
import os.path
from shutil import copyfile

def findPNGFiles(folder_src_path):
    files_list = []
    for src_path, _, filenames in os.walk(folder_src_path):
        for filename in [f for f in filenames if f.endswith('.png')]:
            files_list.append(src_path + "\\" + filename)
    return files_list


src_path = "C:\\Users\\arist\\Desktop\\sketch"
dst_path = "C:\\Users\\arist\\Desktop\\Final Dataset\\sketch"

files_list = findPNGFiles(src_path)

paths_dic = {}
for file_path in files_list:
    name = file_path.replace(src_path,"").split("\\")[2].split("_")[0]
    paths_dic.setdefault(name, [])

for file_path in files_list:
    name = file_path.replace(src_path,"").split("\\")[2].split("_")[0]
    paths_dic[name].append(file_path)

for file_path_list in paths_dic.values():
    index = 28
    for file_path in file_path_list:
        data =  file_path.replace(src_path,"").split("\\")
        category = data[1]
        name = data[2].split("_")[0] + "_" + str(index) + ".png"
        dst_file = dst_path + "\\" + category + "\\" + name
        index = index + 1
        copyfile(file_path, dst_file)