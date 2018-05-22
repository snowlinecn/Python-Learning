from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.filedialog

class MainWindow(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self["padx"]=1
        self["pady"]=1
        self.createWidgets()

    def createWidgets(self):

        self.grid(padx=10, pady=10)
        
        self.slb = Label(self,text = '')
        self.slb.grid(row=0,column=1, sticky=W)

        self.dlb = Label(self,text = '')
        self.dlb.grid(row=1,column=1, sticky=W)

        self.sbtn = Button(self,text="选择照片位置",width=15,command=self.spwd)
        self.sbtn.grid(row=0,column=0, sticky=W)

        self.dbtn = Button(self,text="选择移动到...",width=15,command=self.dpwd)
        self.dbtn.grid(row=1,column=0, sticky=W)
        
        self.mvtn = Button(self, text="移动",width=15, command=self.move_photo)
        self.mvtn.grid(row=2, column=0, sticky=W)

        self.scr = scrolledtext.ScrolledText(self, width=80, height=18) 
        self.scr.grid(row=3, column=0, columnspan=2)

    def spwd(self):
        spath = tkinter.filedialog.askdirectory()
        if spath != '':
            self.slb.config(text = spath)
            return spath

    def dpwd(self):
        dpath = tkinter.filedialog.askdirectory()
        if dpath != '':
            self.dlb.config(text = dpath)
            return dpath
   
    def move_photo(self):
        # for i in range(0,1000):
        #     self.scr.insert(END, str(i)+"\n")
        self.scr.insert(END, "照片将被移动到")
        self.scr.see(END)
    
app = MainWindow()
app.master.title('照片整理工具 V0.9')
app.master.geometry('600x350')
app.mainloop()