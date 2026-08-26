def electricity(rate_per_unit):
    def bill(units):
        total = rate_per_unit * units
        print("Electricity Bill:", total)
    return bill

e = electricity(8)
e(120)


def salary(bonus):
    def total_salary(basic_salary):
        total = basic_salary + bonus
        print("Total Salary:", total)
    return total_salary

s = salary(5000)
s(25000)


def discount(percent):
    def final_price(price):
        amount = price - (price * percent / 100)
        print("Final Price:", amount)
    return final_price

d = discount(20)
d(1000)


def bank_account(balance):
    def withdraw(amount):
        remaining = balance - amount
        print("Remaining Balance:", remaining)
    return withdraw

b = bank_account(10000)
b(2500)


def movie(movie_name):
    def booking(person_name):
        print(person_name, "booked a ticket for", movie_name)
    return booking

m = movie("Pushpa 2")
m("Srividhya")


def multiplier(number):
    def multiply(value):
        print("Multiplication:", number * value)
    return multiply

mul = multiplier(15)
mul(4)


def restaurant(food_item):
    def order(quantity):
        print("Food Item:", food_item)
        print("Quantity:", quantity)
    return order

r = restaurant("Biryani")
r(3)


def create_password(password):
    def check_password(new_password):
        if password == new_password:
            print("Access Granted")
        else:
            print("Access Denied")
    return check_password

p = create_password("python123")
p("python123")
p("java123")


def shopping_cart(item_name):
    def cart(quantity, price_per_item):
        total = quantity * price_per_item
        print("Item:", item_name)
        print("Quantity:", quantity)
        print("Total Price:", total)
    return cart

c = shopping_cart("Laptop")
c(2, 45000)



def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print("Count:", count)

    return increment

c = counter()

c()
c()
c()
c()
c()