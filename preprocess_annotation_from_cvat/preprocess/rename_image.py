import os

# path = 'data/images/'
path = 'data_vn_en_01_thanh/images/'

files = os.listdir(path)

files = sorted(files)

# print(files)

for i in range(0, len(files)):
    img = files[i]
    src = path + img
    des = path + img.replace("_chars.csv", "")
    os.rename(src, des)
