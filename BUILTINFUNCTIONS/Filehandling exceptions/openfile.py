myfile = open('file.txt')
content = myfile.read()
myfile.close()
with open("file.txt")  as myfile:
    content = myfile.read()
    