import pygame
from sys import exit
from random import randint
from player import Player
from enemies import Enemies
from screen import Screen

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf',50)
start_time = 0
score = 0
running = False

#Adding Sprites
player = pygame.sprite.GroupSingle()
player.add(Player())
enemy = pygame.sprite.Group()

displays = Screen()

#frequency of enemies
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer,1200)

def collision_check():
	if pygame.sprite.spritecollide(player.sprite,enemy,True):
		enemy.empty()
		return False
	return True

#music
bg_sound = pygame.mixer.Sound('audio/music.wav')
bg_sound.set_volume(0.8)
bg_sound.play(loops = -1)


#RUNNING GAME
while True:
	for event in pygame.event.get():
		#exit
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if running:
			#spawn enemies
			if event.type == enemy_timer:
				if randint(0,1): enemy.add(Enemies('fly'))
				else: enemy.add(Enemies('snail'))

		else:
			#restart
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				running = True
				start_time = pygame.time.get_ticks()//500

	if running:
		displays.set_background(screen)
		score = displays.display_score(screen,start_time)

		player.draw(screen)
		player.update()

		enemy.draw(screen)
		enemy.update()

		running = collision_check()
	else:
		displays.restart_screen(screen,score)

	pygame.display.update()
	clock.tick(60)