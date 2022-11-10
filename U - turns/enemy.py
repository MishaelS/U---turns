from config import WIDTH, HEIGHT
import pygame, random

# ----------------------------------------------------------------------------------------

class Enemy:
	def __init__(self, surface, pos, size):
		self.surf = pygame.Surface(size)
		self.rect = self.surf.get_rect(center=(pos))
		self.pos = pygame.math.Vector2(self.rect.center)
		self.surface = surface
		self.speedy = 200

	def hits(self):
		self.rect.centery = -random.randrange(16, 512, 256)
		self.rect.centerx = random.randrange(16, WIDTH - 16, 32)
		self.pos = pygame.math.Vector2(self.rect.center)

	def move(self, dt):
		self.pos.y += self.speedy * dt
		self.rect.centery = round(self.pos.y)
		if self.rect.centery >= HEIGHT + 64:
			self.hits()

	def draw(self):
		self.surface.blit(self.surf, self.rect)

	def update(self, dt):
		self.move(dt)
		self.draw()
