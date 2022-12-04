import datetime
import csv

a = []


def split_into_files() -> None:
    """Эта функция разбивает исходный файл на два файла"""
    with open('/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_1/dataset.csv', 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            a.append(row)

    for i in range(0, len(a)):
        with open("/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_1/X.csv", "a", newline="") as file:
            all_data = [a[i][0]]
            writer = csv.writer(file)
            writer.writerow(all_data)

        with open("/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_1/Y.csv", "a", newline="") as file:
            all_data = a[i][1:]
            writer = csv.writer(file)
            writer.writerow(all_data)
