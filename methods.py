class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Withdrawn:", amount)
    def __str__(self):
        return "Account Holder: " + self.account_holder + ", Balance: " + str(self.balance)
    def __add__(self, other):
        return self.balance + other.balance
    def __sub__(self, other):
        return self.balance - other.balance
    def __eq__(self, other):
        return self.balance == other.balance
    def __lt__(self, other):
        return self.balance < other.balance
    def __getattribute__(self, name):
        print("Attribute accessed:", name)
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == "balance" and value < 0:
            print("Negative balance is not allowed")
        else:
            object.__setattr__(self, name, value)
a1 = BankAccount("Ram", 10000)
a2 = BankAccount("Ravi", 8000)
print(a1)
print(a2)
a1.deposit(2000)
print(a1)
a2.withdraw(1000)
print(a2)
print("Addition:", a1 + a2)
print("Subtraction:", a1 - a2)
print("Equal:", a1 == a2)
print("a1 has lower balance:", a1 < a2)
print(a1.account_holder)
a1.balance = -500


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity
    def __str__(self):
        return "Name: " + self.name + ", Price: " + str(self.price) + ", Quantity: " + str(self.quantity)
    def __add__(self, other):
        return self.total_price() + other.total_price()
    def __mul__(self, number):
        return self.price * number
    def __gt__(self, other):
        return self.total_price() > other.total_price()
    def __eq__(self, other):
        return self.price == other.price
    def __getattr__(self, name):
        return "Attribute not found"
    def __setattr__(self, name, value):
        if name == "price" and value < 0:
            print("Price cannot be less than 0")
        else:
            object.__setattr__(self, name, value)
p1 = Product("Laptop", 50000, 2)
p2 = Product("Mobile", 20000, 3)
print(p1)
print(p2)
print("Total Price of p1:", p1.total_price())
print("Total Price of p2:", p2.total_price())
print("Addition:", p1 + p2)
print("Multiplication:", p1 * 3)
print("p1 greater than p2:", p1 > p2)
print("Same Price:", p1 == p2)
print(p1.color)
p1.price = -100


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"
    def __str__(self):
        return "Name: " + self.name + ", Marks: " + str(self.marks)
    def __add__(self, other):
        return self.marks + other.marks
    def __truediv__(self, number):
        return self.marks / number
    def __ge__(self, other):
        return self.marks >= other.marks
    def __lt__(self, other):
        return self.marks < other.marks
    def __getattribute__(self, name):
        print("Attribute accessed:", name)
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == "marks" and (value < 0 or value > 100):
            print("Marks must be between 0 and 100")
        else:
            object.__setattr__(self, name, value)
s1 = Student("Ram", 85)
s2 = Student("Ravi", 70)
print(s1)
print(s2)
print("Grade of s1:", s1.grade())
print("Grade of s2:", s2.grade())
print("Total Marks:", s1 + s2)
print("Average Marks:", s1 / 2)
print("s1 >= s2:", s1 >= s2)
print("s1 < s2:", s1 < s2)
print(s1.name)
s1.marks = 120


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

    def __str__(self):
        return "Length: " + str(self.length) + ", Breadth: " + str(self.breadth)
    def __add__(self, other):
        return self.area() + other.area()
    def __sub__(self, other):
        return self.area() - other.area()
    def __eq__(self, other):
        return self.area() == other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def __getattr__(self, name):
        return "Attribute not found"
    def __setattr__(self, name, value):
        if (name == "length" or name == "breadth") and value <= 0:
            print("Length and breadth must be positive")
        else:
            object.__setattr__(self, name, value)
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 4)
print(r1)
print(r2)
print("Area of r1:", r1.area())
print("Area of r2:", r2.area())
print("Addition:", r1 + r2)
print("Subtraction:", r1 - r2)
print("Equal:", r1 == r2)
print("r1 greater than r2:", r1 > r2)
print(r1.color)
r1.length = -5


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def annual_salary(self):
        return self.salary * 12
    def __str__(self):
        return "Name: " + self.name + ", Salary: " + str(self.salary)
    def __add__(self, other):
        return self.salary + other.salary
    def __mul__(self, months):
        return self.salary * months
    def __ne__(self, other):
        return self.salary != other.salary
    def __le__(self, other):
        return self.salary <= other.salary
    def __getattribute__(self, name):
        print("Accessing:", name)
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == "salary" and value < 10000:
            print("Salary cannot be below 10000")
        else:
            object.__setattr__(self, name, value)
e1 = Employee("Ram", 30000)
e2 = Employee("Ravi", 25000)
print(e1)
print(e2)
print("Annual Salary of e1:", e1.annual_salary())
print("Annual Salary of e2:", e2.annual_salary())
print("Total Salary:", e1 + e2)
print("Salary for 6 months:", e1 * 6)
print("Salary not equal:", e1 != e2)
print("e1 salary <= e2 salary:", e1 <= e2)
print(e1.name)
e1.salary = 5000


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def reading_time(self):
        return self.pages * 2
    def __str__(self):
        return "Title: " + self.title + ", Author: " + self.author + ", Pages: " + str(self.pages)
    def __add__(self, other):
        return self.pages + other.pages
    def __floordiv__(self, days):
        return self.pages
    def __gt__(self, other):
        return self.pages > other.pages
    def __eq__(self, other):
        return self.title == other.title
    def __getattr__(self, name):
        return "Attribute not found"
    def __setattr__(self, name, value):
        if name == "title" and value == "":
            print("Title cannot be empty")
        elif name == "pages" and value <= 0:
            print("Pages must be positive")
        else:
            object.__setattr__(self, name, value)
