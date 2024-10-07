import pygame
import sys
from modelos.Fondo import Fondo
from modelos.Jugador import Jugador
from modelos.Mapa import Mapa

pygame.init()

screen = pygame.display.set_mode((1280, 960))
map_surface = pygame.Surface((screen.get_size()[0], screen.get_size()[1]), pygame.SRCALPHA)
empty_surface = pygame.Surface((32, 32), pygame.SRCALPHA)
empty_surface.fill((0, 204, 102))
fondo = Fondo(screen)
mapa = Mapa('res/pixel_adventure_map.json', [screen.get_size()[0], screen.get_size()[1]], map_surface)
mapa.establecer_capas()
map_surface.fill((0, 204, 102))
mapa.dibujar_capa_suelo()
mapa.dibujar_capa_frutas()
mapa.dibujar_capa_plataformas()
# fondo.dibujar(fondo.img, [0, 0])
jugador = Jugador(screen)
col_points = None
aux_col_points = None

while 1:

    jugador.enPlataforma = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if jugador.enCaida == False:
                    jugador.saltando = True

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        jugador.moverX(1)
    if pressed_keys[pygame.K_LEFT]:
        jugador.moverX(-1)


    jugador.saltar(-20)
    jugador.actualizarTiempoSalto()

    for r in mapa.col_rects:
        jugador.controlar_colision_suelo(r)

    counter = 0
    for r in mapa.col_rects_platform:
        jugador.controlar_colision_plataforma(r)
        counter += 1

    colision_rect = jugador.colisiona_fruta(mapa.col_rects_fruits)
    if colision_rect is not None:
        mapa.controlar_desaparicion_frutas(colision_rect, empty_surface)

    if jugador.enSuelo == False and jugador.enPlataforma == False:
        jugador.efecto_gravitatorio(8)

    screen.blit(map_surface, [0, 0])

    jugador.dibujar(jugador.img, [jugador.x, jugador.y])

    pygame.display.update()
    pygame.time.delay(58)
