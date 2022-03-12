# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b '

    def __add__(self, other):
        print(f'Сумма c1 и c2 равна')
        return f'c = {self.a + other.a} + {self.b + other.b} '

    def __mul__(self, other):
        print(f'Произведение c1 и c2 равно')
        return f'c = {self.a * other.a} + {self.b * other.b} '

    def __sub__(self, other):
        print(f'Вычитание с1 и с2 равно')
        return f'c = {self.a - other.a} - {self.b - other.b} '


    def __str__(self):
        return f'c = {self.a} + {self.b} '


c_1 = ComplexNum(3, 8)
c_2 = ComplexNum(6, 2)
print(c_1)
print(c_2)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)