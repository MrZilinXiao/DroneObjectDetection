import os
import cv2
import time

filelist = []
path = 'E:/DataSet/VisDrone2018-VID-val/sequences/uav0000137_00458_v'
filelist = os.listdir(path)  # 获取该目录下的所有文件名  ['aaa.jpg',...,'zzz.jpg']
fps = 24
size = (2688, 1512)
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
video = cv2.VideoWriter('out.mp4', fourcc, fps, size)

for item in filelist:
    if item.endswith('.jpg'):  # 判断图片后缀是否是.jpg
        item = path + '/' + item  # 全路径地址(c:/../scence/haha.jpg)
        img = cv2.imread(item)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
        video.write(img)  # 把图片写进视频

video.release()
