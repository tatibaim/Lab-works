class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Ввод
l, w = map(int, input().split())

# Создаем объект
rect = Rectangle(l, w)

# Вывод
print(rect.area())

'''
тоже самое что и предыдущая задача, надо по идеи делать это классами
'''