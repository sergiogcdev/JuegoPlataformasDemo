import pygame
import json
from modelos.Modelo import Modelo
from modelos.BloqueSuelo import BloqueSuelo
from modelos.BloquePlataforma import BloquePlataforma
from modelos.Fruta import Fruta
from modelos.PixelVacio import PixelVacio
class Mapa(Modelo):
	def __init__(self, map_path, dimensions, screen):

		self.screen = screen

		self.dimensions = dimensions

		self.nGround = []
		self.nPlatform = []
		self.nFruit = []
		self.nSky = []

		self.patron_h = 80
		self.patron_v = 60

		with open(map_path) as f:
		   self.data = json.load(f)

		for key, value in self.data.items():
			if(key == "layers"):
				self.layers = value

		for i in range(4):
			for key, value in self.layers[i].items():
				if key == 'name' and value == 'Suelo':
					self.data_suelo = self.layers[i]
				if key == 'name' and value == 'Plataformas':
					self.data_platform = self.layers[i]
				if key == 'name' and value == 'Frutas':
					self.data_frutas = self.layers[i]
				if key == 'name' and value == 'Cielo':
					self.data_cielo = self.layers[i]
				

	def establecer_capas(self):
		limit = self.patron_h * self.patron_v
		self.col_rects = []
		self.col_rects_platform = []
		self.col_sky = []
		self.col_rects_fruits = []
		# self.col_rects_fruits_aux = []
		self.capa_vacia = []
		for i in range(limit):
			axis_x = int(i/self.patron_h)
			axis_y = i%self.patron_h
			if self.data_suelo['data'][i] != 0:
				self.col_rects.append(pygame.Rect((16 * axis_y), 16 * axis_x, 16, 16))
				self.nGround.append(self.data_suelo['data'][i])
			if self.data_platform['data'][i] != 0:
				self.col_rects_platform.append(pygame.Rect((16 * axis_y), 16 * axis_x, 28, 24))
				self.nPlatform.append(self.data_platform['data'][i])
			if self.data_frutas['data'][i] != 0:
				self.col_rects_fruits.append(pygame.Rect((16 * axis_y), 16 * axis_x, 16, 16))
				self.nFruit.append(self.data_frutas['data'][i])
			if self.data_cielo['data'][i] != 0:
				self.nSky.append(self.data_cielo['data'][i])
				self.col_sky.append(pygame.Rect((16 * axis_y), 16 * axis_x, 16, 16))

	def dibujar_capa_suelo(self):
		cont = 0
		for r in self.col_rects:
			tipoSuelo = None
			if self.nGround[cont] == 23:
				tipoSuelo = 'topleft'
			if self.nGround[cont] == 24:
				tipoSuelo = 'topcenter'
			if self.nGround[cont] == 25:
				tipoSuelo = 'topright'
			if self.nGround[cont] == 46:
				tipoSuelo = 'midcenter'
			block = BloqueSuelo(self.screen, [r.left, r.top], tipoSuelo)
			if block.obtener_elemento():
				block.dibujar()
			cont += 1

	def dibujar_capa_plataformas(self):
		for r in self.col_rects_platform:
			block = BloquePlataforma(self.screen, [r.left, r.top])
			block.obtener_elemento()
			block.dibujar()

	def dibujar_capa_frutas(self):
		for r in self.col_rects_fruits:
			block = Fruta(self.screen, [r.left, r.top])
			block.obtener_elemento()
			block.dibujar()


	def controlar_desaparicion_frutas(self, r, empty_surface, map_surface):
	    block = PixelVacio(empty_surface, [r.left, r.top])
	    block.obtener_elemento()
	    empty_surface.fill((0, 204, 102))
	    map_surface.blit(empty_surface, [block.x, block.y])
	    self.dibujar_capa_plataformas()
