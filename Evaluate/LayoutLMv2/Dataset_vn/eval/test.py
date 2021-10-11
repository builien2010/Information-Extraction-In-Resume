

f = open("test_image.txt", "r", encoding="utf-8")

data = f.read()

# print(data)

data = data.split("\n")

n = len(data)

for i in range (0, n - 1):
    d = data[i]
    d = d.split("\t")
    # print(d)
    # break
    if len(d) == 0 or len(d) == 1:
        continue
    # print(d)

    d1 = d[1].split()
    d2 = d[2].split()


    xmin, ymin, xmax, ymax = int(d1[0]), int(d1[1]), int(d1[2]), int(d1[3])

    width, height = int(d2[0]), int(d2[1])

    image_name = d[-1]

    if xmax > width or ymax > height or xmax < xmin or ymax < ymin:
        print(image_name)



