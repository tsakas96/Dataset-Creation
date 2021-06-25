import os
import os.path
from shutil import copyfile

def create_directory(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

def findPNGFiles(folder_src_path):
    files_list = []
    file_names_categories = set()
    for src_path, _, filenames in os.walk(folder_src_path):
        for filename in [f for f in filenames if f.endswith('.png')]:
            files_list.append(src_path + "\\" + filename)
            #category + name
            category = src_path.replace(folder_src_path + "\\", "")
            name = filename.split("_")[0]
            file_names_categories.add((name, category))
    return files_list, file_names_categories

src_path = "C:\\Users\\arist\\Desktop\\Dataset2\\Augmentations\\sketches"
files_list, file_names_categories = findPNGFiles(src_path)

dst_path = "C:\\Users\\arist\\Desktop\\Dataset2\\Augmentations\\sketches1"
create_directory(dst_path)
for name, category in file_names_categories:
    count = 1
    for path in files_list:
        category_name = path.replace(src_path + "\\", "")
        file_name = category_name.split("\\")[1].replace(".png","").split("_")[0]
        if file_name == name:
            create_directory(dst_path + "\\" + category)
            new_name = name + "_" + str(count)
            copyfile(path, dst_path + "\\" + category + "\\" + new_name + ".png")
            count = count + 1