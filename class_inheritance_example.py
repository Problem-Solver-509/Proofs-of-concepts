class Person:
    name = ''
    age = 0

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


class Student(Person):

    student_id = ''

    def __init__(self, student_name, student_age, student_id):
        Person.__init__(self, student_name, student_age)
        self.student_id = student_id

    def get_id(self):
        return self.student_id


person1 = Person('Richard', 23)
student1 = Student('Max', 22, 201666)

print(student1.get_id())
student1.show_name()
