# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники
# на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую
# структуру (например, словарь).

# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.

# Подсказка: постарайтесь реализовать в проекте
# «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class Orgtechnika:

    def __init__(self, name, price, country, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.country = country
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель ': self.name, 'Цена за ед': self.price, 'Количество': self.quantity, 'Страна': self.country }

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity} страна {self.country}'

    # @classmethod
    # @staticmethod
    def reception(self):

        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unit_c = str (input(f'Введите страну '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q, 'Страна': unit_c}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Orgtechnika.reception(self)


class Printer(Orgtechnika):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Orgtechnika):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Orgtechnika):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('Epson', 3999, 15, 10, 'Russia')
unit_2 = Scanner('Canon', 3200, 6, 10, 'Russia')
unit_3 = Copier('Xerox', 4500, 8, 15, 'Chine')
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
