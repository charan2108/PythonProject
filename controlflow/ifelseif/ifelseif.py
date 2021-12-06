print("Welcome to the roller costr ride")
height = int(input("Enter the height"))
age    =int(input("Enter the age"))

if height>120:
    print("Eligible for the ride")
elif age < 12:
    print("Pay $ 5")    
elif age < 18:
    print("Pay $ 12")    
elif age > 18:
    print("Pay $ 24")    
else:
    print("Not eligible")    