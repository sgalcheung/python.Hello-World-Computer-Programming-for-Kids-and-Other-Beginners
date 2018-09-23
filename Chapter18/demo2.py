#encoding=utf-8
import pygame, sys

pygame.init()
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)
screen = pygame.display.set_mode([640,480])
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])
clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):
	def __init__(self, image_file, speed, location):
		pygame.sprite.Sprite.__init__(self)# 初始化动画精灵
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()# 得到定义图像边界的矩形
		self.rect.left, self.rect.top = location#设置球的初始位置
		self.speed = speed #增加speed属性

	def move(self):
		if self.rect.left <= screen.get_rect().left or \
				self.rect.right >= screen.get_rect().right:
			self.speed[0] = -self.speed[0]
		newpos = self.rect.move(self.speed)
		self.rect = newpos
		
my_ball = Ball('beach_ball.png', [10,0], [20, 20]) # 建立球的实例

held_down = False
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			held_down = True
		elif event.type == pygame.MOUSEBUTTONUP:
			held_down = False
		elif event.type == pygame.MOUSEMOTION:
			if held_down:
				my_ball.rect.center = event.pos


	clock.tick(30)
	screen.blit(background, (0, 0))
	my_ball.move()
	screen.blit(my_ball.image, my_ball.rect)
	pygame.display.flip()