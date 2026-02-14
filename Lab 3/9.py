import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Ввод
r = int(input())

# Создание объекта
c = Circle(r)

# Вычисление площади
area = c.area()

# Вывод с 2 знаками
print(f"{area:.2f}")
