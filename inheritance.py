class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
a = Animal()
a.sound()
d = Dog()
d.sound()


class A:
    def show(self):
        print("This is class A")
class B(A):
    def show(self):
        super().show()
        print("This is class B")
obj = B()
obj.show()



class A:
    def display(self):
        print("Class A")
class B(A):
    def display(self):
        print("Class B")
class C(B):
    def display(self):
        print("Class C")
obj = C()
obj.display()


class Vehicle:
    def wheels(self):
        print("Vehicle has wheels")
class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")
c = Car()
c.wheels()
b = Bike()
b.wheels()


class Employee:
    def salary(self):
        print("Employee salary: 30000")
class Manager(Employee):
    def salary(self):
        print("Manager salary: 50000")
        print("Manager incentive: 10000")
e = Employee()
e.salary()
m = Manager()
m.salary()


class University:
    university_name = "ABC University"
    @classmethod
    def show_university(cls):
        print(cls.university_name)
class College(University):
    pass
print(College.university_name)
College.show_university()



class MathOps:
    @staticmethod
    def add(a, b):
        return a + b
class AdvancedOps(MathOps):
    pass
print(AdvancedOps.add(10, 20))




class Father:
    def skills(self):
        print("Father's skills")
class Mother:
    def skills(self):
        print("Mother's skills")
class Child(Father, Mother):
    pass
c = Child()
c.skills()
print(Child.mro())


class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
s = Student("Srividhya", 101)
s.display()