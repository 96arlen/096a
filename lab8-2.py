class Product:
    def __init__(self, title, cost):
        self.title = title
        self.__price = float(cost)

    def apply_discount(self, percent):
        if percent < 0:
            return "Скидка не может быть отрицательной"
        self.__price = max(0, self.__price * (1 - percent / 100))
        return f"Новая цена: {self.__price:.2f} сом"

    def final_price(self):
        return f"Цена: {self.__price:.2f} сом"


p = Product("Смартфон", 20000)
print(p.apply_discount(12))
print(p.final_price())
