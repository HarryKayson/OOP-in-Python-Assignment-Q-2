#Activity 2: Polymorphism Challenge! 🎭
#Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Car class inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Boat class inherits from Vehicle
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Creating objects of each class
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism: each class has its own implementation of move()
vehicles = [car, plane, boat]

for vehicle in vehicles:
    vehicle.move()
