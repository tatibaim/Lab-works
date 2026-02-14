import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# Ввод
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# Первая точка
p1 = Point(x1, y1)

# Показываем начальные координаты
p1.show()

# Двигаем точку
p1.move(x2, y2)

# Показываем новые координаты
p1.show()

# Вторая точка
p2 = Point(x3, y3)

# Считаем расстояние
d = p1.dist(p2)

# Вывод с 2 знаками
print(f"{d:.2f}")
