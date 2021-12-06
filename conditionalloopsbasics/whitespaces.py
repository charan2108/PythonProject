def weather(temperature):
    if temperature > 25:
        print("its hot")
    else:
        print("Its cool")
temp = float(input("Enter temperautre"))
# print(weather(temp))            
print(temp)          


# string formatting
temp = input("Enter name")
msg = "Hello %s" %temp
print(msg)  

temp = input("Enter name")
msg = "Hello %s" %temp
msg =f"Hello {temp}"
print(msg)  

def greetings(name):
    return " Hi %s" %name
#     print("Hi ," + name)
# greetings('Marry')    

def Hello(name):
    return "Hi %s" %name.title()