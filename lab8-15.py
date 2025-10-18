class Manager:
    def work(self): return "Менеджер организует задачи"

class Dev:
    def work(self): return "Разработчик пишет программы"

class Designer:
    def work(self): return "Дизайнер делает макеты"


for e in [Manager(), Dev(), Designer()]:
    print(e.work())
