import os
import os.path
from PIL import Image

def findPNGFiles(folder_src_path):
    files_list = []
    for src_path, _, filenames in os.walk(folder_src_path):
        for filename in [f for f in filenames if f.endswith('.png')]:
            files_list.append(src_path + "\\" + filename)
    return files_list

def findCategoriesAndNames(folder_src_path):
    file_names_categories = set()
    for src_path, _, filenames in os.walk(folder_src_path):
        for filename in [f for f in filenames if f.endswith('.svg')]:
            category = src_path.replace(folder_src_path + "\\", "")
            name = filename.split(".svg")[0]
            file_names_categories.add((name, category))
    return file_names_categories

def create_directory(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

src_path = "C:\\Users\\arist\\Desktop\\Dataset2\\IconsPng"
files_list = findPNGFiles(src_path)

categories_path = "C:\\Users\\arist\\Desktop\\Thesis\\Dataset\\Final Datasets\\Dataset\\icon"
categories_names = findCategoriesAndNames(categories_path)

dst_path = "C:\\Users\\arist\\Desktop\\Thesis\\Dataset\\Final Datasets\\Dataset\\IconsJpg\\"
for name, category in categories_names:
    create_directory(dst_path + category)
    for path in files_list:
        file_name = path.replace(src_path + "\\","").split(".png")[0]
        if file_name == name:
            im = Image.open(path)
            result = Image.new('RGB', (im.width,im.height), color=(255,255,255))
            result.paste(im,im)
            result.save(dst_path + category + "\\" + name + ".jpg")