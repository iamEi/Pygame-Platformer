import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
		player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

		self.jump_sfx = pygame.mixer.Sound('audio/jump.mp3')
		self.jump_sfx.set_volume(0.5)
		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom>=300:
			self.jump_sfx.play()
			self.gravity = -20

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def animate(self):
		if self.rect.bottom < 300:
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index > 2:
				self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]



	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animate()