# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# combined_name = name1 + name2
# lower_case_string = combined_name.lower()
# t = lower_case_string.count('t')
# r = lower_case_string.count('r')
# u = lower_case_string.count('u')
# e = lower_case_string.count('e')
# true = t + r + u + e
# l = lower_case_string.count('l')
# o = lower_case_string.count('o')
# v = lower_case_string.count('v')
# e = lower_case_string.count('e')
# love = l + o + v + e

# love_score = int(str(true) + str(love))
# print(love_score)

# if (love_score < 10) or (love_score > 90):
#     print(f"your love score is  {love_score}")
# elif (love_score >= 40) or (love_score <= 50):
#     print(f"your love score is {love_score}")
# else:
#     print(f"your score is {love_score}")       


print("Welcomr to the scoring and Wickets")
batsmen1 = input("Enter the name 1")
batsmen2 = input("Enter the name 2")

allrounder = batsmen1 + batsmen2
lower_case_string = allrounder.lower()

r = lower_case_string.count('r')
u = lower_case_string.count('u')
n = lower_case_string.count('n')
s = lower_case_string.count('s')
runs = r + u + n + s
w = lower_case_string.count('w')
i = lower_case_string.count('i')
c = lower_case_string.count('c')
k = lower_case_string.count('k')
e = lower_case_string.count('e')
t = lower_case_string.count('t')
s = lower_case_string.count('s')
wickets = w+i+c+k+e+t+s
legend = int(runs) + int(wickets)

if (runs > 10000) or (wickets >100):
    print(f"the bats runs {runs} and wickets are{wickets}")
elif (runs <= 8000) and (wickets <= 200):
    print(f"the batsmens runs {runs} and wickets {wickets} ")
else:
    print("NONE")
    

