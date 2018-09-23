import pygame, sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.play()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()