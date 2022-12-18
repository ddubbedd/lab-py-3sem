from bs4 import BeautifulSoup

import requests
import csv

a = []


def find_date(iterator: int) -> str:
    """Эта функция возвращает название файла с датой от первого до последнего числа недели"""
    first_day = int(a[iterator][0].split('-')[2])
    date = ''
    for i in range(iterator, len(a)):
        if int(a[i][0].split('-')[2]) > first_day + 6 and int(a[i][0].split('-')[2]) > first_day:
            break
        date = a[iterator][0].replace('-', '') + "_" + a[i][0].replace('-', '')
    return date


def write_to_file(filename='/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab1') -> None:
    """Эта функция записывает данные в файлы, упорядоченные по неделям"""
    with open(filename+'/dataset.csv', 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            a.append(row)
    first_day = int(a[0][0].split('-')[1])
    first_year = int(a[0][0].split('-')[0])
    first_month = int(a[0][0].split('-')[2])

    file_name = find_date(0)

    for i in range(0, len(a)):
        year = int(a[i][0].split('-')[0])
        month = int(a[i][0].split('-')[1])
        day = int(a[i][0].split('-')[2])
        if day > (first_day + 6):
            first_day = int(a[i][0].split('-')[2])
            file_name = find_date(i)
        elif month > first_month:
            first_month = int(a[i][0].split('-')[1])
            first_day = 1
            file_name = find_date(i)
        elif year > first_year:
            first_year = int(a[i][0].split('-')[0])
            first_month = 1
            file_name = find_date(i)
        with open(f"/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab3/datasetWeek/{file_name}.csv", "a", newline="") as file:
            all_data = a[i]
            writer = csv.writer(file)
            writer.writerow(all_data)
