import requests
from json import JSONDecoder
import threading
import cv2


# Face++官方接口封装
def compareIm(faceId1, faceId2):
    # 传送两个本地图片地址 例如："D:/Downloads/wt.jpg"
    # try:
    # 官方给你的接口地址
    compare_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
    # 创建应用分配的key和secret
    key = "c8t2CdrRcU7cgMkKsw_3k7RA1A-aRmPr"
    secret = "c5WxozU_kBn-czNPoBLnHcem84Io_TOd"
    # 创建请求数据
    data = {"api_key": key, "api_secret": secret}
    files = {"image_file1": open(faceId1, "rb"), "image_file2": open(faceId2, "rb")}
    # 通过接口发送请求
    response = requests.post(compare_url, data=data, files=files)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    # print(req_dict)
    # 获得json文件里的confidence值，也就是相似度
    confindence = req_dict['confidence']
    if confindence > 75:
        print("图片相似度：", confindence)
    # confindence为相似度
    return confindence


# except Exception:
#    print("Unexpected error:", sys.exc_info()[0])


# 无限调用face++识别接口，并根据返回相似度判断人脸
def function(i):
    # while True:
    # try:
    if compareIm(imgdict[i], "face//None.jpg") > 75:
        print("身份确认是：", i)


# except Exception:
#   pass

# 该函数用于不断捕捉摄像头，并保存图片
def getimg():
    # while True:
    # 获取摄像头
    ret, frame = cap.read()
    # 保存图片，地址自定，要和function里传递的地址一样
    cv2.imwrite("face//None.jpg", frame)
    cv2.imshow("None", frame)


imgdict = {"程哲": "face//chengzhe.jpg", "姚元豪": "face//yaoyuanhao.jpg"}
#开启摄像头
cap = cv2.VideoCapture(0)
# 开启捕捉摄像头进程
threading.Thread(target=getimg).start()
# 每个匹配对象创建一个线程，为了降低等待延迟
for x in imgdict:
    # print(str(x))
    threading.Thread(target=function, args=(x,)).start()
