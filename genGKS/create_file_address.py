import os 


path = "address/"


files = os.listdir(path)

address = ""
for f in files:
    with open(path + f, "r", encoding='utf-8') as f:
        data = f.read()

    f.close()

    data = data.split('\n')
    data = data[: -1]
    # print(data)

    for d in data:
        d1 = d.split('\t')
        address += d1[0].title() + "\n"
    
    # break

f = open("vocab/address.txt", "w", encoding='utf-8')
f.write(address.replace("\n\n", ""))
f.close()