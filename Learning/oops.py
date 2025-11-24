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
    
    def get_name(self):
        return self.name

# t_name = input('Enter your name:')

# t1 = Teacher(t_name)
# print(f"Hello {t1.get_name()}")


'''
Practice by passing whole ass list into the objects
'''

#non-static/normal method in OOP

class Std:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi {self.name} Your average marks is {sum/len(self.marks)}")


# s_1 = Std('Prashant', [20,30])

# s_1.get_avg()



#Static method in OOP


'''
-Methods that doesn't use the self parameter and works at class level

#decorator - allows us to wrap another function in order to extent the behaviour of the wrapped function, without permanently modifying it (compulsary)

-use where object is not necessary, like where self attributes are not necessary at all
'''

class School:
    @staticmethod #decorator
    def Student():
        print('Fuck youuuuuuuuu')


#four main modules of Object Oriented Programming


#Abstraction

'''
Abstraction: Hiding the implementation details of a class and only showing the essential features to the user.
'''

#implementation of abstraction

class Cars:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")

car1 = Cars()
# car1.start() #hid the unecessary background logic of the constructor and called the start function




#Encapsulation

'''
Encapsulation: Wrapping data and functions into a single object.

every functions we made above falls inside encapsulation.
'''


#Inheritance

'''
-When one class (child/derived) derives the properties & methods of another class (parent/base).

-We declare child same like the parent but we call parent class inside the parentheses of the child class.

-Super method: super() method is used to access methods of parent class in child class.

-Types of Inheritance:
    Single
    Multi-level
    Multiple

Single Inheritance: Base/Parent -> Derived/Child; #I1 to #I2

Multi level Inheritance: Parent -> Child -> Child; #I1 to #I3

Multiple inheritance: Parent1-> Child1 ; #I4 to #I5
                      Parent2 -> Child1
'''

#Example for Inheritance

class Car: # Parent class #I1
        def __init__(self, type):
            self.type = type

        @staticmethod
        def start():
            print('Car started.')

        @staticmethod
        def stop():
            print('Car stopped.')

class Toyota(Car): #child class
    def __init__(self, brand, type):
        self.brand = brand
        super().__init__(type)
        
# car2 = Toyota('Supra') #I2

class Supra(Toyota):
    brand = 'Supra'
    def __init__(self, gasoline, type ):
        self.gasoline = gasoline
        super().__init__(self.brand, type)

car2 = Supra('Petrol', 'Supercar')

print(car2.type, car2.brand, car2.gasoline) #I3


#Example of Multiple Inheritance #I4

class A:
    varA = "welcome to class A"

class B:
    varB = 'Welcome to class B'

class C(A, B):
    varC = 'Welcome to class C'

# c1 = C()
# print(f'{c1.varA}.....{c1.varB}.....{c1.varC}') #I5




####################################




#PolyMorphism

'''
-When the same operator is allowed to have different meaning according to the context.
'''

#####################################

#class method
'''
-Class method is bound to the class & receives the class as an implicit first argument.

Note: Static method can't access or modify the class state and generally for utility
'''
class Staff:
    name = 'Rahul'
    @classmethod
    def college(cls):
        cls.name = 'Sanjay Kumar time machine activate'
    


######################################


#More to go

'''
-del : used to delete object properties or object itself: {del s1.name or del s1}

-private(like) attributes & methods:
    Conceptual implementations in python
        ->Private attributes & methods are meant to be used only within the class and are not accessible from outside the class. We can make an attribute or an object private by addding two sequential underscores before the attribute or the object name.
        -> we can access it insite the class level but outside it is impossible to breach.

-Property decorator: use the method as property
'''


class BankAcc:
    def __init__(self, acc_no, acc_pw):
        self.acc_no = acc_no
        self.__acc_pw = acc_pw #privated the sensitive information


class Stdnts:
    def __init__(self, phy,chem, maths):
        self.chem = chem
        self.phy = phy
        self.maths = maths

    @property
    def percentage(self):
        return str((self.phy + self.chem+ self.maths)/3) + "%"
    

# rahul_marks = Stdnts(34, 66, 45)
# rahul_marks.phy = 94
# rahul_marks.maths = 63
# print(rahul_marks.percentage)