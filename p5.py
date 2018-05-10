from tkinter import *

master = Tk()
master.title("Hello World!")
Label(master, text="用户名", fg="red").grid(row=0, sticky = W)
Label(master, text="密   码").grid(row=1, sticky = W)

e1 = Entry(master).grid(row=0, column=1)
e2 = Entry(master).grid(row=1, column=1)

button = Button(master,text = "button")
button.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5, sticky = W + E + N + S)

mainloop()