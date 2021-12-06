class  Cars:
    def __init__(self, name, year, model, mileage):
        self.name = name
        self.year = year
        self.model = model
        self.mileage =mileage
        self.speedometer = 0
    def code(self):
        program = str(self.year)+" "+self.name+" "+self.model+" "+self.mileage
        return program.title()
    def read_speedometer(self):
        print("The following car has the  "+str(self.speedometer)+"  speed")
    def update_speedometer(self, mileage):
        if  mileage >=self.speedometer:
            self.speedometer = mileage
        else:
            print("Not working")      
    def increment_speedometer(self, miles):
        self.speedometer += miles
                  
myBeast = Cars('Ferrari','2020', 'sports', '15')
print(myBeast.code())
myBeast.update_speedometer(120)
myBeast.increment_speedometer(200)
myBeast.read_speedometer()        

class  Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size 
    def battery(self):
        print("This car has a battery"+str(self.battery_size)+" Kwhbattery")           
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 720
        message = "This car can go up to the " +str(range)
        message+= "miles full charge"
        print(message)        
      
class ElectricCar(Cars):
    def __init__(self,name, year,model,mileage):
        super().__init__(name, year, model, mileage)
        self.battery = Battery()    
mytata_tesla = ElectricCar('ferrari', '2020', 's-220', '36')  
print(mytata_tesla.code())      
mytata_tesla.battery.battery()
mytata_tesla.battery.get_range()
    