# time bulitin
import time
while True:
    with open("textfile/fruits.txt") as file:
        print(file.read())
        time.sleep(10)
    