def mumber_input(s, morenzhi):
    mumber = input(s)
    if mumber == '':
        return morenzhi
    return float(s)

Cr = mumber_input("圆半径(5)：", 5)
Cx = mumber_input("圆心x轴坐标(5)：", 5)
Cy = mumber_input("圆心y轴坐标(-5)：", -5)
xLeft = int(mumber_input("打印范围左边x坐标(0)：", 0))
xRight = int(mumber_input("打印范围右边x坐标(10)：", 10))
yUp = int(mumber_input("打印范围上边y坐标(0)：", 0))
yDown = int(mumber_input("打印范围下边y坐标(-10)：", -10))



def f(x, y):
    if (x-Cx)**2 + (y-Cy)**2 < Cr**2:
        return '**'
    else:
        return '  '

for y in range(yUp, yDown-1, -1):
    for x in range(xLeft, xRight+1):
        print(f(x, y), end = '')
    print()


input()
