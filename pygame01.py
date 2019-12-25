import pygame
import sys


pygame.init()
# pygame初始化
screen = pygame.display.set_mode((600,600))
# 创建窗口对象
myfont = pygame.font.Font(None,20)
# 创建字体对象

white = (233,233,233) 
blue = (122,122,122)
# 颜色参数

textImage = myfont.render('hello pygame',True,white)
    # 字体对象实例化，第二个参数表示抗锯齿

# 将所有事件放在一个循环中
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill(blue)
    # 窗口填充颜色
    screen.blit(textImage,(100,100))
    # 窗口对象位置
    pygame.display.update()
    # 窗口刷新