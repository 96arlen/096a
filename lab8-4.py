class SmartWatch:
    def __init__(self, level=100):
        self.__level = float(level)

    def use(self, mins):
        self.__level = max(0, self.__level - mins / 10)
        return f"Заряд: {self.__level:.1f}%"

    def charge(self, percent):
        self.__level = min(100, self.__level + max(0, percent))
        return f"Заряд: {self.__level:.1f}%"

    def get_level(self):
        return f"Текущий заряд: {self.__level:.1f}%"



watch = SmartWatch()
print(watch.use(30))
print(watch.charge(25))
print(watch.get_level())
