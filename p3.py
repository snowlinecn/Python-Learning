from tkinter import *
from tkinter import ttk
import tkinter.filedialog

root = Tk()
root.title("照片整理工具 V0.9")
root.geometry("500x300")

frame = ttk.Frame(root, padding=10, relief="solid", borderwidth=2)
frame.grid(padx=10, pady=10)


def spwd():
    spath = tkinter.filedialog.askdirectory()
    if spath != '':
        slb.config(text = spath)


def dpwd():
    dpath = tkinter.filedialog.askdirectory()
    if dpath != '':
        dlb.config(text = dpath)

        
slb = ttk.Label(frame,text = '照片所在文件夹')
slb.grid(row=0,column=1,sticky=W)

dlb = Label(frame,text = '照片移动到文件夹')
dlb.grid(row=1,column=1,sticky=W)

sbtn = Button(frame,text="原照片文件夹",command=spwd)
sbtn.grid(row=0,column=0,sticky=W)
dbtn = Button(frame,text="移动到文件夹",command=dpwd)
dbtn.grid(row=1,column=0,sticky=W)

root.mainloop()