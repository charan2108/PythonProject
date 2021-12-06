class Car:
    def __init__(self, make, year, model):
        self.make = make
        self.year = year
        self.model = model
        self.odometer = 0
    def name(self):
        name_c = str(self.year)+ " "+ self.make+" "+self.model
        return name_c.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer)+"miles")
    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("The odometer is not working")   
    def increment_odometer(self, miles):
        self.odometer += miles           
my_sportsCar = Car('1997', 'sports', 'Audi')
print(my_sportsCar.name())
# my_sportsCar.odometer=23
my_sportsCar.update_odometer(23)
my_sportsCar.increment_odometer(30)
my_sportsCar.read_odometer()

# child class
class ElectricCar(Car):
    def __init__(self, make, year, model):
        super().__init__(make, year, model)
        self.battery_size = 10000
    def  read_battery_size(self):
        print("The battery of the car is"+str(self.battery_size)+"-Kwh")    
my_Tatatesla = ElectricCar('Audi', 2020, 'f362')
print(my_Tatatesla.name())        
my_Tatatesla.read_battery_size()
    

        
    