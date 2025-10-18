class Fire:
    def cast(self, tgt): return f"{tgt} обожжён огнём"

class Ice:
    def cast(self, tgt): return f"{tgt} заморожен"

class Heal:
    def cast(self, tgt): return f"{tgt} восстановлен"


for spell in [Fire(), Ice(), Heal()]:
    print(spell.cast("Враг"))
