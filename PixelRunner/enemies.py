from random import randint
import pygame

class Enemies(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()

		if type=='snail':
			snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
			snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
			self.frames = [snail_1,snail_2]
			self.frame_index = 0
			ypos = 300
		elif type=='fly':
			fly_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
			fly_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
			self.frames = [fly_1,fly_2]
			self.frame_index = 0
			ypos = 210		

		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1300),ypos))

	def animate(self):
		self.frame_index += 0.1
		if self.frame_index > 2:
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def move(self):
		self.rect.x -= 5

	def destroy(self):
		if self.rect.x <= -100:
			self.kill()

	def update(self):
		self.animate()
		self.move()
		self.destroy()