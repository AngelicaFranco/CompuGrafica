# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

import pygame
import sys
import random

pygame.init()
ls_muros = pygame.sprite.Group()
ls_player = pygame.sprite.Group()
ls_todos = pygame.sprite.Group()
ls_enemigos = pygame.sprite.Group()
ls_pildoras = pygame.sprite.Group()
ls_estrellas = pygame.sprite.Group()
ls_bolas = pygame.sprite.Group()
ls_balas = pygame.sprite.Group()
ls_explosiones = pygame.sprite.Group()
ls_pausa = pygame.sprite.Group()
ls_emovi = pygame.sprite.Group()
ls_ebalas = pygame.sprite.Group()
ls_pistolas = pygame.sprite.Group()
sonidoNivel1 = pygame.mixer.Sound("Sonidos/Nivel1.ogg")
sonidoNivel2 = pygame.mixer.Sound("Sonidos/Nivel2.ogg")
sonidoNivel3 = pygame.mixer.Sound("Sonidos/Nivel3.ogg")
sonidoExplosion = pygame.mixer.Sound("Sonidos/Explosion.ogg")
sonidoGanar = pygame.mixer.Sound("Sonidos/Win.ogg")
sonidoPerder = pygame.mixer.Sound("Sonidos/GameOver.ogg")
sonidoCargando = pygame.mixer.Sound("Sonidos/Cargando.ogg")
pygame.mixer.music.set_volume(1)
ANCHO = 1020
ALTO = 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#----------------------------------------------------------------
#Funciones
def CrearNivel(nivel):
    x = 0
    y = 0
    iterlen = lambda it: sum(1 for _ in it)
    if(nivel == 1):
        archivo = open('Niveles/Nivel1.txt', 'r')
        lenlineas = iterlen(file('Niveles/Nivel1.txt'))
    if(nivel == 2):
        archivo = open('Niveles/Nivel2.txt', 'r')
        lenlineas = iterlen(file('Niveles/Nivel2.txt'))
    if(nivel == 3):
        archivo = open('Niveles/NivelBoss.txt', 'r')
        lenlineas = iterlen(file('Niveles/NivelBoss.txt'))
    for Fila in archivo:
        lencolumnas = len(Fila)
        for Columna in Fila:
            if Columna == 'X':
                m = Muro(x,y)
                ls_todos.add(m)
                ls_muros.add(m)
            if Columna == 'P':
                p = Pildora(x,y)
                ls_todos.add(p)
                ls_pildoras.add(p)
            if Columna == 'O':
                o = Estrella(x,y)
                ls_todos.add(o)
                ls_estrellas.add(o)
            if Columna == 'I':
                i = Bola(x,y)
                ls_todos.add(i)
                ls_bolas.add(i)
            if Columna == 'Q':
                e = Hongo(x,y)
                ls_todos.add(e)
                ls_enemigos.add(e)
            if Columna == 'W':
                e = LuiG(x,y)
                ls_todos.add(e)
                ls_enemigos.add(e)
            if Columna == 'E':
                e = Pistola(x,y)
                ls_todos.add(e)
                ls_pistolas.add(e)
            if Columna == 'R':
                e = Tortuga(x,y)
                ls_todos.add(e)
                ls_enemigos.add(e)
            if Columna == 'T':
                e = Yoshi(x,y)
                ls_todos.add(e)
                ls_enemigos.add(e)
                ls_emovi.add(e)
            x += 30
        y += 30
        x = 0
    return (lenlineas, lencolumnas)

def DirBala(jg, eg):
    if(jg.rect.x - eg.rect.x > 0):
        return 0
    else:
        return 1

def Distancia(jg, boss):
    if(abs(jg.rect.x - boss.rect.x) < 10):
        return True
    else:
        return False

