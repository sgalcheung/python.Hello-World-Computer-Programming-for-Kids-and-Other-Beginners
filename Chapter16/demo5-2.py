#ecoding=utf-8
import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
screen.blit(my_ball, [x, y])
pygame.display.flip()
for looper in range (1, 200):
	pygame.time.delay(20)
	pygame.draw.rect(screen, [255,255,255], [x,y,90,90], 0)# 擦掉前一个位置
	x = x + 5
	screen.blit(my_ball,[x,y])
	pygame.display.flip()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()