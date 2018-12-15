#coding=utf-8
from __future__ import print_function #using print function in Python3
import socket
import threading
import struct
import cv2
import time
import os
import numpy
from settings import *


class webCamera:
    def __init__(self, resolution=RESOLUTION, host=("", REMOTE_PORT)): #参数初始化
        self.resolution = resolution
        self.host = host
        self.setSocket(self.host)
        self.img_quality = ONLINE_STREAM_QUALITY

    def setSocket(self, host):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
        self.socket.bind(self.host);
        self.socket.listen(5);
        print("Server is running on port:%d" % host[1]);

    def recv_config(self, client):
        info = struct.unpack("lhh", client.recv(8));
        if info[0] > 911: #add verification to avoid network issues
            self.img_quality = int(info[0]) - 911
            self.resolution = list(self.resolution)
            self.resolution[0] = info[1]
            self.resolution[1] = info[2]
            self.resolution = tuple(self.resolution)
            return 1
        else:
            return 0

    def _processConnection(self, client, addr):
        if (self.recv_config(client) == 0):
            return
        camera = cv2.VideoCapture(CAM_NUMBER)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), self.img_quality] #压缩参数

        f = open("video_log.log", 'a+')
        print("Got connection from %s:%d" % (addr[0], addr[1]), file=f);
        print("Resolution: %d x %d" % (self.resolution[0], self.resolution[1]), file=f)
        print("Open Camera Successfully!", file=f)
        print("Start at:%s" % time.strftime("%Y-%m-%d %H:%M:%S",
                                            time.localtime(time.time())), file=f)
        f.close()
        print("Got connection from %s:%d" % (addr[0], addr[1]));
        print("Resolution: %d x %d" % (self.resolution[0], self.resolution[1]))
        print("Open Camera Successfully!")
        print("Start at:%s" % time.strftime("%Y-%m-%d %H:%M:%S",
                                            time.localtime(time.time())))
        while 1:
            time.sleep(0.1)
            (grabbed, self.img) = camera.read()
            self.img = cv2.resize(self.img, self.resolution)  # typehint:self.img images
            if IS_COMPRESSED is True:
                result, imgencode = cv2.imencode('.jpg', self.img, encode_param)
                img_code = numpy.array(imgencode)  # typehint:imgencode ndarray
                self.imgdata = img_code.tostring()  # typehint:imgdata bytes
            else:
                self.imgdata = cv2.imencode('.jpg', self.img)[1].tostring()
            try:
                client.send(struct.pack("lhh", len(self.imgdata), # 指明struct类型
                                        self.resolution[0], self.resolution[1]) + self.imgdata);

            except:
                f = open("video_log.log", 'a+')
                print("%s:%d disconnected!" % (addr[0], addr[1]), file=f)
                print("End at: %s" % time.strftime("%Y-%m-%d %H:%M:%S",
                                                   time.localtime(time.time())), file=f)
                print("****************************************", file=f)
                camera.release()
                f.close()
                print("%s:%d disconnected!" % (addr[0], addr[1]))
                print("End at: %s" % time.strftime("%Y-%m-%d %H:%M:%S",
                                                   time.localtime(time.time())))
                print("****************************************")
                return

    def run(self):
        while 1:
            client, addr = self.socket.accept()
            clientThread = threading.Thread(target=self._processConnection,
                                            args=(client, addr,))
            clientThread.start()


if __name__ == "__main__":
    cam = webCamera() #initializing server
    cam.run()
