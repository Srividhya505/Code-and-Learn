from abc import ABC, abstractmethod
import math
# 11. Shape
class Shape(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r**2
    def perimeter(self): return 2 * math.pi * self.r
class Rectangle(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w
    def perimeter(self): return 2 * (self.l + self.w)
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def perimeter(self): return self.a + self.b + self.c
shapes = [Circle(5), Rectangle(4,5), Triangle(3,4,5)]
for sh in shapes:
    print(f"{sh.__class__.__name__}: Area={sh.area():.2f}, Peri={sh.perimeter():.2f}")
try:
    class IncompleteShape(Shape):
        def area(self): return 10
    obj = IncompleteShape()
except TypeError as e:
    print(f"Error if method missing: {e}\n")


#2.
class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self): pass
    @abstractmethod
    def pay(self, amount): pass
    @abstractmethod
    def refund(self, amount): pass
class UPIPayment(PaymentGateway):
    def authenticate(self): print("UPI: Verified via UPI PIN")
    def pay(self, amount): print(f"UPI: Paid Rs.{amount}")
    def refund(self, amount): print(f"UPI: Refunded Rs.{amount}")
class CardPayment(PaymentGateway):
    def authenticate(self): print("Card: Verified via OTP")
    def pay(self, amount): print(f"Card: Paid Rs.{amount}")
    def refund(self, amount): print(f"Card: Refunded Rs.{amount}")
class NetBankingPayment(PaymentGateway):
    def authenticate(self): print("NetBanking: Verified via Password")
    def pay(self, amount): print(f"NetBanking: Paid Rs.{amount}")
    def refund(self, amount): print(f"NetBanking: Refunded Rs.{amount}")
def checkout(gateway: PaymentGateway, amount):
    gateway.authenticate()
    gateway.pay(amount)
checkout(UPIPayment(), 500)
checkout(CardPayment(), 1000)
print()



#3.
class VehicleControl(ABC):
    @abstractmethod
    def accelerate(self): pass
    @abstractmethod
    def brake(self): pass
    @abstractmethod
    def steer(self, direction): pass
class CarControl(VehicleControl):
    def accelerate(self): print("Car: Pressing accelerator pedal")
    def brake(self): print("Car: Applying disc brakes")
    def steer(self, d): print(f"Car: Turning steering wheel to {d}")
class BikeControl(VehicleControl):
    def accelerate(self): print("Bike: Twisting throttle")
    def brake(self): print("Bike: Applying hand brake")
    def steer(self, d): print(f"Bike: Leaning to {d}")
class TruckControl(VehicleControl):
    def accelerate(self): print("Truck: Heavy acceleration")
    def brake(self): print("Truck: Applying air brakes")
    def steer(self, d): print(f"Truck: Wide turn to {d}")
def drive(vehicle: VehicleControl):
    vehicle.accelerate()
    vehicle.steer("left")
    vehicle.brake()
for v in [CarControl(), BikeControl(), TruckControl()]:
    drive(v)
print()


#4.
class DatabaseDriver(ABC):
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def execute(self, query): pass
    @abstractmethod
    def close(self): pass
class MySQLDriver(DatabaseDriver):
    def connect(self): print("MySQL: Connected")
    def execute(self, q): print(f"MySQL: Executing {q}")
    def close(self): print("MySQL: Closed")
class PostgresDriver(DatabaseDriver):
    def connect(self): print("Postgres: Connected")
    def execute(self, q): print(f"Postgres: Executing {q}")
    def close(self): print("Postgres: Closed")
class SQLiteDriver(DatabaseDriver):
    def connect(self): print("SQLite: Connected")
    def execute(self, q): print(f"SQLite: Executing {q}")
    def close(self): print("SQLite: Closed")
def run_app(driver: DatabaseDriver):
    driver.connect()
    driver.execute("SELECT * FROM users")
    driver.close()
run_app(MySQLDriver())
run_app(PostgresDriver())
print()



#5.
class ReportGenerator(ABC):
    def generate(self):
        self.load_data()
        self.process()
        self.export()
    @abstractmethod
    def load_data(self): pass
    @abstractmethod
    def process(self): pass
    @abstractmethod
    def export(self): pass
class PDFReport(ReportGenerator):
    def load_data(self): print("PDF: Loading data from DB")
    def process(self): print("PDF: Processing charts and tables")
    def export(self): print("PDF: Exported as report.pdf")
class ExcelReport(ReportGenerator):
    def load_data(self): print("Excel: Loading data from API")
    def process(self): print("Excel: Processing formulas")
    def export(self): print("Excel: Exported as report.xlsx")
print("Generating PDF:")
PDFReport().generate()
print("\nGenerating Excel:")
ExcelReport().generate()
