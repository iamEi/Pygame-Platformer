import pygame

class Screen():
	def __init__(self):
		self.font = pygame.font.Font('font/Pixeltype.ttf',50)

		scaled_player = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
		self.scaled_player = pygame.transform.scale(scaled_player,(150,200))
		self.intro_rect = self.scaled_player.get_rect(center = (400,200))

		self.title = self.font.render('Pixel Runner', False, (111,196,169))
		self.title_rect = self.title.get_rect(center = (400,80))

		self.run = self.font.render('Press ENTER to Run!',False, (111,196,169 ))
		self.run_rect = self.run.get_rect(center = (400, 340))

		self.sky_surface = pygame.image.load('graphics/Sky.png').convert()
		self.ground_surface = pygame.image.load('graphics/ground.png').convert()


	def display_score(self,screen,start_time):
		#time elapsed in ms
		time = pygame.time.get_ticks()//500 - start_time
		score_surface = self.font.render(f'Score: {time}',False, (64,64,64))
		score_rect = score_surface.get_rect(center = (400,50))
		pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
		pygame.draw.rect(screen,'#c0e8ec',score_rect)
		screen.blit(score_surface,score_rect)

		return time

	def set_background(self,screen):
		screen.blit(self.sky_surface,(0,0))
		screen.blit(self.ground_surface,(0,300))


	def restart_screen(self,screen,score):
		screen.fill((94,129,162))
		screen.blit(self.title,self.title_rect)
		screen.blit(self.scaled_player,self.intro_rect)

		if not score:
			screen.blit(self.run,self.run_rect)
		else:
			total_score = self.font.render(f'Score: {score}', False, (111,196,169))
			total_score_rect = total_score.get_rect(center = (400, 340))
			screen.blit(total_score,total_score_rect)