import pygame
from modelos.Modelo import Modelo
class Fruta(Modelo):
	def __init__(self, screen, loc):
		super().__init__(screen, 'res/Apple.png', [loc[0], loc[1]], [32, 32] )
		self.pair = [0, 0]
		self.surface = pygame.image.load(self.img_path).convert_alpha()
	def obtener_elemento(self):
		self.surface.set_clip(pygame.Rect(self.pair[0], self.pair[1], 32, 32))
		self.img = self.surface.subsurface(self.surface.get_clip())
	
	def dibujar(self):
		super().dibujar(self.img, [self.x, self.y])