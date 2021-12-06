# fruits = []
# fruits.append('Apple')
# print(fruits)

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# states_of_texas = states_of_america[:]
# print(states_of_texas)
# print(states_of_america)
# # print(states_of_america[0])
# # print(states_of_america[1])
# # print(states_of_america[2])
# # print(states_of_america[3])
# # print(states_of_america[4])
# # print(states_of_america[5])
# # print(states_of_america[6])
# # print(states_of_america[7])
# # print(states_of_america[8])
# # print(states_of_america[9])
# # print(states_of_america[10])
# # print(states_of_america[11])
# # print(states_of_america[12])
# # print(states_of_america[13])
# # print(states_of_america[14])
# # print(states_of_america[15])
# # print(states_of_america[16])
# # print(states_of_america[17])
# # print(states_of_america[18])
# # print(states_of_america[19])
# # print(states_of_america[20])
# # print(states_of_america[21])
# # print(states_of_america[22])
# # print(states_of_america[23])
# # print(states_of_america[24])
# # print(states_of_america[25])
# # print(states_of_america[26])
# # print(states_of_america[27])
# # print(states_of_america[28])
# # print(states_of_america[29])
# # print(states_of_america[30])
# # print(states_of_america[31])
# # print(states_of_america[32])
# # print(states_of_america[33])
# # print(states_of_america[34])
# # print(states_of_america[35])
# # print(states_of_america[36])
# # print(states_of_america[37])
# # print(states_of_america[38])
# # print(states_of_america[39])
# # print(states_of_america[40])
# # print(states_of_america[41])
# # print(states_of_america[42])
# # print(states_of_america[43])
# # print(states_of_america[44])
# # print(states_of_america[45])
# # print(states_of_america[46])
# # print(states_of_america[47])
# # print(states_of_america[48])
# # print(states_of_america[49])

# # # appending
# # states_of_america.append("Alsaka")
# # print(states_of_america)
# # # extend
# # states_of_america.extend("Canda")
# # print(states_of_america)
# # states_of_america.extend("Delware")
# # print(states_of_america)
# # states_of_america.insert(2, 'Texas')
# # print(states_of_america)
# # print(states_of_america)
# # states_of_america.insert(2, 'Texas')
# # print(states_of_america)
# # states_of_america.remove('Texas')
# # print(states_of_america)
# # # states_of_america.pop([4])
# # # print(states_of_america)

# # # count
# # states_of_america.count('vermont')
# # print(states_of_america)
# # sort the list
# states_of_america.sort()
# print(states_of_america)
# # reverse
# states_of_america.reverse()
# print(states_of_america)

# list = ['Angela', 'Ben', 'Jenny', 'Micheal', 'Chole']
# print(list)
# print(type(list))
# print(len(list))
import random
names ="Angela, Ben, Jenny, Micheal, Chole"
name = names.split(", ")
num_items =(len(name))

random_c =random.randint(0, num_items - 1)
person_who_pays =name[random_c]

print(person_who_pays +"is going to buy the meal")
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
print(fruits[2])
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])