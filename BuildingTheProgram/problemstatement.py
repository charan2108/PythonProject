def sentence_maker(phrase):
    interogatives =("how", "what", "why")
    capitalize = phrase.capitalize()
    if phrase.startswith(interogatives):
        return "{}?".format(capitalize)
    else:
        return "{}?".format(capitalize)

 
results=[]
while True:
    name_input = input("Enter Name: ")
    if name_input == "\end":
        results.append(sentence_maker(name_input))
        
print(resutls)        
        
  
      
     