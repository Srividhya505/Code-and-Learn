#1.
class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.__balance = balance  # 1. Inaccessible from outside
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit failed: Amount must be positive")
            return
        self.__balance += amount
        print(f"Deposited {amount}, New Balance: {self.__balance}")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw failed: Amount must be positive")
            return
        if self.__balance - amount < 0:
            print(f"Withdraw failed: Insufficient balance. Current: {self.__balance}")
            return
        self.__balance -= amount
        print(f"Withdrew {amount}, New Balance: {self.__balance}")
    def get_balance(self):
        return self.__balance
print("--- 1. BankAccount ---")
acc = BankAccount("12345", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)


#2.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = 0
        self.set_marks(marks)
    def set_marks(self, marks): # Controlled method with range check
        if 0 <= marks <= 100:
            self.__marks = marks
            print(f"Marks updated to {self.__marks}")
        else:
            print(f"Invalid marks {marks}: Must be 0-100. Rejected.")
    def get_marks(self):
        return self.__marks
print("--- 2. Student ---")
s = Student("Ravi", 85)
s.set_marks(150)
s.set_marks(95)
s.__marks = -50


#3.
class SecureFile:
    def __init__(self, content, password):
        self.__content = content
        self.__password = password
        self.__logs = []
    def read(self, password):
        if password == self.__password:
            return self.__content
        else:
            self.__logs.append("Unauthorized attempt")
            return "Access Denied: Incorrect password"
    def get_logs(self, password):
        if password == self.__password:
            return self.__logs
        return "Access Denied"
print("--- 3. SecureFile ---")
file = SecureFile("Top Secret Data", "admin123")
print(file.read("wrongpass"))
print(file.read("admin123"))
print(f"Logs: {file.get_logs('admin123')}")
print()


#4.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # hidden
        self.__access_log = []
    def get_salary(self, requester):
        self.__access_log.append(f"Salary accessed by {requester}")
        print(f"[LOG] Salary accessed by {requester}")
        return self.__salary
    def update_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print(f"Salary updated to {new_salary}")
        else:
            print(f"Update failed: New salary {new_salary} must be higher than current {self.__salary} (prevent downgrade)")
print("--- 4. Employee ---")
emp = Employee("John", 50000)
print(f"Salary via getter: {emp.get_salary('HR')}")
emp.update_salary(40000)
emp.update_salary(60000)
print()


#5.
class Product:
    def __init__(self, name, price, discount_percent):
        self.name = name
        self.__price = 0
        self.__discount = 0
        self.set_price(price)
        self.set_discount(discount_percent)
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price
    def set_discount(self, discount):
        if not 0 <= discount <= 70:
            raise ValueError("Discount cannot exceed 70% and cannot be negative")
        self.__discount = discount
    def __calculate_final_price(self):
        return self.__price * (1 - self.__discount / 100)
    def get_final_price(self):
        return self.__calculate_final_price()
print("--- 5. Product ---")
p = Product("Shoes", 1000, 20)
print(f"Final Price: {p.get_final_price()}") # 800
try:
    p2 = Product("Bag", -100, 10)
except Exception as e:
    print(f"Price check: {e}")
try:
    p.set_discount(80)
except Exception as e:
    print(f"Discount check: {e}")