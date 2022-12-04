import datetime
import csv

a = []


def find_date(year: str) -> str:
    """Эта функция возвращает название файла с датой от первого до последнего числа"""
    b = []
    max_date = 0
    min_date = 10 ** 10
    for i in range(0, len(a)):
        if int(a[i][0].split("-")[0]) == int(year):
            b.append(a[i][0].split("-"))
            b[-1][1], b[-1][2] = b[-1][2], b[-1][1]

    for i in range(0, len(b)):
        b[i] = int(''.join(b[i]))
        if b[i] > max_date:
            max_date = b[i]
        if b[i] < min_date:
            min_date = b[i]
    return str(min_date) + '_' + str(max_date)


def write_to_file() -> None:
    """Эта функция записывает данные в файлы, упорядоченные по годам"""
    with open('/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_2/dataset.csv', 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            a.append(row)
    for i in range(0, len(a)):
        year = a[i][0].split("-")[0]
        with open(f"/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_2/dataset/{find_date(year)}.csv", "a", newline="") as file:
            all_data = a[i]
            writer = csv.writer(file)
            writer.writerow(all_data)
