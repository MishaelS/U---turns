from config import WIDTH, HEIGHT
import pygame

# ----------------------------------------------------------------------------------------

class Player:
	def __init__(self, surface, pos, size):
		self.surf = pygame.Surface(size)
		self.rect = self.surf.get_rect(center=(pos))
		self.pos = pygame.math.Vector2(self.rect.center)
		self.surface = surface
		self.speedx = 200

	def move(self, dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d] and self.rect.right <= WIDTH:
			self.pos.x += self.speedx * dt
		elif keys[pygame.K_a] and self.rect.left >= 0:
			self.pos.x -= self.speedx * dt

		self.rect.centerx = round(self.pos.x)

	def draw(self):
		self.surface.blit(self.surf, self.rect)

	def update(self, dt):
		self.move(dt)
		self.draw()
