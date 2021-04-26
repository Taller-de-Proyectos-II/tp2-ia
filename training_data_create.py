import csv
from random import seed
from random import randint

inputs = []
outputs = []

seed(1)

for i in range(100):
    row = []
    cont = 0
    for j in range(25):
        if (j == 3) or (j == 4) or (j == 8) or (j == 12) or (j == 10) or (j == 15) or (j == 17) or (j == 21) or (j == 22):
            random = 1
        else:
            random = randint(0, 1)
        row.append(random)
        cont = cont + random
    inputs.append(row)
    if cont > 9:
        outputs.append([1])
    else:
        outputs.append([0])

for i in range(100):
    row = []
    cont = 0
    for j in range(25):
        if (j == 3) or (j == 4) or (j == 8) or (j == 12) or (j == 10) or (j == 15) or (j == 17) or (j == 21) or (j == 22):
            random = 0
        else:
            random = randint(0, 1)
        row.append(random)
        cont = cont + random
    inputs.append(row)
    if cont > 9:
        outputs.append([1])
    else:
        outputs.append([0])

with open('training_data_inputs.csv', 'w', newline = '') as File:
    writer = csv.writer(File)
    writer.writerows(inputs)

with open('training_data_outputs.csv', 'w', newline = '') as File:
    writer = csv.writer(File)
    writer.writerows(outputs)