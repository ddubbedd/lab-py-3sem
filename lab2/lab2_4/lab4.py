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


def find_data1(date: datetime.date) -> Optional[List[str]]:
    list1 = []
    with open('/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab1/dataset.csv', 'r', newline='') as csvfile:
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


def find_data2(date: datetime.date) -> Optional[List[str]]:
    list1 = []
    list2 = []
    with open('/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_1/X.csv', 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            list1.append(row)
    with open('/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_1/Y.csv', 'r', newline='') as csvfile:
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


def find_data3(date: datetime.date) -> Optional[List[str]]:
    list1 = []
    b = []
    filename = ''
    path = os.listdir(path="/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_2/dataset")
    for i in range(len(path)):
        if str(path[i])[0:4] == str(date)[0:4]:
            filename = path[i]

    if filename != '':
        with open(f"/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_2/dataset/{filename}", 'r',
                  newline='') as csvfile:
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


def find_data4(date: datetime.date) -> Optional[List[str]]:
    list1 = []
    b = []
    filename = ''
    all_files = os.listdir(path="/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_3/dataset")

    if all_files:
        for file in all_files:
            if str(date)[0:4] == str(file)[0:4]:
                if str(date)[5:7] == str(file)[4:6]:
                    if int(file[6:8]) <= int(str(date)[8:10]) <= int(file[15:17]):
                        filename = file
                        break

    if filename != '':
        with open(f"/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_3/dataset/{filename}", 'r',
                  newline='') as csvfile:
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


def run_next(path_to_csv: str = os.path.join("/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2")):
    with open(path_to_csv + '/dataset.csv', 'r', encoding='utf-8') as csvfile:
        count = 0
        while count != 50:
            print(*next(path_to_csv, count))
            count += 1


def run(date=datetime.date(2010, 12, 12)) -> None:
    print(find_data1(date))
    print(find_data2(date))
    print(find_data3(date))
    print(find_data4(date))
