import csv

filename = 'cwurData_4years.csv'

data = []

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)