#vehicles.py
#Brian Sherrill
#09/12/2022
#Purpose: Demonstrate inheritence by creating a car subclass of a vehicle class

class Vehicle():
    def __init__(self):
        self.type = " "

class Auto(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        self.type = "Car"
        self.year = year
        self.make = make
        self.model = model 
        self.doors = doors
        self.roof = roof

    def display(self):  #displays a car's info in an organized way
        print("Vehicle Type: " + self.type)
        print("Vehicle Year: " + self.year)
        print("Vehicle Make: " + self.make)
        print("Vehicle Model: " + self.model)
        print("Vehicle Doors: " + self.doors)
        print("Vehicle Roof: " + self.roof)

print("Let's build you a car!\n")

#gathers car information
input_year = input("Enter the year: ")
input_make = input("Enter the make: ")
input_model = input("Enter the model: ") 
input_doors = input("How many doors? ")
input_roof = input("Solid roof or sunroof? ")

#creates the car
new_car = Auto(input_year, input_make, input_model, input_doors, input_roof)

#displays the car info
print("\nHere's your car: \n")
new_car.display()