#encoding=utf-8
import pygame, sys
from random import *

#-----------------------------ball subclass definition-----------------------------------
class MyBallClass(pygame.sprite.Sprite):
	def __init__(self, image_file, location, speed):
		pygame.sprite.Sprite.__init__(self)# 初始化动画精灵
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()# 得到定义图像边界的矩形
		self.rect.left, self.rect.top = location#设置球的初始位置
		self.speed = speed #增加speed属性

	def move(self):
		self.rect = self.rect.move(self.speed)
		if self.rect.left < 0 or self.rect.right > width:
			self.speed[0] = -self.speed[0] # speed[0]:x-speed
		if self.rect.top < 0 or self.rect.bottom > height:
			self.speed[1] = -self.speed[1] # speed[1]:y-speed

def animate(group):
	screen.fill([255,255,255])
	for ball in group:
		ball.move() # 先移动所有球
	for ball in group:
		group.remove(ball)# 从组删除精灵

		if pygame.sprite.spritecollide(ball, group, False):# 检查精灵与组之间的碰撞
			ball.speed[0] = -ball.speed[0]
			ball.speed[1] = -ball.speed[1]

		group.add(ball)

		ball.move()
		screen.blit(ball.image, ball.rect)
	pygame.display.flip()

#-------------------------------Main Program----------------------------------------
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "b_ball_rect.png"
clock = pygame.time.Clock()
group = pygame.sprite.Group() # 创建精灵组
for row in range (0, 3):
	for column in range (0, 3):
		location = [column * 180 + 10, row * 180 + 10]
		speed = [choice([-2, 2]), choice([-2, 2])]
		ball = MyBallClass(img_file, location, speed)# 创建一个球
		group.add(ball) # 将各个球增加到组

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			frame_rate = clock.get_fps() # 检查帧速率
			print "frame rate = ", frame_rate
			sys.exit()

	animate(group)
	clock.tick(30) # 设置为30f