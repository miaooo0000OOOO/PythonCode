import math   
  
from PyQt5.QtCore import Qt  
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,   
        QSizePolicy, QToolButton, QWidget)  
  
class Button(QToolButton):  
    def __init__(self, text, parent = None):  
        super(Button, self).__init__(parent)  
          
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)  
        self.setText(text)  
          
    def sizeHint(self):  
        size = super(Button, self).sizeHint()  
        size.setHeight(size.height() + 20)  
        size.setWidth(max(size.width(), size.height()))  
        return size  
  
#[2] Calculator inherit QWidget  
class Calculator(QWidget):  
    NumDigitButtons = 10  # C++ enum   
      
    def __init__(self,  parent = None):  
        super(Calculator,  self).__init__(parent)  
          
        #[3]  
        self.display = QLineEdit('0')     # new QLineEdit  
        self.display.setReadOnly(True)   # 设置只读  
        self.display.setAlignment(Qt.AlignRight)  # 设置文字从右向左显示  
        self.display.setMaxLength(15)   # set max length  
        #[3]  
        #[4]  
        font = self.display.font()  
        font.setPointSize(font.pointSize() + 8)  
        self.display.setFont(font)  
        #[4]  
          
        #[5] create button  0, 1, 2, .... 9  
        self.digitButtons = []  
          
        for i in range(Calculator.NumDigitButtons):  
            self.digitButtons.append(self.createButton(str(i), self.digitClicked))  
        #[5]  
          
        #[7] create button   
        self.pointButton = self.createButton(".",  self.pointClicked)  
        self.changeSignButton = self.createButton(u"\N{PLUS-MINUS SIGN}",  self.changeSignClicked)  
          
        self.backspaceButton = self.createButton("Backspace",  self.backspaceClicked)  
        self.clearButton = self.createButton("Clear",  self.clearClicked)  
        self.clearAllButton = self.createButton("Clear All",  self.clearAll)  
          
        self.clearMemoryButton = self.createButton("MC",  self.clearMemory)  
        self.readMemoryButton = self.createButton("MR",  self.readMemory)  
        self.setMemoryButton = self.createButton("MS",  self.setMemory)  
        self.addToMemoryButton = self.createButton("M+",  self.addToMemory)  
          
        # / * - +    
        self.divisionButton = self.createButton(u"\N{DIVISION SIGN}", self.multiplicativeOperatorClicked)  
        self.timesButton = self.createButton(u"\N{MULTIPLICATION SIGN}", self.multiplicativeOperatorClicked)  
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)  
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)  
          
        self.squareRootButton = self.createButton("Sqrt", self.unaryOperatorClicked)  
        self.powerButton = self.createButton(u"x\N{SUPERSCRIPT TWO}", self.unaryOperatorClicked)  
        self.reciprocalButton = self.createButton("1/x", self.unaryOperatorClicked)  
        self.equalButton = self.createButton("=", self.equalClicked)  
        #[7]  
          
        #[9]  
        mainLayout = QGridLayout()  
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)  
          
        mainLayout.addWidget(self.display, 0, 0, 1, 6)  
        mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)  
        mainLayout.addWidget(self.clearButton, 1, 2, 1, 2)  
        mainLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)  
          
        mainLayout.addWidget(self.clearMemoryButton, 2, 0)  
        mainLayout.addWidget(self.readMemoryButton, 3, 0)  
        mainLayout.addWidget(self.setMemoryButton, 4, 0)  
        mainLayout.addWidget(self.addToMemoryButton, 5, 0)  
          
        for i in range(1,  Calculator.NumDigitButtons):  
            row = ((9 - i) / 3) + 2  
            column = ((i -1) % 3) + 1  
            mainLayout.addWidget(self.digitButtons[i],  row,  column)  
           
        mainLayout.addWidget(self.digitButtons[0], 5, 1)  
        mainLayout.addWidget(self.pointButton, 5, 2)  
        mainLayout.addWidget(self.changeSignButton, 5, 3)  
         
        mainLayout.addWidget(self.divisionButton, 2, 4)  
        mainLayout.addWidget(self.timesButton, 3, 4)  
        mainLayout.addWidget(self.minusButton, 4, 4)  
        mainLayout.addWidget(self.plusButton, 5, 4)   
          
        mainLayout.addWidget(self.squareRootButton, 2, 5)  
        mainLayout.addWidget(self.powerButton, 3, 5)  
        mainLayout.addWidget(self.reciprocalButton, 4, 5)  
        mainLayout.addWidget(self.equalButton, 5, 5)  
        self.setLayout(mainLayout)  
          
        self.setWindowTitle("Calculator")  
        #[9]  
          
          
    #[6] 函数未实现  
    def createButton(self, text, member):  
        button = Button(text)  
        button.clicked.connect(member)  # member = SLOT(函数名)  
        return button  
          
    def digitClicked(self):  
        print("digitClicked")              
    #[6]  
      
    #[8] function about buttons 函数未实现  
    def pointClicked(self):  
        print("pointClicked")        
         
    def changeSignClicked(self):  
        print("changeSignClicked")   
      
    def backspaceClicked(self):  
        print("backspaceClicked")   
      
    def clearClicked(self):  
        print("clearClicked")   
      
    def clearAll(self):  
        print("clearAll")   
      
    def clearMemory(self):  
        print("clearMemory")  
          
    def readMemory(self):  
        print("readMemory")  
          
    def setMemory(self):  
        print("setMemory")  
       
    def addToMemory(self):  
        print("addToMemory")  
      
    def multiplicativeOperatorClicked(self):  
        print("multiplicativeOperatorClicked")  
      
    def additiveOperatorClicked(self):  
        print("additiveOperatorClicked")  
          
    def unaryOperatorClicked(self):  
        print("unaryOperatorClicked")  
          
    def equalClicked(self):  
        print("equalClicked")  
    #[8]  
  
  
#[1] same as C++ main.cpp  
if __name__ == '__main__':  
    import sys  
    app = QApplication(sys.argv)  
    calc = Calculator()  
    calc.show()  
    sys.exit(app.exec_())  
