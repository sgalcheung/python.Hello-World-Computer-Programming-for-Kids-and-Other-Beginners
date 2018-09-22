#coding=utf-8
import pygame ,sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])# 用白色背景填充窗口
pygame.draw.circle(screen, [255,0,0],[100,100],30,0)#画一个圈
pygame.display.flip()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
