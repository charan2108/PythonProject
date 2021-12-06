height = float(input("enter the height in m:"))
weight = float(input("enter the weight in kg:"))

bmi = round(weight / height**2)
print(bmi)
if(bmi < 18):
    print(f"your bmi {bmi}  is underweight")
elif bmi<25:
    print(f"your bmi {bmi}  is normal")
elif bmi<30:
    print(f"your bmi {bmi}  is overweight")
elif bmi<35:
    print(f"your bmi {bmi}  is obese")
else:
    print(f"your bmi {bmi}  is clinically obese")
   
  
    
    
        