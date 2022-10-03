import datetime
import csv

a = []
with open('2_1/original.csv', 'r', newline='') as csvfile:
    file_reader = csv.reader(csvfile)
    for row in file_reader:
        a.append(row)
    print(a)

for i in range(0, len(a)):
    with open("2_1/X.csv", "a", newline="") as file:
        all_data = [a[i][0]]
        writer = csv.writer(file)
        writer.writerow(all_data)

    with open("2_1/Y.csv", "a", newline="") as file:
        all_data = a[i][1:]
        writer = csv.writer(file)
        writer.writerow(all_data)