import csv
import datetime
import os

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

    for i in range(0, len(list1) - 1):
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
    for i in range(len(all_files) - 1):
        if str(all_files[i])[0:4] == str(date)[0:4]:
            print(all_files[i])

    if all_files:
        for file in all_files:
            if str(date)[0:4] == str(file)[0:4]:
                if str(date)[5:6] == str(file)[5:6]:
                    print(file)
    else:
        return None

    # if filename != '':
    #     with open(f"dataset3/{filename}", 'r', newline='') as csvfile:
    #         file_reader = csv.reader(csvfile)
    #         for row in file_reader:
    #             list1.append(row)
    # else:
    #     return None
    #
    # for i in range(0, len(list1)):
    #     if str(date) == list1[i][0]:
    #         b.append(list1[i][1:])
    # if not b:
    #     return None
    # else:
    #     return b


date = datetime.date(2012, 7, 14)
print(find_data4(date))
