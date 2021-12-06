username = ''

# while username!= 'code':
#     username = input("Enter username")
#     if username == 'code':
#         break
#     else:
#         continue

while True:
    username = input("Enter username :")
    if username == 'code':
        break
    else:
        continue
# cheat sheet

for letter in 'abc':
    print(letter.upper())
    
phone_numbers = {"John Smith": "+37682929928",
                 "Marry Simpons": "+423998200919"}
for value in phone_numbers.keys():
    print(value)

phone_numbers = {"John Smith": "+37682929928",
                 "Marry Simpons": "+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)

while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
