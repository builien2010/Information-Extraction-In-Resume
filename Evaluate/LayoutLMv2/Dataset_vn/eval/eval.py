

from seqeval.metrics import (
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)

from sklearn.metrics import confusion_matrix

with open("test_ground_true.txt", "r", encoding='utf8') as f :
    data = f.read()
f.close()

ground_truth = []
for d in data.split('\n'):
    if d == "":
        continue
    d1 = d.split()

    for dd in d1:
        if dd == "S-PROJECT_NAME":
            dd = 'O'
        ground_truth.append(dd)

with open("test_predictions.txt", "r", encoding='utf8') as f :
    data1 = f.read()
f.close()

predict = []
for d in data1.split('\n'):
    if d == "":
        continue
    d1 = d.split()
    for dd in d1:
        if dd == "S-PROJECT_NAME":
            dd = 'O'
        predict.append(dd)

# print(ground_truth)
# print(predict)
# print(classification_report(ground_truth, predict))

# for i in range(len(ground_truth)):
#     if ground_truth[i] != predict[i]:
#         print(i)
#         print(ground_truth[i])
#         print(predict[i])

labels = set(ground_truth)
labels2 = set(predict)

print("labels2: ", labels2)
# print(labels)
labels = list(labels)


# confusion_matrix(ground_truth, predict)

print(confusion_matrix(ground_truth, predict, labels=labels))

print(classification_report(ground_truth, predict))


# print(ground_truth)
# print(predict)