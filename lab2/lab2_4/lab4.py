import csv
import datetime
import os
from typing import Optional, List


def next(path_to_csv: str, count: int) -> Optional[List[str]]:
    with open(path_to_csv + '/dataset.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        if file_reader[count] is None:
            return None
        else:
            return file_reader[count]


def find_data1(date: datetime.date) -> list:
    list1 = []
    with open('dataset1/dataset1.csv', 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            list1.append(row)
    b = []
    for i in range(0, len(list1)):
        if str(date) == list1[i][0]:
            b.append(list1[i][1:])
    if not b:
        return None
    else:
        return b


def find_data2(date: datetime.date) -> list:
    list1 = []
    list2 = []
    with open('dataset2/X.csv', 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            list1.append(row)
    with open('dataset2/Y.csv', 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            list2.append(row)
    b = []
    for i in range(0, len(list2)):
        if str(date) == list1[i][0]:
            b.append(list2[i])
    if not b:
        return None
    else:
        return b


def find_data3(date: datetime.date) -> list:
    list1 = []
    b = []
    filename = ''
    path = os.listdir(path="dataset3")
    for i in range(len(path)):
        if str(path[i])[0:4] == str(date)[0:4]:
            if str(path[i])[4:6] == str(date)[5:7]:
                if int(str(path[i])[6:8]) <= int(str(date)[8:10]) <= int(str(path[i])[15:17]):
                    filename = path[i]

    if filename != '':
        with open(f"dataset3/{filename}", 'r', newline='') as csvfile:
            file_reader = csv.reader(csvfile)
            for row in file_reader:
                list1.append(row)
    else:
        return None

    for i in range(0, len(list1)):
        if str(date) == list1[i][0]:
            b.append(list1[i][1:])
    if not b:
        return None
    else:
        return b


def find_data4(date: datetime.date):
    list1 = []
    b = []
    filename = ''
    all_files = os.listdir(path="dataset4")

    if all_files:
        for file in all_files:
            if str(date)[0:4] == str(file)[0:4]:
                if str(date)[5:7] == str(file)[4:6]:
                    if int(file[6:8]) <= int(str(date)[8:10]) <= int(file[15:17]):
                        filename = file
                        break

    if filename != '':
        with open(f"dataset4/{filename}", 'r', newline='') as csvfile:
            file_reader = csv.reader(csvfile)
            for row in file_reader:
                list1.append(row)
    else:
        return None

    for i in range(0, len(list1)):
        if str(date) == list1[i][0]:
            b.append(list1[i][1:])
    if not b:
        return None
    else:
        return b


def run(path_to_csv: str = os.path.join("/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2")) -> None:
    date = datetime.date(2010, 12, 12)
    print(find_data1(date))
    print(find_data2(date))
    print(find_data3(date))
    print(find_data4(date))

    with open(path_to_csv + '/dataset.csv', 'r', encoding='utf-8') as csvfile:
        count = 0
        while count != 50:
            print(*next(path_to_csv, count))
            count += 1


run()
