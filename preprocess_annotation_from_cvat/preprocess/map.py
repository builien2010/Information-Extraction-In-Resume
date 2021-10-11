import os 

# file_name = "a1.pdf-1.txt"
path_dir = "data/resumes_en_1_thanh/"
path1 = path_dir + "txt_en/"
path2 = path_dir + "txt/"


def map(file_name):
    print("path: ", path1 + file_name)
    if not os.path.exists(path1 + file_name):
        print(1)
        print(file_name)
        return None

    f1 = open(path1 + file_name, "r", encoding='utf-8')
    data1 = f1.read()
    # print(data1)

    f2 = open(path2 + file_name, "r", encoding='utf-8')
    data2 = f2.read()
    # print(data2)

    dt1 = data1.split('\n')
    dt2 = data2.split('\n')
    results = ""
    l1 = len(dt1)
    l2 = 0
    if l1 == 0 or l1 == 1:
        return None
    for d1 in dt1:

        dd1 = d1.split('\t')
        # print(len(dt1))
        xmin1 = int(dd1[0])
        ymin1 = int(dd1[1])
        xmax1 = int(dd1[2])
        ymax1 = int(dd1[3])
        size = dd1[5]
        # font = dd1[6]

        for d2 in  dt2:

            dd2 = d2.split('\t')
            xmin2 = int(dd2[0])
            ymin2 = int(dd2[1])
            xmax2 = int(dd2[2])
            ymax2 = int(dd2[3])

            # print(xmin1, ymin1, xmax1, xmax2)
            # print()

            # if xmin1 == xmin2 and (ymin1 <= ymin2 - 3 or ymin1 >= ymin2 - 3) and xmax1 == xmax2 and ymax1 == ymax2:
            #     dd1[-1]  = dd2[4]
            #     results += str(xmin1) + '\t' + str(ymin1) + '\t' + str(xmax1) + '\t' + str(ymax1) + '\t' + dd1[4] + '\t' + dd2[4] + '\n'
            
            # if (xmin2 - 5 <= xmin1 <= xmin2 + 5) and (ymin2 - 5 <= ymin1 <= ymin2 + 5) and (xmax2 - 5 <= xmax1 <= xmax2 + 5) and (ymax2 - 5 <= ymax1 <= ymax2 + 5):
            #     dd1[-1]  = dd2[4]
            #     results += str(xmin1) + '\t' + str(ymin1) + '\t' + str(xmax1) + '\t' + str(ymax1) + '\t' + dd1[4] + '\t' + dd2[4] + '\n'
            #     l2 += 1
            #     break
            if (xmin2 - 10 <= xmin1 <= xmin2 + 10) and (ymin2 - 10 <= ymin1 <= ymin2 + 10) and (xmax2 - 10 <= xmax1 <= xmax2 + 10) and (ymax2 - 10 <= ymax1 <= ymax2 + 10):
                dd1[-1]  = dd2[4]
                results += str(xmin1) + '\t' + str(ymin1) + '\t' + str(xmax1) + '\t' + str(ymax1) + '\t' + dd1[4] + '\t' + dd2[4] +  '\t' + size + '\n'
                l2 += 1
                break

    if l1 != l2:
        print(file_name) 
        print(l1)
        print(l2)
        print()
    # print(results)
    fout = 'data/resumes_en_1_thanh/txt_font_sau_map/' + file_name
    f = open(fout, "w", encoding='utf-8')
    f.write(results[: -1])
    f.close()


files = os.listdir(path2)

for f in files:
    # print(f)
    map(f)






