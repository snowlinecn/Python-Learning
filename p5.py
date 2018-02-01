from tkinter import *
master = Tk()
Label(master, text="First").grid(row=0, sticky = W)
Label(master, text="Second").grid(row=1, sticky = W)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

button = Button(master,text = "button")
button.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5,
            pady = 5, sticky = W + E + N + S)
mainloop()
