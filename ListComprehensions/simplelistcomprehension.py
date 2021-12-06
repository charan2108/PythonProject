temperature = [205,368,445,475,300]
# method1
# new_temp = []
# for temp in temperature:
#    new_temp.append(temp / 10)
# print(new_temp) 

# method2
new_temp = [temp/10 for temp in temperature]
print(new_temp)   

# method3
temperatures = [205,368,445,-475,300]

new_Temps =[temp/10 for temp in temperatures if temp!=-475]
print(new_Temps)

# method4
scores = [100,300,500,-650,8020]
print(scores)

new_Score =[score/10 for score in scores if score!=-650]
print(new_Score)


def foo(lst):
    return [i for i in lst if isinstance(i, int)]
print(int)