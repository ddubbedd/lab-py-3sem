import csv
import datetime
import os
from email import generator

list1 = []
list2 = []


def find_data1(date):
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


def find_data2(date):
    with open('dataset2/X.csv', 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            list1.append(row)
    with open('dataset2/Y.csv', 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            list2.append(row)
    b = []
    for i in range(0, len(list1)):
        if str(date) == list1[i][0]:
            b.append(list2[i])
    if not b:
        return None
    else:
        return b


def find_data3(date):
    b = []
    filename = ''
    path = os.listdir(path="dataset3")
    for i in range(len(path)):
        if str(path[i])[0:4] == str(date)[0:4]:
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


def find_data4(date):
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


def next(file_name: str) -> generator:
    path = os.path.join("", file_name)
    names_list = os.listdir(path)
    names_list.append(None)
    my_generator = (item for item in names_list)
    for i in my_generator:
        yield i


def run():
    date = datetime.date(2022, 22, 22)
    find_data1(date)
    find_data2(date)
    find_data3(date)
    find_data4(date)


for i in next("lab2/lab2_4/dataset1/dataset1.csv"):
    print(i)
