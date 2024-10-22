import pygame
from modelos.Modelo import Modelo


class Jugador(Modelo):
	def __init__(self, screen):
		super().__init__(screen, 'res/char_run_32x32.png', [20, 200], [32, 32])
		self.sprite_length = 11
		self.actual_mov = 0
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
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
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
		if self.actual_mov < self.sprite_length:
			self.actual_mov += 1
		else:
			self.actual_mov = 0
		self.surface.set_clip(pygame.Rect(32 * self.actual_mov, 0, 32, 32))
		self.img = self.surface.subsurface(self.surface.get_clip())
		if self.direccion < 0:
			self.img = pygame.transform.flip(self.img, True, False)

	def actualizarTiempoSalto(self):
		if (self.tiempoSalto == -(self.maxSalto*2)):
			self.enCaida = True
			self.saltando = False
			self.tiempoSalto = -10

	def saltar(self, direccion):
		if self.saltando:
			if (self.tiempoSalto < self.maxSalto):
				self.tiempoSalto -= 5
			self.y = self.y + direccion
			self.rect = pygame.Rect(self.x, self.y, 32, 32)
			self.enSuelo = False

	def efecto_gravitatorio(self, gravedad):
		self.y = self.y + gravedad
		self.rect = pygame.Rect(self.x, self.y, 32, 32)

	def colisiona_suelo(self, lista_suelo):
	    for suelo_rect in lista_suelo:
		    if self.rect.colliderect(suelo_rect):
			    self.enSuelo = True
			    self.saltando = False
			    self.enCaida = False
			    self.enPlataforma = False
			    break
	def colisiona_plataforma(self, lista_plataformas):
	    for plataforma in lista_plataformas:
		    if self.rect.collidepoint(plataforma.centerx, plataforma.top):
			    if self.rect.bottom -5 <= plataforma.top:
				    self.enSuelo = False
				    self.enPlataforma = True
				    self.enCaida = False
				    break
	def colisiona_fruta(self, lista_frutas):
		for f in lista_frutas:
		    if self.rect.colliderect(f):
		        return f
		return None
