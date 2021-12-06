# def mean(mylist):
#     the_mean = sum(mylist)/len(mylist)
#     return the_mean

# avg = mean([1,4,5])
# print(avg)

# def claculate_length(lst):
#     return len(lst)

# def square(b):
#     return b*b
# a = square(5)
# print(a)
    
# def converter(volume):
#     oz =float(input("Enter number of Ounces"))
#     ml =  oz * 29.57353
#     return ml
# a = converter(5)
# print(a)
# def converter(volume):
#     return volume * 29.57353

def maen(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean
student_grades = {'Maerry': 9.1,'dufty': 8.5, 'jhon': 7.5}

        
# a = -10
# if a * 2 > a:
#     print("greater")
# else:
#     print("leser tha")    
            

# def foo(x, array):
#     if x in array:
#         return True
#     else:
#         return False


# print(foo(1, [1, 2, 3]))
# print(foo(1, [2, 3]))
# print(foo(1, ['1', 2, 3]))

# def check_username(username):
#     if len(username) > 4:
#         return "successful"
#     else:
#         return "Another username"


# def check_username(username):
#     if len(username) > 4:
#         return "successful"
#     else:
#         return "Another username"

# def check_username(username):
#     if len(username) > 4:
#         return "successful"
#     else:
#         return "Another username"

# def check_username(username):
#     if len(username) > 4:
#         return "successful"
#     else:
#         return "Another username"
    

# if isinstance(x, int) or isinstance(x, float) or x == '1':
#     print("Valid type!")
# else:
#     print("Not valid!")

