import numpy as np
import cv2, time, os
from PIL import Image


# 人脸识别
def gface(image):
    # 模式参数
    dir_path = "E:\\OpenCv\\opencv-3.3.0\\data\\haarcascades"  # openCV路径
    filename = "haarcascade_frontalface_default.xml"  # 识别模式文件
    model_path = dir_path + "\\" + filename
    # 创建classifier
    clf = cv2.CascadeClassifier(model_path)
    # 设定灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 识别面部
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # 画方框
    result = []
    for (x, y, w, h) in faces:
        # 保存识别的人脸
        result.append((x, y, x + w, y + h))
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image, result


# 打开摄像头进行人脸检测
def faceCapture(name):
    cap = cv2.VideoCapture(0)  # 从摄像头中取得视频
    dir = 'face//'
    # 获取视频播放界面长宽
    # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

    # # 定义编码器 创建 VideoWriter 对象

    while (cap.isOpened()):
        # 读取帧摄像头
        ret, frame = cap.read()
        k=cv2.waitKey(1)&0xFF
        if ret == True:
            # 输出当前帧
            faceCapture, result = gface(frame)
            cv2.imshow('My Camera', faceCapture)
            if result:
                if k == ord('s'):
                    for x1, y1, x2, y2 in result:
                        face = frame[y1:y2, x1:x2]
                    print(name)
                    # cv2.imwrite(dir + name + '.jpg', face)
                    cv2.imencode('.jpg', face)[1].tofile(dir + name + '.jpg')
                    break
                elif k == ord('q'):
                    break
        else:
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()
