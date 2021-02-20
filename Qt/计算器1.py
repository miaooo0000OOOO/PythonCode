#!/usr/bin/env python  
# -*- coding:UTF-8 -*-  
# calculator  
  
import sys  
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
  
  
class UI_form(QWidget):  
    def __init__(self,parent = None):  
             QWidget.__init__(self)  
  
             self.setWindowTitle('UI')  
  
             grid = QGridLayout() #网格式布局  
             global lcd  
             lcd = QTextBrowser()  
             lcd.setFixedHeight(90)  
             lcd.setFont(QFont("Microsoft YaHei", 20))  
             lcd.setText('0'.decode('utf-8'))  
             grid.setSpacing(0)  
             grid.addWidget(lcd, 0, 0, 1, 5)  
  
    # ---------------------按钮定义及显示-------------------------  
  
             button_0 = QPushButton('0')  
             grid.addWidget(button_0,5,0)  
  
             button_1 = QPushButton('1')  
             grid.addWidget(button_1,4,0)  
  
             button_2 = QPushButton('2')  
             grid.addWidget(button_2,4,1)  
  
             button_3 = QPushButton('3')  
             grid.addWidget(button_3,4,2)  
  
             button_4 = QPushButton('4')  
             grid.addWidget(button_4,3,0)  
  
             button_5 = QPushButton('5')  
             grid.addWidget(button_5,3,1)  
  
             button_6 = QPushButton('6')  
             grid.addWidget(button_6,3,2)  
  
             button_7 = QPushButton('7')  
             grid.addWidget(button_7,2,0)  
  
             button_8 = QPushButton('8')  
             grid.addWidget(button_8,2,1)  
  
             button_9 = QPushButton('9')  
             grid.addWidget(button_9,2,2)  
  
             button_plus = QPushButton('+')  
             grid.addWidget(button_plus,2,3)  
  
             button_dec = QPushButton('-')  
             grid.addWidget(button_dec,3,3)  
  
             button_mul = QPushButton('*')  
             grid.addWidget(button_mul,4,3)  
  
             button_dev = QPushButton('/')  
             grid.addWidget(button_dev,5,3)  
  
             button_eq = QPushButton('=')  
             grid.addWidget(button_eq,5,2)  
  
             button_point = QPushButton('.')  
             grid.addWidget(button_point,5,1)  
  
             button_close = QPushButton('Close')  
             grid.addWidget(button_close,1,0)  
  
             button_clear = QPushButton('Clear')  
             grid.addWidget(button_clear,1,1)  
  
             button_blk = QPushButton('Blk')  
             grid.addWidget(button_blk,1,2)  
  
