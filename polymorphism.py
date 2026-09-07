#1.
# class Animal:
#     def make_sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def make_sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def make_sound(self):
#         print("Cat meows")
# class Cow(Animal):
#     def make_sound(self):
#         print("Cow moo")
# l= [Dog(), Cat(), Cow()]
# for i in l:
#     i.make_sound()


#2.
# def operate(device):
#     device.start()
# class car:
#     def start(self):
#         print("start")
# class computer:
#     def start(self):
#         print("Turns On")
# class washingmachine:
#     def start(self):
#         print("Washing")
# k = [car(), computer(), washingmachine()]
# for i in k:
#     operate(i)


#3.
# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,o2):
#         if isinstance(o2,Vector):
#             return Vector(self.x+o2.x,self.y+o2.y)
#         elif isinstance(o2,int):
#             self.x+=o2
#             self.y+=o2
#             return self
#     def __eq__(self,o2):
#         return self.x==o2.x and self.y==o2.y
# v1=Vector(2,5)
# v2=Vector(7,9)
# v3=Vector(10,1)
# print(v1+v2+v3)
# print(v1+5)



#4.
# class Transport:
#     def move(self):
#         print("Transport is moving")
# class Bus(Transport):
#     def move(self):
#         super().move()  # Reusing parent logic
#         print("Bus is moving on road with passengers")
# class Bike(Transport):
#     def move(self):
#         super().move()  # Reusing parent logic
#         print("Bike is moving fast on two wheels")
# t = Transport()
# b = Bus()
# k = Bike()
# print("Transport")
# t.move()
# print("Bus")
# b.move()
# print("Bike")
# k.move()



#6.
# class Payment:
#     def process(self,amount):
#         print("Payment Successful")
#         print(f"{amount} is paid")
# class creditcard(Payment):
#     def process(self,amount,card_type):
#         print(f"{card_type} is used")
#         super().process(amount)
# p1=Payment()
# p1.process(200)
# c1=creditcard()
# c1.process(2000,"visa")



#7.
# class Sorter:
#     def strategy(self, obj):
#         obj.logic()
# class BS:
#     def logic(self):
#         print("Bubble Sort logic")
#
# class MS:
#     def logic(self):
#         print("Merge Sort logic")
#
# class QS:
#     def logic(self):
#         print("Quick Sort logic")
# l = [MS(), QS(), BS()]
# for i in l:
#     Sorter().strategy(i)


#8






#9.
# def draw(shape):
#     shape.draw()
# class shapes:
#     pass
# class circle(shapes):
#     def draw(self):
#         print("circle")
# class square(shapes):
#     def draw(self):
#         print("square")
# class Rectangle(shapes):
#     def draw(self):
#         print("Rectangle")
# class car():
#     def draw(self):
#         print("car")
# l=[circle(),square(),Rectangle(),car()]
# for i in l:
#     draw(i)



#10.
# class Upi:
#     def payment(self,amount):
#         print(f"{amount} paid using upi")
# class card:
#     def pay(self,amount):
#         print(f"{amount} paid using card")
# class cash:
#     def pay(self,amount):
#         print(f"{amount} paid using cash")
#     def pay(obj,amount):
#         obj.pay(amount)
#     def pay(obj,amount):
#         if isinstance(obj,Upi):
#             obj.pay(amount)
# l=[Upi(),card(),cash()]
# for i in l:
#     pay(i,7000)
#     pay2(i,2000)


















