# print("Welcome to the roller coste ride")
# height = int(input("Enter the height"))
# if height > 120:
#     print("Elgible for the  ride")
# else:
#     print("Try next time not eligible")   

print("Welcome to the roller cost")
height = int(input("Enter the height"))
bill = 0
if height > 120:
    print("You are eligible for ride")
    age = int(input("Enter the age"))
    if age < 12:
        bill=5
        print("Children tickets r 5 $")
    elif age <= 18:
        bill=7
        print("Youth tickets are  7 $")
    else:
        bill = 12
        print("Adult tickets r 12 $")
        
    want_photo = input("Do you want to take photo Y or N")
    if want_photo == 'Y':
        bill+= 3
        
    print(f" the final bill amount is {bill}")          
else:
    print("Not eligible for the ride")    
  
    


    