# -*- coding: cp1252 -*-
from Libreria import *

def Juego(Pantalla):
    pygame.mouse.set_visible(False)
    reloj = pygame.time.Clock()
    Fondo = pygame.image.load('Images/Fondo.png').convert()
    font = pygame.font.Font(None, 20)
    jugador = Jugador(30,0)
    ls_todos.add(jugador)
    ls_pausa.add(jugador)
    ls_player.add(jugador)
    Intro(Pantalla)
    LimpiarNivel(jugador)
    InicioJuego(Pantalla, reloj)
    tamano = CrearNivel(jugador.nivel)
    camara = Camara(Pantalla, jugador.rect, tamano[1]*30, tamano[0]*30)
    sonidoNivel1.play(-1)
    Pantalla.blit(Fondo, (0,0))
    Pausa = False
    while jugador.win == False and jugador.vida > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                b = Bala(jugador.rect, jugador.direccion)
                ls_balas.add(b)
                ls_todos.add(b)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            jugador.movex = -5
            jugador.direccion = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            jugador.movex = 5
            jugador.direccion = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            jugador.irArriba()
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            jugador.movex = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            jugador.movex = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            jugador.noArriba()
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            jugador.movex = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            jugador.movex = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            if Pausa:
                Pausa = False
                for s in ls_pausa:
                    s.pausa = False
            else:
                Pausa = True
                for s in ls_pausa:
                    s.pausa = True

        col_pil = pygame.sprite.spritecollide(jugador, ls_pildoras, True)
        for p in col_pil:
            if jugador.vida < 600:
                jugador.vida = 600
                ls_pildoras.remove(p)
                ls_todos.remove(p)

        for ex in ls_explosiones:
            if ex.contador == 13:
                ls_todos.remove(ex)
                ls_explosiones.remove(ex)

        col_bala = pygame.sprite.spritecollide(jugador, ls_ebalas, True)
        for bala in col_bala:
            jugador.vida -= 40
            ex = miniExplosion(bala.rect)
            ls_todos.add(ex)
            ls_explosiones.add(ex)
            ls_todos.remove(bala)
            ls_ebalas.remove(bala)
            jugador.menosPuntaje()

        col_be = pygame.sprite.groupcollide(ls_balas, ls_enemigos, True, True)
        for e in col_be:
            jugador.puntaje += 70
            ex = miniExplosion(e.rect)
            ls_explosiones.add(ex)
            ls_todos.add(ex)
            ls_todos.remove(e)
            ls_balas.remove(b)
            ls_enemigos.remove(e)

        col_be = pygame.sprite.groupcollide(ls_balas, ls_pistolas, False, False)
        for e in col_be:
            ex = miniExplosion(e.rect)
            ls_explosiones.add(ex)
            ls_todos.add(ex)
            ls_todos.remove(b)
            ls_balas.remove(b)

        col_entrebal =pygame.sprite.groupcollide(ls_balas, ls_ebalas, True, True)
        for cb in col_entrebal:
            ex = miniExplosion(cb.rect)
            ls_explosiones.add(ex)
            ls_todos.add(ex)

        col_bm = pygame.sprite.groupcollide(ls_balas, ls_muros, True, False)
        for bm in col_bm:
            ls_balas.remove(bm)
            ls_todos.remove(bm)

        col_bm = pygame.sprite.groupcollide(ls_balas, ls_muros, True, False)
        for bm in col_bm:
            ls_ebalas.remove(bm)
            ls_todos.remove(bm)

        col_ene = pygame.sprite.spritecollide(jugador, ls_enemigos, False)
        for e in col_ene:
            jugador.vida -= e.dano

        col_estrella = pygame.sprite.spritecollide(jugador, ls_estrellas, True)
        for es in col_estrella:
            jugador.cant += 1

        col_bola = pygame.sprite.spritecollide(jugador, ls_bolas, True)
        for bola in col_bola:
            ls_bolas.remove(bola)
            jugador.rect.x = 30
            jugador.rect.y = 30

        for e in ls_enemigos:
            if e.disparar:
                b = BalaEnemigo(e.rect, DirBala(jugador, e))
                ls_todos.add(b)
                ls_ebalas.add(b)

        for e in ls_emovi:
            e.movimiento(jugador)

        for ex in ls_explosiones:
            if ex.contador == 13:
                ls_explosiones.remove(ex)
                todos.remove(ex)

        if jugador.nivel == 3:
            Boss.movimiento(jugador)
            Boss.poder = Distancia(jugador, Boss)
            if Boss.vida > 0:
                colbb = pygame.sprite.spritecollide(Boss, ls_balas, True)
                for b in colbb:
                    ex = miniExplosion(b.rect)
                    ls_explosiones.add(ex)
                    ls_todos.add(ex)
                    Boss.vida -= 40

                if pygame.sprite.collide_mask(jugador, Boss):
                    if Boss.poder == 1:
                        jugador.vida -= 20
                        if jugador.rect.x > Boss.rect.x:
                            jugador.rect.x += 40
                        else:
                            jugador.irArriba()
                            if jugador.rect.x < 40:
                                jugador.rect.x = 30
                            else:
                                jugador.rect.x -= 50
            else:
                jugador.win = True
                sonidoNivel3.stop()
                jugador.masPuntajeFinal()
            
        if jugador.cant ==1 and jugador.nivel == 1:
            jugador.nivel = 2
            sonidoNivel1.stop()
            jugador.masPuntaje1()
            LimpiarNivel(jugador)
            InicioJuego(Pantalla, reloj)
            tamano = CrearNivel(jugador.nivel)
            camara = Camara(Pantalla, jugador.rect, tamano[1]*30, tamano[0]*30)
            sonidoNivel2.play(-1)
            jugador.cant = 0      
            jugador.rect.x = 30
            jugador.rect.y = 30

        if jugador.cant == 1 and jugador.nivel == 2:
            jugador.nivel = 3
            sonidoNivel2.stop()
            jugador.masPuntaje2()
            LimpiarNivel(jugador)
            InicioJuego(Pantalla, reloj)
            tamano = CrearNivel(jugador.nivel)
            camara = Camara(Pantalla, jugador.rect, tamano[1]*30, tamano[0]*30)
            sonidoNivel3.play(-1)
            jugador.cant = 0
            jugador.rect.x = 30
            jugador.rect.y = 30
            Boss = Warrior(180,180)
            ls_pausa.add(Boss)
            ls_todos.add(Boss)

        if jugador.nivel == 3 and (jugador.rect.x < 0 or jugador.rect.x > 1020 or jugador.rect.y < 0 or jugador.rect.y > 600):
            jugador.rect.x = 600
            jugador.rect.y = 300

        if Pausa:
            PausarJuego(Pantalla)
        else:
            Pantalla.blit(Fondo, (0,0))
            ls_todos.update()
            camara.update()
            camara.dibujarSprites(Pantalla, ls_todos)
            texto = font.render(str((jugador.vida)/6), True, VERDE)
            Pantalla.blit(texto,(30, 0))
            pygame.display.flip()
            reloj.tick(60)

    FinJuego(Pantalla, jugador, reloj)
    pygame.mouse.set_visible(True)