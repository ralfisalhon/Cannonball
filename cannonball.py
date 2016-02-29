#Imports essentials and initiates pygame
import pygame
import time
from pygame.locals import *
from random import randint, randrange, uniform
from timeit import default_timer
pygame.init()

backResim =  pygame.image.load("blueBack.jpg")

#Names our game!
pygame.display.set_caption("Cannonball!")

#Color references for future use
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
darkGray = (100,100,100)

#Sets game screen size in pixels
Width = 800
Height = 280

textColor = white

while True:
	playing = "True"
	difficulty = 20
	onLevel = 1.0

	while playing == "True":
		#Initial vars
		Speed = 3
		faceUp = 0.04

		#Creates screen and background for screen updates
		screen = pygame.display.set_mode((Width,Height))
		back = pygame.Surface((Width,Height))
		background = back.convert()
		background.fill(black)
		screen.blit(background,(0,0))
		screen.blit(backResim, (0,Height-233))

		x = 0
		y = Height-26
		vel = 3.0

		randLocationX = randrange(150,Width-50)

		#Text created for moving sprite
		font = pygame.font.Font(None, 46)
		text = font.render("Speed: " + str(Speed), 1, textColor)
		textpos = text.get_rect()

		font2 = pygame.font.Font(None, 46)
		text2 = font2.render("faceUp: " + str(faceUp), 1, textColor)
		textpos = text2.get_rect()

		font3 = pygame.font.Font(None, 46)
		text3 = font3.render("Level: " + str(difficulty), 1, textColor)
		textpos = text3.get_rect()

		font4 = pygame.font.Font(None, 46)
		text4 = font4.render("DistanceX: " + str(abs(x - randLocationX)), 1, textColor)
		textpos = text4.get_rect()

		#Main loop for game
		while y < Height-20 and not x > Width-25:
			for event in pygame.event.get():
				#Quits game if red button is pressed
				if event.type == pygame.QUIT:
					exit()
				#Checks keydown events
				if event.type == KEYDOWN:
					if event.key == K_q:
						exit()
					if event.key == K_UP and faceUp > 0.02:
						faceUp -= 0.02
					if event.key == K_DOWN and faceUp < 0.1:
						faceUp += 0.02
					if event.key == K_RIGHT and Speed < 4:
						Speed += 1
					if event.key == K_LEFT and Speed > 1:
						Speed -= 1
			#Updates display for the UI
			pygame.display.update()
			
			#After update, screen is created once again for next update
			
			screen.blit(background,(0,0))
			screen.blit(backResim, (0,Height-233))

			pygame.draw.rect(screen, red, (randLocationX,Height-25,25,25), 0)

			pygame.draw.rect(screen, darkGray, (x,y,25,25), 0)

			text = font.render("Speed: " + str(Speed), 1, textColor)
			textpos.centerx = 125
			textpos.centery = 25
			screen.blit(text, textpos)

			text2 = font.render("Gravity: " + str(faceUp*50), 1, textColor)
			textpos.centerx = 275
			textpos.centery = 25
			screen.blit(text2, textpos)

			text3 = font.render("Level: " + str(21 - difficulty), 1, textColor)
			textpos.centerx = 490
			textpos.centery = 25
			screen.blit(text3, textpos)

			text4 = font4.render("DistanceX: " + str(abs(x - randLocationX)), 1, textColor)
			textpos.centerx = 650
			textpos.centery = 25
			screen.blit(text4, textpos)

			y -= vel*onLevel
			vel -= faceUp*onLevel
			x += Speed*onLevel

		#print "You finished " + str(abs(x - randLocationX)) + " pixels apart!"
		if abs(x - randLocationX) <= difficulty:
			#print "That's very good!" 
			difficulty -= 1
			onLevel += 0.1
		else:
			#print "You can do better! You had to be within " + str(difficulty) + " pixels to pass!"
			playing = "False"

		pygame.display.update()
		time.sleep(0.5)

	print "GAME OVER! Restarting"

	font = pygame.font.Font(None, 90)
	text = font.render("GAME OVER! Restarting", 1, red)
	textpos = text.get_rect()
	textpos.centerx = Width/2
	textpos.centery = (Height/2)*1.2
	screen.blit(text, textpos)

	pygame.display.update()

	time.sleep(2)