import pygame
from modelos.Modelo import Modelo
class Fondo(Modelo):
	def __init__(self, screen):
		super().__init__(screen, 'res/pixel_adventure_map.png', [0, 0], [screen.get_size()[0], screen.get_size()[1]] )
		self.img = pygame.image.load(self.img_path).convert()