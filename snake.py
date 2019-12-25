# -*- coding:utf-8 -*-
import pygame
    # 导入pygame库
import random
    # 导入random库

caption_width = 500  #画布宽度
caption_height = 500 #画布高度
white_color = (233, 233, 233) # 白色rgb
black_color = (12, 12, 12)
game_title = '贪吃蛇'
cell = 10 
    # 格子
snake_init_pos = [[250,250], [240,250], [230,250], [220,250]] 
    # 蛇的初始位置
food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10] 
    # 食物初始随机位置
head_pos = [250, 250]
    # 蛇头位置

pygame.init() 
    # 初始化 pygame

clock = pygame.time.Clock()
    # 创建clock时间对象

caption = pygame.display.set_mode((caption_width, caption_height))
    # 创建一个窗口对象，传入大小
pygame.display.set_caption(game_title)
    # 设置窗口标题

def draw_rect(color, position):
    # 绘制矩形，传入颜色和位置
    pygame.draw.rect(caption, color, pygame.Rect(position[0], position[1], cell, cell))

# 撞自己
def hit_the_self():
    # 第一个数据是蛇头，如果和蛇身其他数据相同则表示撞自己
    if snake_init_pos[0] in snake_init_pos[1:]:
        return True
    else:
        return False

# 蛇头撞墙
# 如果蛇头越界，则判定撞墙
def hit_the_wall(head_pos):
    if head_pos[0] >= caption_width or head_pos[0]<0 or head_pos[1] >= caption_height or head_pos[1] < 0:
        return True
    else:
        return False

# 吃食物，判定头与食物位置相同，则长一格
def change_direction(head_pos):
    global food_pos
    snake_init_pos.insert(0, list(head_pos))

    if head_pos != food_pos:
        snake_init_pos.pop()
    else:
        food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]

    if hit_the_self() or hit_the_wall(head_pos):
        # 给我死
        pygame.quit()

# 主函数
def main():
    for pos in snake_init_pos:
        draw_rect(white_color, pos)

    draw_rect(white_color, food_pos)
    pygame.display.update()

    while True:
        # 监听键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    head_pos[0] -= cell
                    change_direction(head_pos)
                elif event.key == pygame.K_RIGHT:
                    head_pos[0] += cell
                    change_direction(head_pos)
                elif event.key == pygame.K_UP:
                    head_pos[1] -= cell
                    change_direction(head_pos)
                elif event.key == pygame.K_DOWN:
                    head_pos[1] += cell
                    change_direction(head_pos)

        caption.fill(black_color)
        draw_rect(white_color, food_pos)

        # 更新蛇身
        for pos in snake_init_pos:
            draw_rect(white_color, pos)

        pygame.display.update()
        clock.tick(10)



if __name__ == '__main__':
    main()









