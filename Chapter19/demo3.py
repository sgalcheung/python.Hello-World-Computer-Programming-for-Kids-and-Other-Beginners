import pygame, sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.5)
splat.play()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	if not pygame.mixer.music.get_busy():
		splat.play()
		pygame.time.delay(1000)
		sys.exit()
