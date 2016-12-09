from Juego import *

def main():
	Pantalla = pygame.display.set_mode([ANCHO, ALTO])
	terminar = False
	Menu = pygame.font.Font(None, 60)
	Menu.set_bold(True)
	MenuT = pygame.font.Font(None, 160)
	Title = MenuT.render("Megaman", True, BLANCO)
	Title2 = MenuT.render("vs", True, BLANCO)
	Title3 = MenuT.render("Warrior", True, BLANCO)
	Menu = [Opcion("Jugar", (440, 350), 0, Menu, Pantalla), Opcion("Salir", (448, 450), 1, Menu, Pantalla)]
	
	while not terminar:
	    for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                    terminar = True
	    Pantalla.fill((0, 0, 0))
	    Pantalla.blit(Title, [250, 30])
	    Pantalla.blit(Title2, [460, 100])
	    Pantalla.blit(Title3, [310, 170])
	    
	    for opcion in Menu:
	            if opcion.rect.collidepoint(pygame.mouse.get_pos()):
	                    opcion.ver=True
	                    if event.type == pygame.MOUSEBUTTONDOWN:
	                            if(opcion.valor == 0):
	                                Juego(Pantalla)
	                            elif(opcion.valor == 1):
	                                    terminar = True
	            else:
	                    opcion.ver = False
	            opcion.dibujar(Pantalla)
	    pygame.display.flip()
	pygame.quit()

if __name__ == '__main__':
	main()