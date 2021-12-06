##n = int(input("Enter the number"))
##factorial = 1
##for i in range (1, n + 1):
##    
##    factorial*= i
##print("the factorial is", n ,"is", factorial)
####
##
##a = int(input("Enter"))
##for i in range(a, 0, -1):
##    for j in range(a - i):
##        print (' ', end="")
##    for j in range(2*i - 1):
##        print("*", end=" "),
##    print()       
##        



def solution(A):
    b = 0
    maxb = 0
    for a in A:
        if int(a)==0:
            b+=1
        elif int(a)==1:
            maxb=max(b,maxb) 
            b=0
    return maxb        
