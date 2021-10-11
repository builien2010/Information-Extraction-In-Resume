from sklearn.metrics import confusion_matrix

f = open("Dataset1/test_predictions.txt", "r", encoding="utf-8")

data = f.read()

# print(data)

data1 = data.split("\n")

print(len(data1))

print(data1[0])

