from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self): pass
    @abstractmethod
    def edit(self): pass
    @abstractmethod
    def save(self): pass

class WordDoc(Document):
    def open(self): return "Word открыт"
    def edit(self): return "Word редактируется"
    def save(self): return "Word сохранён"

class PdfDoc(Document):
    def open(self): return "PDF открыт"
    def edit(self): return "PDF редактирование ограничено"
    def save(self): return "PDF сохранён"

class SheetDoc(Document):
    def open(self): return "Таблица открыта"
    def edit(self): return "Таблица редактируется"
    def save(self): return "Таблица сохранена"


docs = [WordDoc(), PdfDoc(), SheetDoc()]
for d in docs:
    print(d.open())
    print(d.edit())
    print(d.save())

