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

def findPNGFileNameAndCategory(folder_src_path):
    file_names_categories = set()
    for src_path, _, filenames in os.walk(folder_src_path):
        for filename in [f for f in filenames if f.endswith('.png')]:
            #category + name
            category = src_path.replace(folder_src_path + "\\", "")
            name = filename.split("_")[0]
            file_names_categories.add((name, category))
    return file_names_categories

src_path = "C:\\Users\\arist\\Desktop\\Dataset2\\RenamedSketches"
file_names_categories = findPNGFileNameAndCategory(src_path)

src_icons_path = "C:\\Users\\arist\\Desktop\\Thesis\\Dataset\\IconsInCategories"
dst_path = "C:\\Users\\arist\\Desktop\\Dataset2\\IconsSvg"
create_directory(dst_path)
for name, category in file_names_categories:
    create_directory(dst_path + "\\" + category)
    src_icon = src_icons_path + "\\" + category + "\\" + name + ".svg"
    dst_icon = dst_path + "\\" + category + "\\" + name + ".svg"
    copyfile(src_icon, dst_icon)

