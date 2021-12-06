class Restaurant:
    def __init__(self, customer, food, dishes):
        self.customer = customer
        self.food = food
        self.dishes = dishes
        self.number_served = 0
    def  hotel(self):
        dhaba = str(self.customer)+" "+self.food+" "+self.dishes
        return dhaba.title()
    def read_number_served(self):
        print("This hotel has served "+str(self.number_served)+ " customers")
    def update_served_customer(self, customer):
        if customer >= self.number_served:
            self.number_served = customer
        else:
            print("Hotel is empty")
    def increment_served_customer(self, customer):
        self.number_served+= customer                
my_favR = Restaurant('350', 'indian', 'continental')
print(my_favR.hotel())
my_favR.update_served_customer(30)     
my_favR.increment_served_customer(350)   
my_favR.read_number_served()