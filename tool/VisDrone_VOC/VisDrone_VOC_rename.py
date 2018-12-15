# -*- coding: utf-8 -*-
# Rename 
import os
path = "E:\\DataSet\\VisDrone2018-DET-train\\annotations1"
filelist = os.listdir(path)
count=1
for file in filelist:
    print(file)
for file in filelist:
    Olddir=os.path.join(path,file)
    if os.path.isdir(Olddir):   #skip folder
        continue
    filename=os.path.splitext(file)[0]
    filetype=os.path.splitext(file)[1]
    Newdir=os.path.join(path,str(count).zfill(6)+filetype)
    os.rename(Olddir,Newdir)
    count+=1