from seqeval.metrics import (
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)

with open("test_font.txt", "r", encoding='utf8') as f :
    data = f.read()
f.close()

ground_truth = []
for d in data.split('\n'):
    if d == "":
        continue
    d1 = d.split()
    ground_truth.append(d1[-1])

with open("test_predictions_font.txt", "r", encoding='utf8') as f :
    data1 = f.read()
f.close()

predict = []
for d in data1.split('\n'):
    if d == "":
        continue
    d1 = d.split()
    predict.append(d1[-1])

# print(ground_truth)
# print(predict)

print(set(ground_truth))
print(classification_report(ground_truth, predict))

# for i in range(len(ground_truth)):
#     if ground_truth[i] != predict[i]:
#         print(i)
#         print(ground_truth[i])
#         print(predict[i])


