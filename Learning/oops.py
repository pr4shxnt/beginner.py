'''
- To map with real word scenarios, we use objects in the code. This is called OOP.

- procedural code -> functional code -> oop

- to reduce redundancy and increase reusability we can also choose to use classes and objects too.

- its not compulsary to use object oreintation, but in practical we should.

- we make class before objects. Class is basically blueprint for creating objects.

- class -> classroom, object -> student

- list are objects, strings are objects.

- just like we did on backend using nodejs and mongodb, here from what i understood, class is mongoose model and objects are the objects that is in the format of that schema.

- constructor(__init__ function): all classes have a function called __init__(), which is always executed when the class is being initiated.

- the self parameter is basically the same as the "this" in javascript. it is basically reference to the current instance of class and is used to acess variables that belongs to the class. in js you dont have to pass this as an argument, but in python you have to pass delf as a parameter.


- the data or variables stored inside a class or object is called attributes.

- default constructors are basically constructors with single parameter: self.

'''



class Class: 
    def __init__(self): # Default constructor
        pass

class Student:
    collge_name = "Sunway College Kathmandu" #1
    name = 'anonymous' #2

    def __init__(self, name, student_id): # Parameterized constructor
        self.name = name
        self.student_id = student_id


s1 = Student("Prashant", 18)


'''
class attributes and instance attributes

- so basically (#1 college_name) is a class attribute as it is common in all student's instance attribute and will occupy more space in the memory if it was written as instance attribute.

- (#2 name) is dummy name, if name isn't passed as a instance attribute. but if it is passed it always shows the passed value when we print because ( instance attribute > class attribute.)
'''


# Methods

'''
- class consists of 2 things, attributes & methods.

- attributes: features

-function: methods

- methods are basically functions that belongs to an object.

-we can reuse it by objectname.methodname;

hello function is a method here in this context.
'''


class Teacher:
    def __init__(self, fullname):
        self.name = fullname

    def hello(self):
        print(f'hello {self.name}')


t1 = Teacher('Shyam')
t1.hello()
