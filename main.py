from UI.face import *
from UI.admain import *
from faceDector import *
from UserManage import *
from Timing import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import sys, os, face_recognition, time
import matplotlib.pyplot as plt


class AdmainWindow(QtWidgets.QDialog, Ui_admainDialog):
    def __init__(self):
        super(AdmainWindow, self).__init__()
        self.setupUi(self)

    def takePhoto(self):
        name = self.nameEdit.text()
        if name != "":
            dir = 'face//'
            if not os.path.exists(dir):
                os.mkdir(dir)
            faceCapture(name)
            self.imgEdit.setText(name + '.jpg')
        else:
            img_box = QMessageBox.information(self, "拍照", "请输入姓名")

    def addUser(self):
        dbHelper = DBHelper()
        userName = self.nameEdit.text()
        userClass = self.classEdit.text()
        userImg = self.imgEdit.text()
        if userName == "" or userClass == "" or userImg == "":
            blank_box = QMessageBox.information(self, "注册", "不能输入空值")
        else:
            print('Name:{0}, Class:{1}, Image:{2}'.format(userName, userClass, userImg))
            sql = "insert into users values (null,'{0}','{1}','{2}')".format(userName, userClass, userImg)
            result = dbHelper.execute(sql, None)
            sql = "insert into record values (null,'{}',0)".format(userName)
            result1 = dbHelper.execute(sql, None)
            if result and result1:
                success_box = QMessageBox.information(self, "注册", "注册成功")
                print("插入数据成功")
            else:
                fail_box = QMessageBox.information(self, "注册", "注册失败")
                print("插入数据失败")


class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)

    def showCamera(self):
        if self.cameraButton.clicked:
            faceCapture('None')
            os.chdir('face//')
            face = QtGui.QPixmap('None.jpg').scaled(115, 120)
            self.faceView.setAlignment(Qt.AlignCenter)
            self.faceView.setPixmap(face)

    def showFace(self):
        if self.ImageButton.clicked:
            # os.chdir('face//')
            # face = QtGui.QPixmap('None.jpg').scaled(115, 120)
            # self.faceView.setAlignment(Qt.AlignCenter)
            # self.faceView.setPixmap(face)
            info = faceRecognize()
            if info != False:
                self.infoLabel.setText("打卡成功！" + info)
                # 数据表中的打卡记录设置为True
                addRecord(info)
            else:
                self.infoLabel.setText("识别错误，重新识别！")

    def showAdmain(self):
        if self.admainButton.clicked:
            admainDialog = AdmainWindow()
            admainDialog.show()
            admainDialog.exec_()

    def showStatis(self):
        print("打卡统计")
        drawPane()


def faceRecognize():
    print(os.getcwd())
    # 从数据库中获取已注册的用户脸部图片
    dbHelper = DBHelper()
    sql = 'select * from users';
    all_result = dbHelper.fetchall(sql, None)
    # 将jpg文件加载到numpy数组中
    imgs = list()
    labels = list()
    known_encoding = list()
    print(len(all_result))
    for i in range(len(all_result)):
        labels.append(all_result[i][1])
        imgs.append(face_recognition.load_image_file(all_result[i][3]))
        print("识别中...")
        # 获取每个图像文件中每个面部的面部编码
        encode = face_recognition.face_encodings(imgs[i])[0]
        known_encoding.append(encode)
    unknown_image = face_recognition.load_image_file('None.jpg')
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    try:
        results = face_recognition.face_distance(known_encoding, unknown_encoding)
        print(results)
        print(np.min(results))
        if np.min(results) > 0.30:
            return False
        # 找出最小值的下标
        min = 1.0
        minIndex = 0
        for i in range(len(results)):
            if results[i] < min:
                min = results[i]
                minIndex = i
        print(labels[minIndex])
        return labels[minIndex]
    except:
        return False


# 识别成功后数据表中的打卡记录设置为1
def addRecord(name):
    print('添加记录')
    dbHelper = DBHelper()
    sql = "update record set success=1 where name=%s"
    result = dbHelper.execute(sql, name)
    if result:
        print("打卡记录添加成功")
    else:
        print("打卡记录添加失败")


def drawPane():
    print("绘制饼状图")
    labels = ['Success', 'Failure']
    colors = ['red', 'blue']
    explode = [0.1, 0]
    sizes = []
    dh = DBHelper()
    sql = "select count(*) from record where success=%s"
    success = dh.fetchall(sql, 1)[0][0]
    sizes.append(success)
    print(success)
    sql1 = "select count(*) from record where success=%s"
    fail = dh.fetchall(sql1, 0)[0][0]
    sizes.append(fail)
    print(fail)
    plt.axes(aspect=1)
    plt.pie(x=sizes, labels=labels, explode=explode, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
    plt.title("Card Record")
    plt.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    app.exec_()
    # 每天零点定时更新数据库
    timerRun(21, 45)
    sys.exit(0)