b1 = Book("Python", "John", 200)
b2 = Book("Java", "David", 150)
print(b1)
print(b2)
print("Reading Time:", b1.reading_time(), "minutes")
print("Total Pages:", b1 + b2)
print("Pages per day:", b1 // 10)
print("b1 has more pages:", b1 > b2)
print("Same Title:", b1 == b2)
print(b1.price)
b1.title = ""
b1.pages = -50


class CartItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
    def final_amount(self):
        return self.price * self.quantity
    def __str__(self):
        return "Item: " + self.item_name + ", Price: " + str(self.price) + ", Quantity: " + str(self.quantity)
    def __add__(self, other):
        return self.final_amount() + other.final_amount()
    def __mod__(self, discount):
        return self.final_amount() % discount
    def __lt__(self, other):
        return self.final_amount() < other.final_amount()
    def __ge__(self, other):
        return self.quantity >= other.quantity
    def __getattribute__(self, name):
        print("Accessing:", name)
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == "quantity" and value < 1:
            print("Quantity must be at least 1")
        else:
            object.__setattr__(self, name, value)
c1 = CartItem("Laptop", 50000, 2)
c2 = CartItem("Mouse", 1000, 3)
print(c1)
print(c2)
print("Final Amount of c1:", c1.final_amount())
print("Final Amount of c2:", c2.final_amount())
print("Total Amount:", c1 + c2)
print("Remainder:", c1 % 1000)
print("c1 < c2:", c1 < c2)
print("c1 >= c2:", c1 >= c2)
print(c1.item_name)
c1.quantity = 0


class TimeDuration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def total_minutes(self):
        return self.hours * 60 + self.minutes
    def __str__(self):
        return "Hours: " + str(self.hours) + ", Minutes: " + str(self.minutes)
    def __add__(self, other):
        total = self.total_minutes() + other.total_minutes()
        hours = total // 60
        minutes = total % 60
        return TimeDuration(hours, minutes)
    def __sub__(self, other):
        total = self.total_minutes() - other.total_minutes()
        hours = total // 60
        minutes = total % 60
        return TimeDuration(hours, minutes)
    def __eq__(self, other):
        return self.total_minutes() == other.total_minutes()
    def __gt__(self, other):
        return self.total_minutes() > other.total_minutes()
    def __getattr__(self, name):
        return "Attribute not found"
t1 = TimeDuration(2, 30)
t2 = TimeDuration(1, 45)
print(t1)
print(t2)
print("Total Minutes of t1:", t1.total_minutes())
print("Total Minutes of t2:", t2.total_minutes())
print("Addition:", t1 + t2)
print("Subtraction:", t1 - t2)
print("Equal:", t1 == t2)
print("t1 is greater:", t1 > t2)
print(t1.seconds)


class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
    def upgrade_ram(self, extra_ram):
        self.ram = self.ram + extra_ram
    def __str__(self):
        return "Brand: " + self.brand + ", RAM: " + str(self.ram) + " GB, Price: " + str(self.price)
    def __add__(self, other):
        return self.price + other.price
    def __mul__(self, number):
        return self.price * number
    def __lt__(self, other):
        return self.price < other.price
    def __eq__(self, other):
        return self.ram == other.ram
    def __getattribute__(self, name):
        print("Accessing:", name)
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if (name == "ram" or name == "price") and value <= 0:
            print(name, "must be positive")
        else:
            object.__setattr__(self, name, value)
l1 = Laptop("Dell", 8, 50000)
l2 = Laptop("HP", 16, 60000)
print(l1)
print(l2)
l1.upgrade_ram(8)
print("After RAM Upgrade:", l1)
print("Total Price:", l1 + l2)
print("Price for 3 laptops:", l1 * 3)
print("l1 < l2:", l1 < l2)
print("Same RAM:", l1 == l2)
print(l1.brand)
l1.ram = 0
l1.price = -5000


class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, enemy):
        enemy.health = enemy.health - self.attack_power
        print(self.name, "attacked", enemy.name)
    def __str__(self):
        return "Name: " + self.name + ", Health: " + str(self.health) + ", Attack Power: " + str(self.attack_power)
    def __add__(self, other):
        return self.attack_power + other.attack_power
    def __sub__(self, other):
        return self.health - other.attack_power
    def __gt__(self, other):
        return self.health > other.health
    def __eq__(self, other):
        return self.attack_power == other.attack_power
    def __getattr__(self, name):
        return "Player stat not available"
    def __setattr__(self, name, value):
        if name == "health" and value < 0:
            object.__setattr__(self, name, 0)
        else:
            object.__setattr__(self, name, value)
p1 = Player("Ram", 100, 20)
p2 = Player("Ravi", 80, 15)
print(p1)
print(p2)
p1.attack(p2)
print(p2)
print("Combined Attack Power:", p1 + p2)
print("Health after attack:", p2 - p1)
print("p1 has greater health:", p1 > p2)
print("Same Attack Power:", p1 == p2)
print(p1.mana)
p2.health = -50
print(p2)