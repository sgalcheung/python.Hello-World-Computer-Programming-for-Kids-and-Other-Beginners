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
pygame.time.set_timer(pygame.USEREVENT, 1000) # 创建一个定时器，1s执行一次
direction = 1

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.USEREVENT:
			my_ball.rect.centery = my_ball.rect.centery + (30*direction)
			if my_ball.rect.top <= 0 or \
			my_ball.rect.bottom >= screen.get_rect().bottom:
				direction = -direction


	clock.tick(30)
	screen.blit(background, (0, 0))
	my_ball.move()
	screen.blit(my_ball.image, my_ball.rect)
	pygame.display.flip()