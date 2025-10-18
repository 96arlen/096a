class BankAccount:
    def __init__(self, name, account_number, balance, pin):
        self.name = name
        self.__account_number = str(account_number)
        self.__balance = float(balance)
        self.__pin = str(pin)

    def __check_pin(self, pin):
        return str(pin) == self.__pin

    def get_account_number(self, pin):
        return self.__account_number if self.__check_pin(pin) else "Неверный PIN"

    def deposit(self, amount, pin):
        if not self.__check_pin(pin):
            return "Неверный PIN"
        if amount <= 0:
            return "Сумма должна быть положительной"
        self.__balance += amount
        return f"Пополнено на {amount} сом. Баланс: {self.__balance} сом"

    def withdraw(self, amount, pin):
        if not self.__check_pin(pin):
            return "Неверный PIN"
        if amount <= 0:
            return "Сумма должна быть положительной"
        if amount > self.__balance:
            return "Недостаточно средств"
        self.__balance -= amount
        return f"Снято {amount} сом. Баланс: {self.__balance} сом"

    def get_balance(self, pin):
        return f"Баланс: {self.__balance} сом" if self.__check_pin(pin) else "Неверный PIN"



acc = BankAccount("ar096", 215092097, 5000, 5596)
print(acc.name)
print(acc.get_account_number(5596))
print(acc.deposit(600, 5596))
print(acc.withdraw(300, 5596))
print(acc.get_balance(5596))
print(acc.get_balance(9999))  
