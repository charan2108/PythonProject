# reading lineby line
filename = 'pi.txt'
with open(filename) as file_object:
    contents =file_object.readlines()
    for line in file_object:
        print(line)