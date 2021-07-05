import random
L=[]
for i in range(20):
    L.append(random.randint(5,30))
print(L)
print(sum(L))

import csv
csv_reader = csv.reader(open("dataset-compliance.csv"))
print(type(csv_reader))
for row in csv_reader:
    1
