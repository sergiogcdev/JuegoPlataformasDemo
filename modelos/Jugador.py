import pygame
from modelos.Modelo import Modelo
class Jugador(Modelo):
	def __init__(self, screen):
		super().__init__(screen, 'res/char_run_32x32.png', [20, 200], [32, 32] )
		self.sprite_length = 11
		self.actual_mov = 0
		self.rect = pygame.Rect( self.x, self.y, 32, 32)
		self.direccion = 0
		self.surface = pygame.image.load(self.img_path).convert_alpha()
		self.enSuelo = False
		self.enPlataforma = False
		self.enCaida = True
		self.saltando = False
		self.surface.set_clip(pygame.Rect(32 * self.actual_mov, 0, 32, 32))
		self.img = self.surface.subsurface(self.surface.get_clip())
		self.tiempoSalto = -5
		self.maxSalto = 30
	def moverX(self, direccion):
		self.direccion = direccion
		self.x = self.x + (self.direccion * 3)
		self.rect = pygame.Rect( self.x, self.y, 32, 32)
		if self.actual_mov < self.sprite_length:
			self.actual_mov += 1
		else:
			self.actual_mov = 0
		self.surface.set_clip(pygame.Rect(32 * self.actual_mov, 0, 32, 32))
		self.img = self.surface.subsurface(self.surface.get_clip())
		if self.direccion < 0:
			self.img = pygame.transform.flip(self.img, True, False)
	def actualizarTiempoSalto(self):
		if(self.tiempoSalto == -(self.maxSalto*2)):
			self.enCaida = True
			self.saltando = False
			self.tiempoSalto = -10
	def saltar(self, direccion):
		if self.saltando:
			if(self.tiempoSalto < self.maxSalto):
				self.tiempoSalto -= 5
			self.y = self.y + direccion
			self.rect = pygame.Rect( self.x, self.y, 32, 32)
			self.enSuelo = False
	def efecto_gravitatorio(self, gravedad):
		self.y = self.y + gravedad
		self.rect = pygame.Rect( self.x, self.y, 32, 32)
	def controlar_colision_suelo(self, recta_modelo):
		if self.rect.colliderect(recta_modelo):
			self.enSuelo = True
			self.saltando = False
			self.enCaida = False
			self.enPlataforma = False
			return True
		return False
	def controlar_colision_plataforma(self, r):
		if self.rect.collidepoint(r.centerx, r.top):
			if self.rect.bottom -5 <= r.top:
				self.enSuelo = False
				self.enPlataforma = True
				self.enCaida = False
				return True
		return False
	def colisiona_fruta(self, lista_frutas):
		for f in lista_frutas:
		    if self.rect.colliderect(f):
		        return f
		return None
	# if(self.y + 32 >= recta_modelo.top and self.rect.colliderect(recta_modelo)):
	"""
	if alto_bloque == 16:
		print('Colisiona con plataforma')
		print('Plataforma', recta_modelo)
		print('Jugador', self.rect)
	"""
"""
	def controlar_colision_x(self, recta_modelo):
		if(self.rect.colliderect(recta_modelo)):
			if(self.direccion == -1 and self.x - 32 < recta_modelo.left):
				self.x += 5
			if(self.direccion == 1 and self.x >= recta_modelo.right):
				self.x -= 5
"""
