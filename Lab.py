#requirements: 
#super class called Vehicle with attribute for vehicle type (car, truck, boat, etc.)
#A class called Automobile inherit Vehicle and contain attributes year, make, model, doors, roof
#accepts user input for car and stores info. asks for automobile attribute input
#app will output info given in a neat easy to read format
#That's It!



#This defines the superclass 'Vehicle'
class Vehicle:
    def __init__(self, car, truck, suv, boat, bike):
        self.car = '0'
        self.truck = '0'
        self.suv = '0'
        self.boat = '0'
        self.bike = '0'
    
#this defines the child class called 'Automobile'
class Automobile(Vehicle):
    def __init__(self, car):
        super().__init__(self, car)
        self.year = '0000'
        self.make = '0'
        self.model = '0'
        self.doors = '0'
        self.roof = '0'
         
        
#this section will gather the information from the user
Automobile.make = input("Welcome! Please follow the prompts to enter details about your car.\nFirst, your make (ex: Toyota): ")

Automobile.model = input("Welcome! Please follow the prompts to enter details about your car.\nyour model (ex: camry): ")

Automobile.year = input("Welcome! Please follow the prompts to enter details about your car.\nyour year (ex: 2020): ")

Automobile.doors = input("Welcome! Please follow the prompts to enter details about your car.\n2 or 4: ")

Automobile.roof = input("Welcome! Please follow the prompts to enter details about your car.\nyour roof type (ex: convertable or hard top): ")


#this section will print out the information
print("\n\nVehicle Type: car\nYear:",Automobile.year,"\nMake:",Automobile.make,"\nModel:",Automobile.model,"\nNumber of Doors:", 
      Automobile.doors, "\nRoof Type:", Automobile.roof)