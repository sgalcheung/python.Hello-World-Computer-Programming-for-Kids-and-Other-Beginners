import pygame, sys , random

pygame.init();
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range (100):
	width = random.randint(0, 250)
	height = random.randint(0, 100)
	top = random.randint(0,400)
	left = random.randint(0, 500)
	pygame.draw.rect(screen, [0,0,0], [left, top, width, height], 1)
	pygame.display.flip()
	pygame.time.delay(30)