#--------------------------------------------------  
  
             self.setLayout(grid)  
             self.resize(350, 300)  
  
             self.str1 = ''#接收第一个要运算的数  
             self.str2 = ''#接收第二个要运算的数  
             self.flag = '0'  
             self.calFlag = ''  
             lcd.setText(self.str1)  
  
             #数字键事件处理  
             QObject.connect(button_7,SIGNAL("clicked()"),self.func_button7)  
             QObject.connect(button_8,SIGNAL("clicked()"),self.func_button8)  
             QObject.connect(button_9,SIGNAL("clicked()"),self.func_button9)  
             QObject.connect(button_4,SIGNAL("clicked()"),self.func_button4)  
             QObject.connect(button_5,SIGNAL("clicked()"),self.func_button5)  
             QObject.connect(button_6,SIGNAL("clicked()"),self.func_button6)  
             QObject.connect(button_1,SIGNAL("clicked()"),self.func_button1)  
             QObject.connect(button_2,SIGNAL("clicked()"),self.func_button2)  
             QObject.connect(button_3,SIGNAL("clicked()"),self.func_button3)  
             QObject.connect(button_0,SIGNAL("clicked()"),self.func_button0)  
             #运算符按键事件处理  
             QObject.connect(button_plus,SIGNAL("clicked()"),self.func_buttonAdd)  
             QObject.connect(button_dec,SIGNAL("clicked()"),self.func_buttonDec)  
             QObject.connect(button_mul,SIGNAL("clicked()"),self.func_buttonMul)  
             QObject.connect(button_dev,SIGNAL("clicked()"),self.func_buttonChu)  
             QObject.connect(button_eq,SIGNAL("clicked()"),self.func_buttonEqual)  
             QObject.connect(button_clear,SIGNAL("clicked()"),self.func_buttonClear)  
    def closeEvent(self,event):#窗口关闭时的处理，只实现这个函数就可以，不用去调用  
        reply = QMessageBox.question(self,'Message',"Are you sure to quit?",QMessageBox.Yes,QMessageBox.No)  
        if reply == QMessageBox.Yes:  
            event.accept()  
        else:  
            event.ignore()  
    def func_button7(self):  
  
        if self.flag == '1':  
            self.str2 = self.str2 + '7'  
            lcd.setText(self.str2)  
        else:  
            self.str1 = self.str1 + '7'  
            lcd.setText(self.str1)  
    def func_button8(self):  
        if self.flag == '1':  
            self.str2 = self.str2 + '8'  
            lcd.setText(self.str2)  
        else:  
            self.str1 = self.str1 + '8'  
            lcd.setText(self.str1)  
    def func_button9(self):  
        if self.flag == '1':  
            self.str2 = self.str2 + '9'  
            lcd.setText(self.str2)  
        else:  
            self.str1 = self.str1 + '9'  
            lcd.setText(self.str1)  
    def func_button4(self):  
        if self.flag == '1':  
            self.str2 = self.str2 + '4'  
            lcd.setText(self.str2)  
        else:  
            self.str1 = self.str1 + '4'  
            lcd.setText(self.str1)  
    def func_button5(self):  
        if self.flag == '1':  
            self.str2 = self.str2 + '5'  
            lcd.setText(self.str2)  
        else:  
            self.str1 = self.str1 + '5'  
            lcd.setText(self.str1)  
    def func_button6(self):  
        if self.flag == '1':  
            self.str2 = self.str2 + '6'  
            lcd.setText(self.str2)  
        else:  
            self.str1 = self.str1 + '6'  
            lcd.setText(self.str1)  
    def func_button1(self):  
        if self.flag == '1':  
            self.str2 = self.str2 + '1'  
            lcd.setText(self.str2)  
        else:  
            self.str1 = self.str1 + '1'  
            lcd.setText(self.str1)  
    def func_button2(self):  
        if self.flag == '1':  
            self.str2 = self.str2 + '2'  
            lcd.setText(self.str2)  
        else:  
            self.str1 = self.str1 + '2'  
            lcd.setText(self.str1)  
    def func_button3(self):  
        if self.flag == '1':  
            self.str2 = self.str2 + '3'  
            lcd.setText(self.str2)  
        else:  
            self.str1 = self.str1 + '3'  
            lcd.setText(self.str1)  
    def func_button0(self):  
        if self.flag == '1':  
            self.str2 = self.str2 + '0'  
            lcd.setText(self.str2)  
        else:  
            self.str1 = self.str1 + '0'  
            lcd.setText(self.str1)  
    #运算符处理函数  
    def func_buttonAdd(self):  
        lcd.setText(self.str2)  
        self.flag = '1'  
        self.calFlag = '1'  
    def func_buttonDec(self):  
        lcd.setText(self.str2)  
        self.flag = '1'  
        self.calFlag = '2'  
    def func_buttonMul(self):  
        lcd.setText(self.str2)  
        self.flag = '1'  
        self.calFlag = '3'  
    def func_buttonChu(self):  
        lcd.setText(self.str2)  
        self.flag = '1'  
        self.calFlag = '4'  
    def func_buttonEqual(self):  
        #字符串先转换为数字，计算结果后再转换为字符串  
        if self.calFlag == '1':  
            num = str(int(self.str1) + int(self.str2))  
        elif self.calFlag == '2':  
            num = str(int(self.str1) - int(self.str2))  
        elif self.calFlag == '3':  
            num = str(int(self.str1) * int(self.str2))  
        elif self.calFlag == '4':  
             num = str(int(self.str1) / int(self.str2))  
        else:  
            self.calFlag = '0'  
        lcd.setText(num)  
    def func_buttonClear(self):  
        self.str1 = ''  
        self.str2 = ''  
        lcd.setText('')  
        self.flag = '0'  
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    myapp = UI_form()  
    myapp.show()  
    sys.exit(app.exec_()) 
