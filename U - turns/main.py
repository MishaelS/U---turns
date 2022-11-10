from player import Player
from enemy  import Enemy
from config import *
import pygame, sys
import random
import time

# ----------------------------------------------------------------------------------------

def updates(dt):
	for enemy in enemys_list:
		if enemy.rect.colliderect(player.rect):
			enemy.hits()

	for enemy in enemys_list:
		enemy.update(dt)

	player.update(dt)

# ----------------------------------------------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

previous_times = time.time()

enemys_list = []
for i in range(20):
	enemys_list.append(Enemy(screen, (random.randrange(16, WIDTH - 16, 48), -random.randrange(16, 512, 256)), (32, 32)))

player = Player(screen, (WIDTH/2, HEIGHT - 140), (48, 48))

# ----------------------------------------------------------------------------------------

def main():
	global previous_times

	running = True
	while running:
		dt = time.time() - previous_times
		previous_times = time.time()

		screen.fill(WHITE)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		updates(dt)

		pygame.display.update()
		clock.tick(FPS)

# ----------------------------------------------------------------------------------------

if __name__ == '__main__':
	main()
