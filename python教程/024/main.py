def hanoi(n, x, y, z):
    """
    汉诺塔游戏
    将n个盘子从x柱借助y柱移动到z柱上
    """
    if n == 1:
        print("%s --> %s"%(x, z))
    else:
        hanoi(n-1, x, z, y)
        print("%s --> %s"%(x, z))
        hanoi(n-1, y, x, z)

n = int(input("请输入汉诺塔的层数"))
hanoi(n, 'X', 'Y', 'Z')