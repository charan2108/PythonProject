myfile = open("textfile/fruits.txt")
content = myfile.read()
myfile.close()

with open("textfile/fruits.txt") as myfile:
    content = myfile.read()

    
print(content)
