from abc import ABC, abstractmethod

class Lesson(ABC):
    @abstractmethod
    def start(self): pass

class Video(Lesson):
    def start(self): return "Видеоурок запущен"

class Quiz(Lesson):
    def start(self): return "Квиз открыт"

class Text(Lesson):
    def start(self): return "Текстовый урок открыт"


for l in [Video(), Quiz(), Text()]:
    print(l.start())
