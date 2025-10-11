class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

class Mammal(Animal):
    def __init__(self, name, species, age, fur_type):
        super().__init__(name, species, age)
        self.fur_type = fur_type
    def make_sound(self):
        return f"{self.name} мияукает!"
    def give_birth(self):
        return f"{self.name} рожает котят!"

class Reptile(Animal):
    def __init__(self, name, species, age, scale_type):
        super().__init__(name, species, age)
        self.scale_type = scale_type
    def hiss(self):
        return f"{self.name} щипит!"
    def lay_eggs(self):
        return f"{self.name} откладывает яйца!"

cat = Mammal("мурка", "Кошка", 3,"пушистая")
lizard = Reptile("аллигатр", "ящерица", 2, "быстрый")

print(cat.make_sound(), cat.give_birth())
print(lizard.hiss(), lizard.lay_eggs())