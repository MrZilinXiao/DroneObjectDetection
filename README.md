# Drone Object Detect System
Drone Object Detect System is a project based on YOLOv3, with some interesting functions such as detecting image on a web page and a C/S remote monitor system.
> Note:This is also my project to participate in the Wuliangchun Cup Competition in Electronics and Information Engineering School of Sichuan University.Thanks to Professor Lei for providing necessary assistances.

**Attention: [YOLOv4 implemented with Darknet](https://github.com/AlexeyAB/darknet) released, Highly recommend!**



**Congratuations! My work achieved second-class prize in in the Wuliangchun Cup Competition in Electronics and Information Engineering School of Sichuan University.**
![](https://mrxiao.net/usr/uploads/2019/01/1649061890.png)

Competition Requirements in Chinese are as below:

我国经济的发展，带来机动车辆不断增多，国家国民安全需求不断增加，加之其他种种因素导致监控信息爆炸般增长，给人为监控带来诸多困难。加之无人机技术不断发展，利用无人机从高空采集视频信息已经成为常见的事情，在可见的未来，利用人工智能算法识别监控航拍图像成为可能。
	
本题目旨在利用深度学习的目标检测算法对航拍图像信息进行处理，输出图像将关注目标框选出来（关注目标如车辆、机场飞机、油罐等中大型物体），并对不同目标进行类别标注。	

基本要求： 

（1）通过目标检测的算法将航拍图像中的关注目标全部框选出来；

（2）能够准确地对全部框选出来的目标进行类别标注；

（3）监控识别不同类别物体的平均准确率达到60%以上。

（4）基于嵌入式平台（NVIDIA Jetson TX2）和Python语言设计App进行行人数目检测可视化窗口，也可以用摄像头在PC端实现所需要求，平台要求不限。

（5）利用深度神经网络，用深度学习的方法进行物体标注。

发挥部分：

（1）能够实时的监控检测航拍视频，框选出关注目标并标注，检测速度至少为10帧每秒。

（2）一个深度神经网络模型能够准确框选标注的目标类别尽可能多（甚至可以标注不同种类的汽车如卡车、轿车等）。

--------
## Installation Instrction
Before using, please configure settings.py first.
### Test Environment

Windows 10 1803 + NVIDIA GTX1060 6GB

Anaconda 4.3.0

Python 3.5.2

TensorFlow-GPU 1.8.0

Keras 2.2.0

CUDA 9.0.176 (https://developer.nvidia.com/cuda-90-download-archive)

cuDNN 7.3.1.20 (https://developer.nvidia.com/cudnn)

To get the source code files, run:
    git pull https://github.com/MrZilinXiao/VisualObjectDetection.git

    python main.py --help

to see what functions main.py have.

--------
## Functions Introduction
    python main.py --help
    
    usage: main.py [-h] [--image] [--input [INPUT]] [--output [OUTPUT]]
                   [--cam [CAM]] [--web [WEB]] [--online [ONLINE]] [--rtsp [RTSP]]
    
    optional arguments:
      -h, --help         show this help message and exit
      --image            Image detection mode, will ignore all positional
                         arguments, press Ctrl+C to stop.
      --input [INPUT]    [Optional] Video input path
      --output [OUTPUT]  [Optional] Video output path
      --cam 	         [Optional] Using camera,by default using built-in camera
                         of laptop,press Esc to stop.
      --web              [Optional] Using web server,press Ctrl+C to stop.
      --online           [Optional] Using a C/S structure system, will start a
                         video stream detecting client. Please run remote.py on
                         the device with a camera and configure ip and port in
                         settings.py first. Press Esc to stop.
      --rtsp [RTSP]      [Optional] Detect video stream from an IP camera or
                         something else. Need rtsp address as an argument.

remote_server.py can start an online streaming server which sends local camera's video stream to client.
                         
## Performance Test
Refer to [keras-yolo3](https://github.com/qqwweee/keras-yolo3).
## Training Instrction
Files under tool/ are used to train your own dataset. Considering about that different datasets have different formats of annotations, there are only specific training instructions for VOC dataset.

For VisDrone2018 Dataset, tools in tool folder will help.

## Model Download
For the offical model training on VOC dataset: https://pjreddie.com/media/files/yolov3.weights

For my model training on VisDrone dataset: (BaiduNetdisk)https://pan.baidu.com/s/1vhSEPMckC7QogL1WdOjWVQ Code：ouvo

For my training dataset : (BaiduNetdisk)https://pan.baidu.com/s/1QTzy8S7IHSHWtkrFxd100w Code: kdfv

Considering the requirements of the Competition, I prefer to use VisDrone2018 Dataset instead of VOC Dataset. 
