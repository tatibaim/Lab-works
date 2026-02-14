class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


# Ввод
n = int(input())

# Создаем объект
sq = Square(n)

# Вывод
print(sq.area())

'''
так как в итоге ответ должен быть квдрат введенного числа и это все делается
в эджадже то можно просто

a=int(input())
print(a*a)
:)
'''