import pygame
from modelos.Modelo import Modelo
class BloqueSuelo(Modelo):
	def __init__(self, screen, loc, suelo):
		super().__init__(screen, 'res/terran_16x16.png', [loc[0], loc[1]], [16, 16] )
		self.left_border = [192/2, 0] #23
		self.center_border = [224/2, 0] #24
		self.right_border = [256/2, 0] #25
		self.center_ground = [224/2, 16] #46
		self.surface = pygame.image.load(self.img_path).convert_alpha()
		self.tipoSuelo = suelo
	def obtener_elemento(self):
		if self.tipoSuelo is not None:
			if self.tipoSuelo == 'topleft':
				self.surface.set_clip(pygame.Rect(self.left_border[0], self.left_border[1], 16, 16))
			if self.tipoSuelo == 'topcenter':
				self.surface.set_clip(pygame.Rect(self.center_border[0], self.center_border[1], 16, 16))
			if self.tipoSuelo == 'topright':
				self.surface.set_clip(pygame.Rect(self.right_border[0], self.right_border[1], 16, 16))
			if self.tipoSuelo == 'midcenter':
				self.surface.set_clip(pygame.Rect(self.center_ground[0], self.center_ground[1], 16, 16))
			self.img = self.surface.subsurface(self.surface.get_clip())
			return True
		return False
	def dibujar(self):
		super().dibujar(self.img, [self.x, self.y])