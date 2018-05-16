from tkinter import *
from tkinter import ttk
import tkinter.filedialog

class MainWindow(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()

    def createWidgets(self):
        #self["padding"]=10
        #, relief="solid", borderwidth=2)
        self.grid(padx=10, pady=10)
        
        self.slb = Label(self,text = '照片所在文件夹')
        self.slb.grid(row=0,column=1,sticky=W)

        self.dlb = Label(self,text = '照片移动到文件夹')
        self.dlb.grid(row=1,column=1,sticky=W)

        self.sbtn = Button(self,text="原照片文件夹",command=self.spwd)
        self.sbtn.grid(row=0,column=0,sticky=W)

        self.dbtn = Button(self,text="移动到文件夹",command=self.dpwd)
        self.dbtn.grid(row=1,column=0,sticky=W)

        self.txt = Text(self)
        self.txt.grid(row=2,column=0,columnspan=2,sticky=W)

    def spwd(self):
        spath = tkinter.filedialog.askdirectory()
        if spath != '':
            self.slb.config(text = spath)

    def dpwd(self):
        dpath = tkinter.filedialog.askdirectory()
        if dpath != '':
            self.dlb.config(text = dpath)
  
app = MainWindow()
app.master.title('照片整理工具 V0.9')
app.master.geometry('500x300')
app.mainloop()