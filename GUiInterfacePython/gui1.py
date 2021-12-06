# from tkinter import *
# window =Tk()

# # button
# btn = Button(window, text="Execute")
# #button grid btn.pack()
# btn.grid(row=0,column=0)
# # entry grid
# entry = Entry(window)
# entry.grid(row=0,column=1)
# # text grid
# text=Text(window, height=1, width=20)
# text.grid(row=0,column=2)
# window.mainloop()


from tkinter import *
window =Tk()
def km_to_miles():
    print(e1_val.get())
    miles = e1_val.get()*1.6
    text.insert(END,miles)

# button
btn = Button(window, text="Execute", command=km_to_miles)

#button grid btn.pack()
btn.grid(row=0,column=0)

# entry grid
e1_val = StringVar()
entry = Entry(window,textvariable=e1_val)
entry.grid(row=0,column=1)

# text grid
text=Text(window, height=1, width=20)
text.grid(row=0,column=2)
window.mainloop()