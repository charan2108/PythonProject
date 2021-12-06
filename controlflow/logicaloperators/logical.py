print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N")
add_cheese = input("Do you want cheese? Y or N")
billAmt = 0
if size == 'S':
    billAmt+= 15
elif size == 'M'  and size == 'L':
    billAmt+= 20
else:
    billAmt+=25
    
if add_pepperoni == "Y":
    if size == 'S':
        billAmt+= 2
    else:
        billAmt+= 3
if add_cheese == 'Y':
        billAmt+=1   
        
print(f"the final bill amount is {billAmt}")    
            
                   
                
    