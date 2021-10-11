
import os
import xml.etree.ElementTree as ET
import cv2
import shutil
import time

# path_dir = "data_vn_en_02_van_26/"
file_xml = "data/resumes_en_1_thanh/annotations.xml"
path_txt = "data/resumes_en_1_thanh/txt/"
tree = ET.parse(file_xml)
root = tree.getroot()
list_images = root.findall("image")

# count = 0
for image in list_images:
    #get attrib of image, read image
    attrib = image.attrib
    file_name = attrib["name"]          #file name (labeled)
    id_image = int(attrib["id"])
    # if id_image >= 40:
    #     continue
    print(file_name)
    file_name = file_name.replace('_chars.csv', "")

    width = attrib["width"]
    height = attrib["height"]

    bboxes = image.findall("box")
    results = ""
    for box in bboxes:
        att = box.attrib
        label = att["label"]
        xmin = att["xtl"]
        xmin = int(float(xmin))
        ymin = att["ytl"]
        ymin = int(float(ymin))
        xmax = att["xbr"]
        xmax = int(float(xmax))
        ymax = att["ybr"]
        ymax = int(float(ymax))
        # print(label, xmin, ymin, xmax, ymax)
        results += str(xmin) + '\t' + str(ymin) + '\t' + str(xmax) + '\t' + str(ymax) + '\t' + str(label) + '\n'

    fout = path_txt + file_name[: -3] + "txt"
    # print(fout)
    f = open(fout, "w")
    f.write(results[: -1])
    f.close()

    # break



