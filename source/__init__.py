import pygame
from source.constants import SPACE_X, SPACE_Y


# 1.游戏初始化
pygame.init()
# 2.设置游戏标题
pygame.display.set_caption("Gomoku")
# 3.设置屏幕大小
SCREEN = pygame.display.set_mode((SPACE_X, SPACE_Y))