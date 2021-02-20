import re

def xiang(string):
        s = 0
        e = 0
        c = 0
        re = []
        for i in string:
                if i == "+" | i == "-":
                        if c == 0:
                                c = 1
                                s = i
                        else:
                                e = i
                                
                                
                                
                                

"""def qie(string, char):
        '把string用char分割，返回左边和右边'
        restr = []
        for i in range(len(string)):
                if string[i] == char: 
                        return string[:i],string[i+1:]
        return -1"""
                        
print("未知数用x表示")
print("乘号，正号不能省略")
suanshi = input("请输入一元一次方程:")
zuo, you = suanshi.partition("=")[0], suanshi.partition("=")[2]


zuo_l = []
you_1 = []
