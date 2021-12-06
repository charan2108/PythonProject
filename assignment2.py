class Bikes:
    def __init__(self, name, year,model,mileage):
        self.name = name
        self.year=year
        self.model=model
        self.mileage=mileage
        self.speedometer = 0
    def motobike(self):
        harley = str(self.year)+" "+self.name+" "+self.model+" "+self.mileage
        return harley.title()
    def indicate_speedometer(self):
        print("the following bike has the  "+str(self.speedometer)+" distance travelled in miles or km ")
    def update_speedometer(self, mileage):
        if mileage >= self.speedometer:
            self.speedometer = mileage
        else:
            print("Not working")   
    def increment_speedometer(self, km):
        self.speedometer+= km
                     
moBike = Bikes('DUcati', '2020', 'sportrs', '20')
print(moBike.motobike())
moBike.update_speedometer(120)
moBike.increment_speedometer(300)
moBike.indicate_speedometer()        

class ElectricBike(Bikes):
    def __init__(self, name, year, model, mileage):
        super().__init__(name, year, model, mileage)
myTata_bike = ElectricBike('Austin', 'model 36', 150, 300)            
print(myTata_bike.motobike()) 
            