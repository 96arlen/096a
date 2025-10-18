class Character:
    def __init__(self, nick, hp, atk):
        self.nick = nick
        self.hp = hp
        self.atk = atk

    def attack(self):
        return f"{self.nick} наносит {self.atk} урона"


class Warrior(Character):
    def attack(self):
        return f"{self.nick} атакует мечом: {self.atk} урона"


class Mage(Character):
    def attack(self):
        return f"{self.nick} колдует: {self.atk} урона"


class Archer(Character):
    def attack(self):
        return f"{self.nick} стреляет: {self.atk} урона"



chars = [Warrior("Артем", 100, 17), Mage("Элина", 80, 22), Archer("Раян", 90, 19)]
for c in chars:
    print(c.attack())



