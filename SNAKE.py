import os
import pygame
import random
import time

def load_image(name):
	return pygame.image.load(os.path.join('', name)).convert()

pygame.init()
pygame.display.set_caption('Serpiente')
pygame.display.set_icon(pygame.image.load("icon.png"))
clock = pygame.time.Clock()
black = (0,0,0)
red = (175,17,32)
green = (53,144,28)
purple = (112,38,120)
snake_green =(31,107,47)
width = 500
height = 500
font = pygame.font.SysFont("arial.ttf", 25)
surface = pygame.display.set_mode((width,height))
background = load_image('GAME_PLAY.jpg')
surface.blit(background, [0,0])
bite = pygame.mixer.Sound("bite.ogg")
bite.set_volume(0.1)
game_over = pygame.mixer.Sound("game_over.ogg")
game_loop_music = pygame.mixer.Sound("game_loop.ogg")
select = pygame.mixer.Sound("select.ogg")

def messageToScreen(msg,color,y_displace=0):
	textSur, textRect = text_objetos(msg,color)
	textRect.center = (250),(250)+y_displace
	surface.blit(textSur,textRect)

def intro():
	intro = True
	while intro:
		surface.blit(load_image('INTRO.jpg'), [0,0])
		pygame.display.update()		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					gameLoop()
					intro = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.key == pygame.K_i:
					select.play(0)
					documentation()
					intro = False 

def points(score, velocidad):
	text = font.render("PUNTAJE: "+str(score),True,black)
	text2 = font.render("VELOCIDAD: "+str(velocidad-14), True,black)
	surface.blit(text,[25,20])
	surface.blit(text2,[350,20])

def serpiente(serp_tamano ,listaSerpiente):
	for i in listaSerpiente:
		pygame.draw.rect(surface,snake_green,[i[0],i[1],serp_tamano,serp_tamano])

def gameLoop():
	game_loop_music.play(18)
	listaSerpiente = []
	largoSerpiente = 1
	sentido = ''
	serp_tamano = 10
	azarManzanaRx = round(random.randrange (100,width-100)/10)*10
	azarManzanaRy = round(random.randrange (100,height-100)/10)*10
	azarManzanaVx = round(random.randrange (100,width-100)/10)*10
	azarManzanaVy = round(random.randrange (100,height-100)/10)*10
	azarManzanaLx = round(random.randrange (100,width-100)/10)*10
	azarManzanaLy = round(random.randrange (100,height-100)/10)*10
	velocidad = 15
	contador = 0
	mover_x = 400
	mover_y = 250
	mover_x_cambio = 0
	mover_y_cambio = 0
	lost = False

	while not lost:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and sentido != 'RIGHT':
					mover_x_cambio = -serp_tamano
					mover_y_cambio = 0
					sentido = 'LEFT'
				elif event.key == pygame.K_RIGHT and sentido != 'LEFT':
					mover_x_cambio = serp_tamano
					mover_y_cambio = 0		
					sentido = 'RIGHT'
				elif event.key == pygame.K_UP and sentido != 'DOWN':
				 	mover_y_cambio = -serp_tamano
				 	mover_x_cambio = 0
				 	sentido = 'UP'
				elif event.key == pygame.K_DOWN and sentido != 'UP':
				 	mover_y_cambio = serp_tamano
				 	mover_x_cambio = 0
				 	sentido = 'DOWN'
				elif event.key == pygame.K_p:
					pause()
		mover_x += mover_x_cambio
		mover_y += mover_y_cambio
		surface.blit(load_image('GAME_PLAY.jpg'), [0,0])
		cabezaSerpiente = []
		cabezaSerpiente.append(mover_x)
		cabezaSerpiente.append(mover_y)
		listaSerpiente.append(cabezaSerpiente)
		if len(listaSerpiente)>largoSerpiente:
			del listaSerpiente[0]
		for i in range(len(listaSerpiente)-1):
			if cabezaSerpiente == listaSerpiente[i]:
				game_over.play(0)	
				game_loop_music.stop()	
				gameOver(largoSerpiente)
		serpiente(serp_tamano,listaSerpiente)
		points (largoSerpiente-1, velocidad)
		pygame.draw.rect(surface, red, [azarManzanaRx, azarManzanaRy, 10, 10])
		pygame.draw.rect(surface, green, [azarManzanaVx, azarManzanaVy, 10, 10])
		pygame.draw.rect(surface, purple, [azarManzanaLx, azarManzanaLy, 10, 10])
		pygame.display.update()
		if mover_x == azarManzanaRx and mover_y == azarManzanaRy:	
			azarManzanaRx = round(random.randrange (50,width-50)/10)*10
			azarManzanaRy = round(random.randrange (50,height-50)/10)*10
			largoSerpiente += 1
			contador += 1
			if contador%3 == 0:
				velocidad+=1
			bite.play(0)	
		if mover_x == azarManzanaVx and mover_y == azarManzanaVy:	
			azarManzanaVx = round(random.randrange (50,width-50)/10)*10
			azarManzanaVy = round(random.randrange (50,height-50)/10)*10	
			largoSerpiente += 5	
			velocidad +=3
			bite.play(0)	
		if mover_x == azarManzanaLx and mover_y == azarManzanaLy:			
			azarManzanaLx = round(random.randrange (50,width-50)/10)*10
			azarManzanaLy = round(random.randrange (50,height-50)/10)*10
			largoSerpiente+=10
			velocidad +=6
			bite.play(0)	
		if mover_x >= width or mover_x <= 1 or mover_y <=45 or mover_y >= height-50: 
				game_over.play(0)	
				game_loop_music.stop()	
				gameOver(largoSerpiente)
		clock.tick(velocidad)

def gameOver(largoSerpiente):
	lost = True
	while lost:
			surface.blit(load_image('PERDISTE.jpg'), [0,0])
			text = font.render("PUNTAJE: "+str(largoSerpiente-1),True,black)
			surface.blit(text,[210,250])			
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						gameLoop()
					elif event.key == pygame.K_q:
						gameOver = False
						pygame.quit()
						quit()	

def pause():
	select.play(0)
	pausedo = True
	while pausedo:
		pygame.mixer.pause()
		surface.blit(load_image('pause1.jpg'), [0,0])
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					select.play(0)
					pygame.mixer.unpause()
					pausedo = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()

def documentation():
	documentation = True
	while documentation:
		surface.blit(load_image('INSTRUCCIONES.jpg'), [0,0])
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_v:
					select.play(0)
					intro()
					documentation = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit() 

intro()