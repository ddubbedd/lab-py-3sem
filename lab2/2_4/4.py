import csv
import datetime

a = []

with open('dataset.csv', 'r', newline='') as csvfile:
    file_reader = csv.reader(csvfile)
    for row in file_reader:
        a.append(row)


def find_data1(date):
    print(date)
    for i in range(0, len(a)):
        print(a[i][0])
        if str(date) == a[i][0]:
            print(a[i][0])
    pass


def find_data2(date):
    pass


def find_data3(date):
    pass


def find_data4(date):
    pass


date = datetime.date(2022, 7, 14)
find_data1(date)