def Intro(Pantalla):
    font=pygame.font.Font(None, 36)
    ver = True
    pag = 1
    while ver:
        for event in pygame.event.get():
           if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pag += 1
                if pag == 4:
                    ver = False

        if pag == 1:
            Pantalla.fill(BLANCO)
            texto = font.render("Warrior Cansado De Que Mario Le Ganara Las Batallas...", True, NEGRO)
            texto2 = font.render("Decidio Traer De Nuevos Universos A Nuevos Enemigos...", True, NEGRO)
            texto3 = font.render("Desafortunadamente para Warrior, Trajo a Megaman", True, NEGRO)
            Warrior = pygame.image.load('Images/WarriorPortada.png').convert_alpha()
            Portal = pygame.image.load('Images/PortalPortada.png').convert_alpha()
            Pantalla.blit(texto, (30,30))
            Pantalla.blit(texto2, (30,70))
            Pantalla.blit(texto3, (30, 110))
            Pantalla.blit(Warrior, (30, 200))
            Pantalla.blit(Portal, (600,180))

        if pag == 2:
            Pantalla.fill(BLANCO)
            texto = font.render("La Unica Forma De Que Megaman Vuelva A Su Universo Es...", True, NEGRO)
            texto2 = font.render("Derrotando A Warrior Y Su Ejercito De Subditos...", True, NEGRO)
            texto3 = font.render("Podras...Ayudarlo?", True, NEGRO)
            Megaman = pygame.image.load('Images/MegamanPortada.jpg').convert_alpha()
            Pantalla.blit(texto, (30,30))
            Pantalla.blit(texto2, (30,70))
            Pantalla.blit(texto3, (30,110))
            Pantalla.blit(Megaman, (500,150))

        if pag == 3:
            Pantalla.fill(BLANCO)
            texto = font.render("C O N T R O L", True, NEGRO)
            texto2 = font.render("Pulsa arriba para saltar", True, NEGRO)
            texto3 = font.render("Derecha para correr hacia adelante", True, NEGRO)
            texto4 = font.render("Izquierda para correr hacia atras", True, NEGRO)
            texto5 = font.render("Espacio para disparar", True, NEGRO)
            texto6 = font.render("P para Pausar juego", True, NEGRO)
            Pantalla.blit(texto, (30,30))
            Pantalla.blit(texto2, (30,120))
            Pantalla.blit(texto3, (520,120))
            Pantalla.blit(texto4, (30,340))
            Pantalla.blit(texto5, (520,340))
            Pantalla.blit(texto6, (400,400))

        pygame.display.flip()


def LimpiarNivel(jugador):
    ls_muros.empty()
    ls_todos.empty()
    ls_enemigos.empty()
    ls_pildoras.empty()
    ls_estrellas.empty()
    ls_balas.empty()
    ls_explosiones.empty()
    ls_todos.add(jugador)
    jugador.movex = 0
    jugador.movey = 0

def InicioJuego(Pantalla, reloj):
    sonidoCargando.play()
    Cargando = 0
    time = 1
    font = pygame.font.Font(None, 80)
    while(Cargando < 100):
        Pantalla.fill(NEGRO)
        texto = font.render("Cargando " + str(Cargando) + "%", True, BLANCO)
        Cargando += time
        time += random.randrange(2)
        Pantalla.blit(texto, (ANCHO/2-150 , ALTO/2))
        reloj.tick(10) 
        pygame.display.flip()
    sonidoCargando.stop()

