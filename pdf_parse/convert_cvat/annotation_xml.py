import os
import json
import glob
from PIL import Image
from pathlib import Path
import cv2
import shutil

with open("meta_info1.txt", "r") as f:
    meta_info = f.read()



def replace_special_text(text):
    text = text.replace('&', '&amp;')
    text = text.replace('>', '&gt;')
    text = text.replace('<', '&lt;')
    text = text.replace('\'', '&apos;')
    text = text.replace('"', '&quot;')
    return text

def add_item(fout, index, image_name, width, height, data_content):
    # fout.write(f'<image id="{index}" name="{image_name}" width="{width}" height="{height}">\n')
    for ij in data_content:
        ij = ij.replace("\n", "")
        if ij.strip() == "":
            continue
        tmp = ij.split("\t")
        xmin, ymin, xmax, ymax = tmp[0:4]
        text = tmp[4]
        label = tmp[5]
        if label == "company":
            label = "company_name"
        elif label == "school":
            label = "school_name"
        elif label == "project":
            label = "project_name"
        text = replace_special_text(text)
        # text = ""
        ymin = max(float(ymin) - 3, 0)
        xmin = str('%.2f' % (float(xmin)))
        ymin = str('%.2f' % (float(ymin)))
        xmax = str('%.2f' % (float(xmax)))
        ymax = str('%.2f' % (float(ymax)))
        # label = "other"
        fout.write(f'\t<box label="{label}" occluded="0" xtl="{xmin}" ytl="{ymin}" xbr="{xmax}" ybr="{ymax}">\n')
        fout.write(f'\t\t<attribute name="text">{text}</attribute>\n')
        fout.write(f'\t\t<attribute name="type">other</attribute>\n')
        fout.write('\t</box>\n')


# pre = "data/"
file_out = 'annotations_vn.xml'
path_images = "images_vn/"
path_txt = "txt_vn/"
fout = open(file_out, 'w', encoding='utf-8')
# copy meta
fout.write(meta_info)

# adding info image
for idx, item in enumerate(sorted(os.listdir(path_images))):
    # print(item)
    prefix = os.path.splitext(item)[0]
    # prefix = prefix.replace("-", "_")
    print("prefix", prefix)
    if not os.path.exists(os.path.join(path_txt, prefix + ".txt")):
        print("not exist path")
        # break
       
        img_path = (Path(path_images)/item).as_posix()
        print(img_path)
        # os.remove(img_path)

        continue
    img_path = (Path(path_images)/item).as_posix()
    # try:
    h, w = Image.open(img_path).size[:2]
    # print(h, w)
    # break
    # except:            
    #     print(img_path)
    #     continue
    fout.write(f'<image id="{idx}" name="{item}" width="{w}" height="{h}">\n')
    with open(os.path.join(path_txt, prefix + ".txt"), 'r', encoding='utf-8') as f:
        cnt = f.readlines()
    h, w = Image.open(img_path).size[:2]
    add_item(fout, idx, item, w, h, cnt)
    fout.write('</image>\n')
fout.write('</annotations>')
fout.close()
print("DONE")

