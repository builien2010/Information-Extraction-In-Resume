
# chia thành 2 tập dữ liệu train và test

import os 
import shutil

path_train_source = "data1/training_data/"
path_test_source = "data1/testing_data/"

files_train = os.listdir(path_train_source + "annotations/")
files_test = os.listdir(path_test_source + "annotations/")

path_source = "dataset_tong_hop/"
path_des = "dataset_final/"


for f in files_train:


    file_name = f[: -5]
    # print(file_name)

    source_img = path_source + "images/" + file_name + ".jpg" 
    destination_img = path_des + "training_data/images/"
    if not os.path.exists(source_img):
        print(file_name)
        continue
    dest_img = shutil.copy(source_img, destination_img)

    source_json = path_source + "annotations/" + f
    destination_json = path_des + "training_data/annotations/"
    dest_json = shutil.copy(source_json, destination_json)

    # break

# for f in files_test:


#     file_name = f[: -4]
#     print(file_name)

#     source_img = path_source + "images/" + f 
#     destination_img = path_des + "testing_data/images/"
#     if not os.path.exists(source_img):
#         continue
#     dest_img = shutil.copy(source_img, destination_img)

#     source_json = path_source + "annotations/" + file_name + ".json"
#     destination_json = path_des + "testing_data/annotations/"
#     dest_json = shutil.copy(source_json, destination_json)


