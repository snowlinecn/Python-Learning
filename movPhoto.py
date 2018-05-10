# 处理照片Exif信息

import exifread
import os
import sys
import shutil

# 读取EXIF信息
def getPhotoExif(filename):
    fd = open(filename,'rb')
    tags = exifread.process_file(fd)
    fd.close()
    return(tags)

def movePhoto(path,dst):
    n = 1
    m = 0
    for root, dirs, files in os.walk(path):
        for filename in files:
            filename = os.path.join(root,filename)
            f,ext = os.path.splitext(filename)
            if ext.lower() not in ('.jpg','.png','.mp4','.gif'):
                continue
            tags = getPhotoExif(filename)
            #print("----------------------------------------------------------------")            
            try:
                date = str(tags['EXIF DateTimeOriginal']).replace(":","-")[:10]

                #pwd = root + "\\" + date
                year = date[0:4]
                yearpath = dst+"\\"+year

                if not os.path.exists(yearpath):
                    os.mkdir(yearpath)
                
                daypath = yearpath+"\\"+date

                if not os.path.exists(daypath):
                    os.mkdir(daypath)
                
                shutil.move(filename,daypath)
                print(n,filename+"  ----->  "+daypath)
                n = n + 1
            except:
                print("照片",filename,"没有EXIF数据")
                m = m + 1
                pass
    
    print("共移动" ,n-1,"文件，",m,"个文件未移动")

def main():
    
    msg = '''使用方法：
        python movePhoto.py 源文件夹 目标文件夹
        '''
    
    if len(sys.argv) < 3:
        print(msg)
    else:
        movePhoto(sys.argv[1],sys.argv[2])
    
if __name__ == '__main__':
    
    main()