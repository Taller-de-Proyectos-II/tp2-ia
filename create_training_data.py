import csv

inputs = []
outputs = []

n = 6
for i in range(64):
    b = bin(i)[2:]
    l = len(b)
    b = str(0) * (n - l) + b
    c = [int(s) for s in list(b)]
    inputs.append(c)
    if sum(c) > 3:
        outputs.append([1])
    else:
        outputs.append([0])

with open('training_data_inputs_alert.csv', 'w', newline = '') as File:
    writer = csv.writer(File)
    writer.writerows(inputs)

with open('training_data_outputs_alert.csv', 'w', newline = '') as File:
    writer = csv.writer(File)
    writer.writerows(outputs)