def FinJuego(Pantalla, jugador, reloj):
    Pantalla.fill(BLANCO)
    font = pygame.font.Font(None, 100)
    font2 = pygame.font.Font(None, 50)
    font.set_bold(True)
    if jugador.vida <= 0:
        sonidoPerder.play()
        texto = font.render("Game Over.", True, NEGRO)
        Ganador = pygame.image.load('Images/WarriorGanador.png').convert_alpha()
    else:
        texto = font.render("You Win.", True, NEGRO)
        Ganador = pygame.image.load('Images/MegamanGanador.png').convert_alpha()
        sonidoGanar.play()
    texto2 = font2.render("Puntaje = " + str(jugador.puntaje), True, VERDE)
    Pantalla.blit(texto, (100, 100))
    Pantalla.blit(texto2, (ANCHO/2, 230))
    Pantalla.blit(Ganador, (ANCHO/2-40, 300))
    pygame.display.flip()
    Terminar = False
    aux = 0
    sonidoNivel1.stop()
    sonidoNivel2.stop()
    sonidoNivel3.stop()
    while Terminar == False:
        if aux == 200:
            Terminar = True
        else:
            aux += 1
        reloj.tick(30)

def PausarJuego(Pantalla):
    Pantalla.fill(NEGRO)
    font = pygame.font.Font(None, 160)
    font.set_bold(True)
    texto = font.render("Pausa", True, BLANCO)
    Pantalla.blit(texto, (ANCHO/2-100, ALTO/2-50))
    pygame.display.flip() 

#----------------------------------------------------------------
#clases
class Opcion:
    ver = False
    def __init__(self, texto, pos, valor, fuente, pantalla):
        self.texto = texto
        self.fuente = fuente
        self.valor = valor
        self.pos = pos
        self.setRect()
        self.dibujar(pantalla)

    def dibujar(self, pantalla):
        self.setRect()
        pantalla.blit(self.rend, self.rect)

    def setRend(self):
        self.rend = self.fuente.render(self.texto, True, self.getColor())

    def getColor(self):
        if(self.ver):
            return AZUL
        else:
            return BLANCO

    def setRect(self):
        self.setRend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

def RelRect(actor, camara):
    return pygame.Rect(actor.rect.x-camara.rect.x, actor.rect.y-camara.rect.y, actor.rect.w, actor.rect.h)

#CLASE PARA CENTRAR LA CaMARA EN EL JUGADOR
class Camara(object): 
    
    def __init__(self, pantalla, jugador, anchoNivel, largoNivel):
        self.jugador = jugador
        self.rect = pantalla.get_rect()
        self.rect.center = self.jugador.center
        self.mundo_rect = pygame.Rect(0, 0, anchoNivel, largoNivel)

    def update(self):
      if self.jugador.centerx > self.rect.centerx + 25:
          self.rect.centerx = self.jugador.centerx - 25
          
      if self.jugador.centerx < self.rect.centerx - 25:
          self.rect.centerx = self.jugador.centerx + 25

      if self.jugador.centery > self.rect.centery + 25:
          self.rect.centery = self.jugador.centery - 25

      if self.jugador.centery < self.rect.centery - 25:
          self.rect.centery = self.jugador.centery + 25
      self.rect.clamp_ip(self.mundo_rect)

    def dibujarSprites(self, pantalla, sprites):
        for s in sprites:
            if s.rect.colliderect(self.rect):
                pantalla.blit(s.image, RelRect(s, self))

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Jugador/D.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vida = 600
        self.movex = 0
        self.movey = 0
        self.win = False
        self.cant = 0
        self.nivel = 1
        self.puntaje = 0
        self.direccion = 0
        self.frame = 0
        self.contacto = False
        self.arriba = False
        self.salto = False
        self.saltar = 8
        self.pausa = False
        self.avanzarIzquierda = ['Jugador/I1.png' , 'Jugador/I3.png', 'Jugador/I4.png', 'Jugador/I5.png']
        self.avanzarDerecha = ['Jugador/D1.png' , 'Jugador/D3.png', 'Jugador/D4.png', 'Jugador/D5.png']
        self.frame = 0
        self.direccion = 0

    def masPuntaje1(self):
        self.puntaje += 100 
        self.puntaje += self.vida

    def masPuntaje2(self):
        self.puntaje += 200
        self.puntaje += self.vida


    def masPuntajeFinal(self):
        self.puntaje += 500
        self.puntaje += self.vida

    def menosPuntaje(self):
        self.puntaje -= 10

    def irArriba(self):
        self.arriba = True

    def noArriba(self):
        self.arriba = False

    def update(self):
        if not self.pausa:
            if self.direccion == 0:
                if self.movex != 0:
                    self.image = pygame.image.load(self.avanzarDerecha[self.frame/6]).convert_alpha()
                else:
                    self.image = pygame.image.load('Jugador/D.png').convert_alpha()
            else:
                if self.movex != 0:
                    self.image = pygame.image.load(self.avanzarIzquierda[self.frame/6]).convert_alpha()
                else:
                    self.image = pygame.image.load('Jugador/I.png').convert_alpha()

            if self.frame == 18:
                self.frame = 0
            else:
                self.frame += 1

            if self.arriba:
                if self.contacto:
                    self.salto = True
                    self.movey -= self.saltar

            self.rect.x += self.movex
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movex > 0:
                    self.rect.right = muro.rect.left
                if self.movex <0:
                    self.rect.left = muro.rect.right

            if not self.contacto:
                self.movey += 0.3
                if self.movey > 10:
                    self.movey = 10
                self.rect.top += self.movey

            if self.salto: 
                self.movey += 2
                self.rect.top += self.movey
                if self.contacto:
                    self.salto = False

            self.contacto = False
            self.rect.y += self.movey
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movey > 0:
                    self.rect.bottom = muro.rect.top
                    self.contacto = True
                    self.movey = 0
                if self.movey < 0:
                    self.rect.top = muro.rect.bottom
                    self.movey = 0

