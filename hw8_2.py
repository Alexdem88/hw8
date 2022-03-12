# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя
# программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class NullDevision:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def null_divide(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Делить на ноль нельзя")


x = NullDevision(10, 143)
print(NullDevision.null_divide(650, 0))
print(NullDevision.null_divide(166, 0.1))
print(x.null_divide(634, 0))