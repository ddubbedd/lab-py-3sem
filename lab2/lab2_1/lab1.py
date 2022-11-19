import datetime
import csv

a = []

# прописать по PEP8 dosctring и typehiting


def write_to_file() -> None:
    with open('dataset.csv', 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            a.append(row)

    for i in range(0, len(a)):
        with open("lab2_1/X.csv", "a", newline="") as file:
            all_data = [a[i][0]]
            writer = csv.writer(file)
            writer.writerow(all_data)

        with open("lab2_1/Y.csv", "a", newline="") as file:
            all_data = a[i][1:]
            writer = csv.writer(file)
            writer.writerow(all_data)
