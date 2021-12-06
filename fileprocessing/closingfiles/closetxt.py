myfile = open("code.txt")
content = myfile.read()
myfile.close()

with open("code.txt") as myfile:
    content = myfile.read()
    
print(content)    
