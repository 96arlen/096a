class Course:
    def __init__(self, name, capacity):
        self.__name = name
        self.__students = []
        self.__capacity = capacity

    def add(self, student_name):
        if len(self.__students) < self.__capacity and student_name not in self.__students:
            self.__students.append(student_name)
            return f"{student_name} добавлен"
        return "Мест нет или студент уже в списке"

    def remove(self, student_name):
        if student_name in self.__students:
            self.__students.remove(student_name)
            return f"{student_name} удалён"
        return "Студент не найден"

    def list_students(self):
        return tuple(self.__students)



course = Course("Python", 3)
print(course.add("Максат"))
print(course.add("Аскат"))
print(course.add("Сули"))
print(course.add("Кадырбек"))
print(course.list_students())
print(course.remove("Айнур"))
print(course.list_students())

