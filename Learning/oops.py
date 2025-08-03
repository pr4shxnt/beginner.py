'''
- To map with real word scenarios, we use objects in the code. This is called OOP.

- procedural code -> functional code -> oop

- to reduce redundancy and increase reusability we can also choose to use classes and objects too.

- its not compulsary to use object oreintation, but in practical we should.

- we make class before objects. Class is basically blueprint for creating objects.

- class -> classroom, object -> student

- list are objects, strings are objects.

- just like we did on backend using nodejs and mongodb, here from what i understood, class is mongoose model and objects are the objects that is in the format of that schema.
'''


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


s1 = Student("Prashant", 18)
s2 = Student("Jasmin", 19)

print(s1.name)

