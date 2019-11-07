import csv

with open('inputs.csv', 'rb') as csvfile:
    data = list(csv.reader(csvfile))

for i in data:
    print(i)
