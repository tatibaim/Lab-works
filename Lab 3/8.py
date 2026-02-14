class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True


# Ввод
balance, amount = map(int, input().split())

# Создаем аккаунт (имя можно любое)
acc = Account("User", balance)

# Пытаемся снять деньги
if acc.withdraw(amount):
    print(acc.balance)
else:
    print("Insufficient Funds")
