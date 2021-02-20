fang_wei = ['w', 'a', 's', 'd']
for_help = "用w,a,s,d来移动\n@是玩家\n*是终点\n当你走到你前面的方块上，它会从白色变成黑色或黑色变成白色"

class Player:
        x = 0
        y = 0

        def setxy(self, xx, yy):        #设置人物坐标
                self.x = xx
                self.y = yy

        def move(self, f): #输入方向移动人物
                if f == 'w':
                        self.y -= 1
                elif f == 'a':
                        self.x -= 1
                elif f == 's':
                        self.y += 1
                elif f == 'd':
                        self.x += 1

        def try_move(self, f_char, m, n):   #输入方向，地图和不能移动的字符返回是否能移动
                y = Player.y
                x = Player.x
                if f_char == 'w':
                        if y <= 0:
                                return False
                        else:
                                if m[y-1][x] == n:
                                        return False
                                else:
                                        return True
                elif f_char == 'a':
                        if x <= 0:
                                return False
                        else:
                                if m[y][x-1] == n:
                                        return False
                                else:
                                        return True
                elif f_char == 's':
                        if y+1 >= len(m):
                                return False
                        else:
                                if m[y+1][x] == n:
                                        return False
                                else:
                                        return True
                elif f_char == 'd':
                        if x+1 >= len(m[0]):
                                return False
                        else:
                                if m[y][x+1] == n:
                                        return False
                                else:
                                        return True
                '''if f_char == 'w':
                        if self.y-1 < 0 or m[self.x][self.y-1] == nchar:
                                return False
                        else:
                                return True
                elif f_char == 'a':
                        if  self.x-1 < 0 or m[self.x-1][self.y] == nchar:
                                return False
                        else:
                                return True
                elif f_char == 's':
                        if self.x > len(m) - 1 or m[self.x][self.y+1] == nchar:
                                return False
                        else:
                                return True
                elif f_char == 'd':
                        if self.y > len(m[0]) - 1 or m[self.x+1][self.y] == nchar:
                                return False
                        else:
                                return True'''

def fuzhi(m):
        return m
def change(m, f):
        x = Player.x
        y = Player.y
        if m[y][x] == '■':
                m[y][x] = '□'
        elif m[y][x] == '□':
                m[y][x] = '■'
        return m

def win(m, x, y):
        b = w = 0
        if m[y][x] != '×':
                return False
        for i in range(0, len(m)):
                for j in range(0, len(m[0])):
                        if m[i][j] == '■':
                                b += 1
                                if w > 0:
                                        return False
                        if m[i][j] == '□':
                                w += 1
                                if b > 0:
                                        return False
        return True
                                

                

def draw_map(m, x, y):          #输入地图和人物的坐标来绘制地图
        for i in range(0, len(m)):
                for j in range(0, len(m[0])):
                        if (x, y) == (j, i):
                                print('⊕', end = '')
                        else:
                                print(m[i][j], end = '')
                print()

count = 0
ditu1 = [
        ['Δ', '■','□', '▓'],
        ['▓', '□','■', '×']
        ]    #关卡地图

c_ditu1 = ditu1    #被实时运算的地图
Player.x, Player.y = 0, 0
print("使用help来查看帮助")
draw_map(c_ditu1, Player.x, Player.y)
print('回合数是%d\n坐标是(%d, %d)脚下的方块是%s' % (count, Player.x+1, Player.y+1, c_ditu1[Player.y][Player.x]))
while True:
        c = input()
        if c in fang_wei:
                if Player.try_move(Player, c, c_ditu1, '▓') == True:
                        print('可以移动')
                        Player.move(Player, c)
                        c_ditu1 = change(c_ditu1, c)
                        draw_map(c_ditu1, Player.x, Player.y)
                        count += 1
                        print('回合数是%d\n坐标是(%d, %d)脚下的方块是%s' % (count, Player.x+1, Player.y+1, c_ditu1[Player.y][Player.x]))
                        if win(c_ditu1, Player.x, Player.y) == True:
                                print('你赢了')
                                break
                else:
                        print('无法移动')
                        
        elif c == 'help':
                print(for_help)
        elif c == 'jump':
                break
        elif c == 're':
                c_ditu1  = ditu1
                count = 0
        elif c == 'e':
                0/0

print('你来到了第二关')



        
