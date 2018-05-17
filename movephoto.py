''' 处理照片Exif信息 '''

import exifread
import os
import sys
import shutil

# 文件打开失败异常
class OpenFailException(Exception):
    pass

# 读取EXIF信息
def get_photoexif(filename):
    try:
        fd = open(filename,'rb')
    except:
        raise OpenFailException("不能打开文件[%s]\n" % filename)
    tags = exifread.process_file(fd)
    fd.close()
    return(tags)

# 移动照片
def move_photo(path,dst):
    n = 1
    m = 0
    for root, dirs, files in os.walk(path):
        for filename in files:
            filename = os.path.join(root,filename)
            f,ext = os.path.splitext(filename)
            if ext.lower() not in ('.jpg','.png','.mp4','.gif'):
                continue
            tags = get_photoexif(filename)
            #print("----------------------------------------------------------------")            
            try:
                date = str(tags['EXIF DateTimeOriginal']).replace(":","-")[:10]
                year = date[0:4]
                yearpath = dst+"\\"+year
                if not os.path.exists(yearpath):    # 生成年份文件夹
                    os.mkdir(yearpath)
                daypath = yearpath+"\\"+date
                if not os.path.exists(daypath): #   生成'年-月-日'文件夹
                    os.mkdir(daypath)
                shutil.move(filename,daypath)   # 移动文件到目标文件夹
                print(n,filename+"  ----->  "+daypath)        
                n = n + 1
            except:
                print("照片",filename,"没有EXIF数据")
                m = m + 1
                pass
    
    print("共移动" ,n-1,"个文件，",m,"个文件未移动")

def main():
    
    msg = '''使用方法：
        python movephoto.py 源文件夹 目标文件夹
        '''
    
    if len(sys.argv) < 3:
        print(msg)
    else:
        move_photo(sys.argv[1],sys.argv[2])
    
if __name__ == '__main__':
    
    main()