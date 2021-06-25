from xml.dom import minidom
import svgpathtools 
from svgpathtools import wsvg, Line, QuadraticBezier, Path, parse_path
import re
import os
import os.path

def findSVGFiles(folder_src_path):
    files_list = []
    file_names = []
    for src_path, src_names, filenames in os.walk(folder_src_path):
        for filename in [f for f in filenames if f.endswith('.svg')]:
            files_list.append(src_path + "\\" + filename)
            #category + name
            file_names.append(filename)
    return files_list, file_names

def findTheDPathsOfSVGs(files_list, file_names):
    name_and_path_list = []
    i = 0
    for svg_file in files_list:
        doc = minidom.parse(svg_file)  # parseString also exists
        path_strings = [path.getAttribute('d') for path
                        in doc.getElementsByTagName('path')]

        viewBox = [path.getAttribute('viewBox') for path
                        in doc.getElementsByTagName('svg')]

        # The svg files have only one path in my case, that is why i am taking
        # only path_strings[0]
        name_and_path_list.append((file_names[i], path_strings[0], viewBox))
        i = i + 1
        doc.unlink()
    return name_and_path_list

def createSVGfileFormat(svg_path, svg_file_name, viewBox):
    headline1 = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="' + str(viewBox[0])+ '" height="256" width="256"><!-- Font Awesome Free 5.15.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) -->'

    with open(svg_file_name, "w+") as f:
        f.write(headline1)

        path = '<path d="' + svg_path + '"/>'
        f.write(path)
        f.write('</svg>')
    f.close()

folder_src_path = "C:\\Users\\arist\\Desktop\\Thesis\\Dataset\\IconsInCategories"
files_list, file_names = findSVGFiles(folder_src_path)
name_and_path_list = findTheDPathsOfSVGs(files_list, file_names)
print(len(name_and_path_list))
dst_path = "C:\\Users\\arist\\Desktop\\ResizedIcons\\"

for name, path, viewBox in name_and_path_list:
    createSVGfileFormat(path, dst_path + name, viewBox)