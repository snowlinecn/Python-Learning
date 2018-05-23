from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.filedialog
import exifread
import os
import sys
import shutil

class Main(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self["padx"] = 1
        self["pady"] = 1
        self.spath = ""
        self.dpath = ""
        self.create_widgets()

    # 读取EXIF信息
    def get_photoexif(self, filename):
        try:
            fd = open(filename,'rb')
        except:
            pass
        tags = exifread.process_file(fd)
        fd.close()
        return(tags)

    # 生成用户界面
    def create_widgets(self):
        self.grid(padx=10, pady=10)
        self.slb = Label(self, text=self.spath, justify="left", width=65, borderwidth=1, relief=SUNKEN)
        self.slb.grid(row=0, column=1, sticky=W)
        self.dlb = Label(self, text=self.dpath, justify="left", width=65, borderwidth=1, relief=SUNKEN)
        self.dlb.grid(row=1, column=1, sticky=W)
        
        self.sbtn = Button(self, text="源文件夹", width=15, command=self.set_spath)
        self.sbtn.grid(row=0, column=0, sticky=W)
        self.dbtn = Button(self, text="目标文件夹", width=15, command=self.set_dpath)
        self.dbtn.grid(row=1, column=0, sticky=W)
        self.mvtn = Button(self, text="开始移动", width=15, command=self.move_photo)
        self.mvtn.grid(row=2, column=0, sticky=W)
        
        self.scr = scrolledtext.ScrolledText(self, width=80, height=18) 
        self.scr.grid(row=3, column=0, columnspan=2)

    # 设置源路径
    def set_spath(self):
        self.spath = tkinter.filedialog.askdirectory().replace("/", "\\")
        if self.spath != "":
            self.slb.config(text=self.spath)
        else:
            self.slb.config(text="请选择照片文件夹")

    # 设置目标路径

    def set_dpath(self):
        self.dpath = tkinter.filedialog.askdirectory().replace("/", "\\")
        if self.dpath != "":
            self.dlb.config(text=self.dpath)
        else:
            self.dlb.config(text="请选择目标文件夹")

    # 移动照片            
    def move_photo(self):
        if self.spath != "" and self.dpath != "":
            n = 1
            m = 0
            for root, dirs, files in os.walk(self.spath):
                for filename in files:
                    filename = os.path.join(root,filename)
                    f,ext = os.path.splitext(filename)
                    if ext.lower() not in ('.jpg','.png','.mp4','.gif'):
                        continue
                    tags = self.get_photoexif(filename)
                    try:
                        date = str(tags['EXIF DateTimeOriginal']).replace(":","-")[:10]
                        year = date[0:4]
                        yearpath = self.dpath + "\\" + year
                        if not os.path.exists(yearpath):    # 生成年份文件夹
                            os.mkdir(yearpath)
                        daypath = yearpath + "\\" + date
                        if not os.path.exists(daypath): #   生成'年-月-日'文件夹
                            os.mkdir(daypath)
                        shutil.move(filename,daypath)   # 移动文件到目标文件夹
                        msg = str(n) + ": " + filename + "  ----->  " + daypath + "\n"
                        self.scr.insert(END, msg)        
                        n = n + 1
                    except:
                        msg = "照片" + filename + "没有EXIF数据，未移动" + "\n"
                        self.scr.insert(END, msg)
                        m = m + 1
                        pass
            
            msg = "共" + str(m+n-1) + "个文件，移动" + str(n-1) + "个文件，" +str(m) + "个文件未移动" + "\n"
            self.scr.insert(END, msg)
        else:
            self.scr.insert(END, "您还未选择照片文件夹！\n")
        self.scr.see(END)
    
app = Main()
app.master.title("照片整理工具 V0.9")
app.master.geometry("600x350")
app.mainloop()