# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
# с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, d_m_y):

        self.d_m_y = str(d_m_y)

    @classmethod
    def extract(cls, d_m_y):
        my_date = []

        for i in d_m_y.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Ошибки нет'
                else:
                    return f'Ошибка, не правильный год'
            else:
                return f'Ошибка, неправильный месяц'
        else:
            return f'Ошибка, Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.d_m_y)}'


today = Data('12 - 3 - 2022')
print(today)
print(Data.valid(1, 12, 2022))
print(today.valid(3, 3, 2009))
print(Data.extract('8 - 9 - 2017'))
print(today.extract('5 - 12 - 2022'))
print(Data.valid(5, 11, 2011))
