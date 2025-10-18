from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self): pass
    @abstractmethod
    def sleep(self): pass

class Lion(Animal):
    def eat(self): return "Лев ест мясо"
    def sleep(self): return "Лев отдыхает на солнце"

class Elephant(Animal):
    def eat(self): return "Слон ест листья"
    def sleep(self): return "Слон спит стоя"

class Snake(Animal):
    def eat(self): return "Змея ест грызунов"
    def sleep(self): return "Змея свернулась и спит"


animals = [Lion(), Elephant(), Snake()]
for a in animals:
    print(a.eat())
    print(a.sleep())
