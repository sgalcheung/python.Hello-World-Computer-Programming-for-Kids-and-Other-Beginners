# Listing_10-1.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Very simple skiing game.
# Avoid the trees and pick up flags to get points

import pygame, sys, random

# different images for the skier depending on his direction
skier_images = ["skier_down.png", "skier_right1.png", "skier_right2.png",
                 "skier_left2.png", "skier_left1.png"]

# class for the skier sprite
class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0
        
    def turn(self, direction): 
        # load new image and change speed when the skier turns
        self.angle = self.angle + direction
        if self.angle < -2:  self.angle = -2
        if self.angle >  2:  self.angle =  2 
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]
        return speed
    
    def move(self, speed):
        # move the skier right and left
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20:  self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620 
        
# class for obstacle sprites (trees and flags)
class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image_file = image_file        
        self.image = pygame.image.load(image_file)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False
                   
    def scroll(self, terrainPos):
        self.rect.centery = self.location[1] - terrainPos

# create one "screen" of terrain: 640 x 640
# use "blocks" of 64 x 64 pixels, so objects aren't too close together
def create_map(start, end):
    obstacles = pygame.sprite.Group()
    locations = []
    gates = pygame.sprite.Group()
    for i in range(10):                 # 10 obstacles per screen 
        row = random.randint(start, end)
        col = random.randint(0, 9)
        location  = [col * 64 + 20, row * 64 + 20] #center x, y for obstacle
        if not (location in locations):        # prevent 2 obstacles in the same place
            locations.append(location)          
            type = random.choice(["tree", "flag"])
            if type == "tree": img = "skier_tree.png"
            elif type == "flag":  img = "skier_flag.png"
            obstacle = ObstacleClass(img, location, type)
            obstacles.add(obstacle)
    return obstacles

# redraw the screen, including all sprites
def animate():
    screen.fill([255, 255, 255])
    pygame.display.update(obstacles.draw(screen)) 
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()    

def updateObstacleGroup(map0, map1):
    obstacles = pygame.sprite.Group()
    for ob in map0:  obstacles.add(ob)
    for ob in map1:  obstacles.add(ob)
    return obstacles

# initialize everything
pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0, 6]
map_position = 0
points = 0
map0 = create_map(20, 29)
map1 = create_map(10, 19)
activeMap = 0

# group for all obstacles to do collision detection
obstacles = updateObstacleGroup(map0, map1)

# font object for score
font = pygame.font.Font(None, 50)

# main Pygame event loop
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:          # check for key presses
            if event.key == pygame.K_LEFT:        # left arrow turns left
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:     #right arrow turns right
                speed = skier.turn(1)
    skier.move(speed)
    map_position += speed[1]                      # scroll the terrain
    
    # manage terrain maps, switch between them,
    # and create new terrain at the bottom
    if map_position >=640 and activeMap == 0:
        activeMap = 1
        map0 = create_map(20, 29)
        obstacles = updateObstacleGroup(map0, map1)
    if map_position >=1280 and activeMap == 1:                        
        activeMap = 0
        for ob in map0:
            ob.location[1] = ob.location[1] - 1280   # wrap around to top
        map_position = map_position - 1280           #
        map1 = create_map(10, 19)
        obstacles = updateObstacleGroup(map0, map1)
    
    for obstacle in obstacles:
        obstacle.scroll(map_position)
    
    # check for hitting trees or getting flags
    hit =  pygame.sprite.spritecollide(skier, obstacles, False)
    if hit:
        if hit[0].type == "tree" and not hit[0].passed:  #crashed into tree  
            points = points - 100
            skier.image = pygame.image.load("skier_crash.png")  # crash image
            animate()  
            pygame.time.delay(1000)
            skier.image = pygame.image.load("skier_down.png")  # resume skiing
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].type == "flag" and not hit[0].passed:   # got a flag
            points += 10
            obstacles.remove(hit[0])                    # remove the flag
    
    score_text = font.render("Score: " +str(points), 1, (0, 0, 0))
    animate()
    