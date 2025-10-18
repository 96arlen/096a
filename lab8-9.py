from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amt):
        pass

class Card(PaymentSystem):
    def pay(self, amt):
        return f"{amt} сом списано с карты"

class Crypto(PaymentSystem):
    def pay(self, amt):
        return f"{amt} сом переведено криптой"

class Bank(PaymentSystem):
    def pay(self, amt):
        return f"{amt} сом через банк"



for p in [Card(), Crypto(), Bank()]:
    print(p.pay(1200))
