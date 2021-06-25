import os
import os.path
from shutil import copyfile
import numpy as np

def findPNGFiles(folder_src_path):
    files_list = []
    for src_path, _, filenames in os.walk(folder_src_path):
        for filename in [f for f in filenames if f.endswith('.png')]:
            #category + name
            category = src_path.replace(folder_src_path + "\\", "").split("\\")[0]
            files_list.append((filename, category))
    return files_list

src_path = "C:\\Users\\arist\\Desktop\\Final Dataset\\sketch"

files_list = findPNGFiles(src_path)

# # train set with all the categories in it and test set with all human sketches
# train_list = []
# test_list = []
# for name, category in files_list:
#     if int(name.replace(".png","").split("_")[1])>=28:
#         test_list.append((name, category))
#     else:
#         train_list.append((name,category))

# dst_path = "C:\\Users\\arist\\Desktop\\Final Dataset"
# filename = dst_path + "\\" + "train_set_human.npy"
# train_array = np.array(train_list)
# print(len(train_array))
# np.save(open(filename, 'wb'), train_array, allow_pickle=True)

# filename = dst_path + "\\" + "test_set_human.npy"
# test_array = np.array(test_list)
# print(len(test_array))
# np.save(open(filename, 'wb'), test_array, allow_pickle=True)

# train set with unseen categories of human sketches in test set
test_categories = ["animals", "beverage", "computers", "food", "vehicles", "winter"]
train_list = []
test_list = []
for name, category in files_list:
    if int(name.replace(".png","").split("_")[1])>=28 and category in test_categories:
        test_list.append((name, category))
    elif category not in test_categories:
        train_list.append((name,category))

filename = src_path + "\\" + "train_set_human_unseen.npy"
train_array = np.array(train_list)
print(len(train_array))
np.save(open(filename, 'wb'), train_array, allow_pickle=True)

filename = src_path + "\\" + "test_set_human_unseen.npy"
test_array = np.array(test_list)
print(len(test_array))
np.save(open(filename, 'wb'), test_array, allow_pickle=True)