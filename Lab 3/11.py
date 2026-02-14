class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        return Pair(self.a + other.a, self.b + other.b)


# Ввод
a1, b1, a2, b2 = map(int, input().split())

# Создаем пары
p1 = Pair(a1, b1)
p2 = Pair(a2, b2)

# Складываем
result = p1.add(p2)

# Вывод
print(f"Result: {result.a} {result.b}")
