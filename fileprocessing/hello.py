# open method
with open("textfiles/writingfile.txt", "r") as myfile:
    content = myfile.read()
print(content)  

# write method  
with open("textfiles/fruit.txt", "w") as myfile:
   myfile.write("grapes\nApples\nBears")
   myfile.write("Oranges")
