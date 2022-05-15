import pygame

class Modelo(pygame.sprite.Sprite):
	def __init__(self, screen, path, location, dimensions):
		self.img_path = path
		self.x = location[0]
		self.y = location[1]
		self.width = dimensions[0]
		self.height = dimensions[1]
		self.screen = screen
	def dibujar(self, surface, location):
		self.screen.blit(surface, [ location[0], location[1] ])