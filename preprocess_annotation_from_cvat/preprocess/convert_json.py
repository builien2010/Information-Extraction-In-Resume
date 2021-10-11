import cv2
from matplotlib import pyplot as plt
from itertools import product
import json
import os

path_txt = "data_vn_en_02_van_26/annotations/txt_font_sau_map/"
path_json = "data_vn_en_02_van_26/annotations/json_font/"

def txt2json(file_name):

    f = open(path_txt + file_name, "r", encoding="utf-8")
    data = f.read()

    data1 = data.split("\n")

    result = dict()

    data = []
    id = 0
    for d1 in data1:
        d2 = dict()
        d1 = d1.split('\t')
        # print(d1)
        xmin = int(d1[0])
        ymin = int(d1[1])
        xmax = int(d1[2])
        ymax = int(d1[3])
        text = d1[4]
        label = d1[5]
        size = int(d1[6])
        font = int(d1[7])

        d2['box'] = [xmin, ymin, xmax, ymax]
        d2['text'] = text
        d2['label'] = label 
        d2['size'] = size
        d2['font'] = font
        d2['id'] = id 
        d3 = dict()
        d3['box'] = [xmin, ymin, xmax, ymax]
        d3['text'] = text 
        d3['size'] = size
        d3['font'] = font 
        d2['words'] = [d3]
        data.append(d2)
        id += 1
    
    result['form'] = data

    with open(path_json + file_name[:-3] + "json", "w") as outfile: 
        json.dump(result, outfile)

files = os.listdir(path_txt)
for f in files:
    txt2json(f)



