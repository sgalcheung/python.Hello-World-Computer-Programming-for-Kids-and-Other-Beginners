#ecoding=utf-8
import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
x_speed = 10

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	pygame.time.delay(20)
	pygame.draw.rect(screen, [255,255,255], [x,y,90,90], 0)# 擦掉前一个位置
	x = x + x_speed
	if x > screen.get_width() - 90 or x < 0:# 当球碰到窗口的任意一边，改变方向
		x_speed = -x_speed
	screen.blit(my_ball, [x, y])# 块移，将一个图像从一个地方复制到另一个地方
	pygame.display.flip()