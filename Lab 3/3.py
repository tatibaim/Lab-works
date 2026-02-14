# Словари преобразования
to_digit = {
    "ZER": "0",
    "ONE": "1",
    "TWO": "2",
    "THR": "3",
    "FOU": "4",
    "FIV": "5",
    "SIX": "6",
    "SEV": "7",
    "EIG": "8",
    "NIN": "9"
}

to_word = {v: k for k, v in to_digit.items()}


# Преобразовать строку в число
def word_to_number(s):
    num = ""

    for i in range(0, len(s), 3):
        part = s[i:i+3]
        num += to_digit[part]

    return int(num)


# Преобразовать число в строку
def number_to_word(n):
    if n == 0:
        return "ZER"

    result = ""

    for d in str(n):
        result += to_word[d]

    return result


# Ввод
expr = input().strip()


# Находим оператор
for op in ["+", "-", "*"]:
    if op in expr:
        left, right = expr.split(op)
        operator = op
        break


# Переводим в числа
a = word_to_number(left)
b = word_to_number(right)


# Считаем
if operator == "+":
    res = a + b
elif operator == "-":
    res = a - b
else:
    res = a * b


# Вывод
print(number_to_word(res))
