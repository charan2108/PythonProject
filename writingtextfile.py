with open("textfile/fruits.txt", "w") as myfile:
    myfile.write("Aples\n")
    myfile.write("Bananas\n")
    myfile.write("grapes\n")
    myfile.write("mangoes\n")
    myfile.write("watermelon\n")
    myfile.write("pines\n")
    

with open("textfile/fruits.txt", "a+") as myfile:
    myfile.write("Aples\n")
    myfile.write("Bananas\n")
    myfile.write("grapes\n")
    myfile.write("mangoes\n")
    myfile.write("watermelon\n")
    myfile.write("pines\n")
    content = myfile.read()
print(content)

