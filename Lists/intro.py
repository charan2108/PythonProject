# Accessing Lists
monday_temp = [25.3,36.5,63.5]
print(monday_temp[0:2])
print(monday_temp[1:4]) 
print(monday_temp[:2])
print(monday_temp[2:])
 
# Negative index
monday_temp = [25.3,36.5,63.5, 50.5]
print(monday_temp[-1])
print(monday_temp[-2])
print(monday_temp[-3])
print(monday_temp[-4])

print(monday_temp[:-2])
print(monday_temp[-2:])

monday_temp = [25.3, 36.5, 63.5, 'Hello']
print(monday_temp[0][2])