class Muro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/Muro.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class Pildora(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/Pildora.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        pass

class Estrella(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/Estrella.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class Bola(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/Bola.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


#CLASE PARA EL ENEMIGO 1 Y SUS COLISIONES
class Hongo(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.movey = 0
        self.movex = 0
        self.x = x
        self.pausa = False
        self.y = y
        self.contacto = False
        self.salto = False
        self.image = pygame.image.load('Enemigos/HongA.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.dano = 10
        self.avanzar = ['Enemigos/HongA.png', 'Enemigos/HongB.png']
        self.frame = 0
        self.direccion = "derecha"
        self.disparar = False
        
    def update(self):
        if not self.pausa:
            if self.direccion == "izquierda":
                self.movex = -5
                
            if self.direccion == "derecha":
                self.movex = +5

            if self.frame == 11:
                self.frame = 0
            else:
                self.frame += 1
            self.image = pygame.image.load(self.avanzar[self.frame/6]).convert_alpha()

            self.rect.x += self.movex
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movex > 0:
                    self.rect.right = muro.rect.left
                    self.direccion = "izquierda"
                if self.movex <0:
                    self.rect.left = muro.rect.right
                    self.direccion = "derecha"

            if not self.contacto:
                self.movey += 0.3
                if self.movey > 10:
                    self.movey = 10
                self.rect.top += self.movey

            if self.salto: 
                self.movey += 2
                self.rect.top += self.movey
                if self.contacto:
                    self.salto = False

            self.contacto = False
            self.rect.y += self.movey
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movey > 0:
                    self.rect.bottom = muro.rect.top
                    self.contacto = True
                    self.movey = 0
                if self.movey < 0:
                    self.rect.top = muro.rect.bottom
                    self.movey = 0

#CLASE PARA EL ENEMIGO 2 Y SUS COLISIONES
class LuiG(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.movey = 0
        self.movex = 0
        self.x = x
        self.y = y
        self.pausa = False
        self.ciclo = False
        self.contacto = False
        self.salto = False
        self.recarga = random.randrange(200, 400)
        self.disparar = False
        self.image = pygame.image.load('Enemigos/LuiGD1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.frame = 0
        self.direccion = "derecha"
        self.dano = 20
        self.disparar = False
        self.avanzarDerecha = ['Enemigos/LuiGD1.png', 'Enemigos/LuiGD2.png', 'Enemigos/LuiGD3.png', 'Enemigos/LuiGD4.png']
        self.avanzarIzquierda = ['Enemigos/LuiGI1.png', 'Enemigos/LuiGI2.png', 'Enemigos/LuiGI3.png', 'Enemigos/LuiGI4.png']

    def update(self):
        if not self.pausa:
            if self.direccion == "izquierda":
                self.movex = -5
                self.image = pygame.image.load(self.avanzarIzquierda[self.frame/6]).convert_alpha()
                
            if self.direccion == "derecha":
                self.movex = +5
                self.image = pygame.image.load(self.avanzarDerecha[self.frame/6]).convert_alpha()

            if self.frame == 23:
                self.frame = 0
            else:
                self.frame += 1

            self.rect.x += self.movex
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movex > 0:
                    self.rect.right = muro.rect.left
                    self.direccion = "izquierda"
                if self.movex <0:
                    self.rect.left = muro.rect.right
                    self.direccion = "derecha"

            if not self.contacto:
                self.movey += 0.3
                if self.movey > 10:
                    self.movey = 10
                self.rect.top += self.movey

            if self.salto: 
                self.movey += 2
                self.rect.top += self.movey
                if self.contacto:
                    self.salto = False

            self.contacto = False
            self.rect.y += self.movey
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movey > 0:
                    self.rect.bottom = muro.rect.top
                    self.contacto = True
                    self.movey = 0
                if self.movey < 0:
                    self.rect.top = muro.rect.bottom
                    self.movey = 0

# CLASE PARA EL ENEMIGO 3
class Pistola(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Enemigos/Pistola.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y-5
        self.dano = 0
        self.disparar = False
        self.recarga = 300

    def update(self):
        if self.recarga == 0:
            self.disparar = True
            self.recarga = 300
        else:
            self.recarga -= 1
            self.disparar = False

#CLASE PARA EL ENEMIGO 1 Y SUS COLISIONES
class Tortuga(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.movey = 0
        self.movex = 0
        self.pausa = False
        self.contacto = False
        self.salto = False
        self.disparar = False
        self.image = pygame.image.load('Enemigos/TortuD1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dano = 30
        self.direccion = "izquierda"
        self.disparar = False
        self.avanzarDerecha = ['Enemigos/TortuD1.png', 'Enemigos/TortuD2.png']
        self.avanzarIzquierda = ['Enemigos/TortuI1.png', 'Enemigos/TortuI2.png']
        self.frame = 0
        
    def update(self):
        if not self.pausa:
            if self.direccion == "izquierda":
                self.movex = -5
                self.image = pygame.image.load(self.avanzarIzquierda[self.frame/6]).convert_alpha()
                
            if self.direccion == "derecha":
                self.movex = +5
                self.image = pygame.image.load(self.avanzarDerecha[self.frame/6]).convert_alpha()

            if self.frame == 11:
                self.frame = 0
            else:
                self.frame += 1

            if self.contacto:
                self.salto = True
                self.movey -= 8

            self.rect.x += self.movex
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movex > 0:
                    self.rect.right = muro.rect.left
                    self.direccion = "izquierda"
                if self.movex <0:
                    self.rect.left = muro.rect.right
                    self.direccion = "derecha"

            if not self.contacto:
                self.movey += 0.3
                if self.movey > 10:
                    self.movey = 10
                self.rect.top += self.movey

            if self.salto: 
                self.movey += 2
                self.rect.top += self.movey
                if self.contacto:
                    self.salto = False

            self.contacto = False
            self.rect.y += self.movey
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movey > 0:
                    self.rect.bottom = muro.rect.top
                    self.contacto = True
                    self.movey = 0
                if self.movey < 0:
                    self.rect.top = muro.rect.bottom
                    self.movey = 0

# CLASE PARA EL ENEMIGO 5
class Yoshi(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Enemigos/YoshiD1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.pausa = False
        self.rect.x = x
        self.rect.y = y - 25
        self.velocidad = 10
        self.movey = 0
        self.movex = 0
        self.arriba = False
        self.contacto = False
        self.salto = False
        self.derecha = False
        self.mover = False
        self.izquierda = False
        self.recarga = random.randrange(100,200)
        self.disparar = False
        self.direccion = 0
        self.duracion = 60
        self.dano = 60
        self.disparar = False
        self.avanzarDerecha = ['Enemigos/YoshiD1.png', 'Enemigos/YoshiD2.png', 'Enemigos/YoshiD3.png']
        self.avanzarIzquierda = ['Enemigos/YoshiI1.png', 'Enemigos/YoshiI2.png', 'Enemigos/YoshiI3.png']
        self.frame = 0 


    def movimiento(self, jg):
        if jg.rect.x == self.rect.x:
            self.derecha = False
            self.izquierda = False

        if jg.rect.bottom >= self.rect.bottom:
            self.arriba = False
        else:
            self.arriba = True

        if jg.rect.x > self.rect.x:
            self.derecha = True
            self.izquierda = False

        if jg.rect.x < self.rect.x:
            self.izquierda = True
            self.derecha = False

    def update(self):
        if not self.pausa:
            if self.arriba:
                if self.contacto:
                    self.salto = True
                    self.movey -= 8

            if self.derecha:
                self.movex = 3
                self.image = pygame.image.load(self.avanzarDerecha[self.frame/6]).convert_alpha()

            if self.izquierda:
                self.movex = -3
                self.image = pygame.image.load(self.avanzarIzquierda[self.frame/6]).convert_alpha()
                
            if self.frame == 14:
                self.frame = 0
            else:
                self.frame += 1

            self.rect.x += self.movex
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movex > 0:
                    self.rect.right = muro.rect.left
                    self.direccion = 1
                if self.movex <0:
                    self.rect.left = muro.rect.right
                    self.direccion = 0

            if not self.contacto:
                self.movey += 0.3
                if self.movey > 10:
                    self.movey = 10
                self.rect.top += self.movey

            if self.salto: 
                self.movey += 2
                self.rect.top += self.movey
                if self.contacto:
                    self.salto = False

            self.contacto = False
            self.rect.y += self.movey
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movey > 0:
                    self.rect.bottom = muro.rect.top
                    self.contacto = True
                    self.movey = 0
                if self.movey < 0:
                    self.rect.top = muro.rect.bottom
                    self.movey = 0

class miniExplosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        sonidoExplosion.play()
        self.image = pygame.image.load("Images/me1.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.contador = 0
        self.avanzar = ["Images/me1.png", "Images/me1.png",
                        "Images/me2.png", "Images/me2.png", "Images/me2.png",
                        "Images/me3.png", "Images/me3.png", "Images/me3.png",
                        "Images/me4.png", "Images/me4.png", "Images/me4.png",
                        "Images/me5.png", "Images/me5.png", "Images/me5.png"]

    def update(self):
        if self.contador <= 13:
            self.image = pygame.image.load(self.avanzar[self.contador])
            self.contador += 1

class BalaEnemigo(pygame.sprite.Sprite):
    def __init__(self, pos, tipo):
        pygame.sprite.Sprite.__init__(self)
        self.direccion = tipo
        self.balas = ["Enemigos/BalaD.png", "Enemigos/BalaI.png"]
        self.image = pygame.image.load(self.balas[self.direccion]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]+3
        self.rect.y = pos[1]+10
        self.contador = 1
    
    def update(self):
        if self.direccion == 0:
            self.rect.x += 8
        else:
            self.rect.x -= 8

class Bala(pygame.sprite.Sprite):
    def __init__(self, pos, tipo):
        pygame.sprite.Sprite.__init__(self)
        self.direccion = tipo
        self.balas = ["Jugador/BD.png", "Jugador/BI.png"]
        self.image = pygame.image.load(self.balas[self.direccion]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]+10
        self.rect.y = pos[1]+10
        self.contador = 1
    
    def update(self):
        if self.direccion == 0:
            self.rect.x += 8
        else:
            self.rect.x -= 8

class Warrior(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Enemigos/WarriorD1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.pausa = False
        self.rect.x = x
        self.rect.y = y - 25
        self.velocidad = 10
        self.movey = 0
        self.movex = 0
        self.arriba = False
        self.contacto = False
        self.salto = False
        self.derecha = False
        self.mover = False
        self.izquierda = False
        self.recarga = random.randrange(100,200)
        self.disparar = False
        self.direccion = 0
        self.duracion = 60
        self.dano = 12
        self.vida = 300
        self.disparar = False
        self.avanzarDerecha = ['Enemigos/WarriorD1.png', 'Enemigos/WarriorD2.png', 'Enemigos/WarriorD3.png']
        self.avanzarIzquierda = ['Enemigos/WarriorI1.png', 'Enemigos/WarriorI2.png', 'Enemigos/WarriorI3.png']
        self.poderDerecha = ['Enemigos/WarriorPD1.png', 'Enemigos/WarriorPD2.png']
        self.poderIzquierda = ['Enemigos/WarriorPI1.png', 'Enemigos/WarriorPI2.png']
        self.frame = 0 
        self.poder = False
        self.poderContador = 0
        self.direccion = 0


    def movimiento(self, jg):
        if not self.poder and self.poderContador < 0:
            if jg.rect.x == self.rect.x:
                self.derecha = False
                self.izquierda = False

            if jg.rect.bottom >= self.rect.bottom:
                self.arriba = False
            else:
                self.arriba = True

            if jg.rect.x > self.rect.x:
                self.derecha = True
                self.izquierda = False

            if jg.rect.x < self.rect.x:
                self.izquierda = True
                self.derecha = False
        else:
            if self.direccion == 0:
                self.rect.x += 2
            else:
                self.rect.x -= 2


    def update(self):
        if not self.pausa:
            if self.arriba:
                if self.contacto:
                    self.salto = True
                    self.movey -= 8

            if self.derecha:
                self.movex = 3
                self.image = pygame.image.load(self.avanzarDerecha[self.frame/6]).convert_alpha()

            if self.izquierda:
                self.movex = -3
                self.image = pygame.image.load(self.avanzarIzquierda[self.frame/6]).convert_alpha()

            if self.poder and self.poderContador < 0:
                self.poderContador = 200
                if self.derecha:
                    self.direccion = 0
                else:
                    self.direccion = 1

            if self.poderContador >= 0:
                self.poderContador -= 1
                if self.direccion == 0:
                    self.image = pygame.image.load(self.poderDerecha[self.poderContador/100])
                else:
                    self.image = pygame.image.load(self.poderIzquierda[self.poderContador/100])
                
            if self.frame == 14:
                self.frame = 0
            else:
                self.frame += 1

            self.rect.x += self.movex
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movex > 0:
                    self.rect.right = muro.rect.left
                    self.direccion = 1
                if self.movex <0:
                    self.rect.left = muro.rect.right
                    self.direccion = 0

            if not self.contacto:
                self.movey += 0.3
                if self.movey > 10:
                    self.movey = 10
                self.rect.top += self.movey

            if self.salto: 
                self.movey += 2
                self.rect.top += self.movey
                if self.contacto:
                    self.salto = False

            self.contacto = False
            self.rect.y += self.movey
            col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
            for muro in col_muro:
                if self.movey > 0:
                    self.rect.bottom = muro.rect.top
                    self.contacto = True
                    self.movey = 0
                if self.movey < 0:
                    self.rect.top = muro.rect.bottom
                    self.movey = 0