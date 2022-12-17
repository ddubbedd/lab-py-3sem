import os


class Iterator:

    def __init__(self, name_of_file: str) -> None:
        """Это конструктор объекта класса Iterator"""
        self.name_of_file = name_of_file
        self.counter = 0
        self.list = []
        file = open(self.name_of_file, "r", encoding='utf-8')
        for row in file:
            self.list.append(row)

    def __iter__(self):
        """Этот метод возвращает объект"""
        return self

    def __next__(self) -> int:
        """Этот метод возвращает количество итераций в данный момент"""
        if self.counter < len(self.list):
            tmp = self.list[self.counter]
            self.counter += 1
            return tmp
        else:
            raise StopIteration


def run(path_to_csv: str = os.path.join("/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_3/dataset")) -> None:
    """Эта функция запускает итератор"""
    file_name = path_to_csv + "/20080110_20080116.csv"
    s_iter1 = Iterator(file_name)
    for val in s_iter1:
        print(val, end="")
