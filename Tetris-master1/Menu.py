from random import *
import pygame


class Menu:
	"""
	Class to draw the menu and keep it updated
	
	Gives information to the main file for which
	screen to display and which game to play.
	"""


	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.demo=0
		self.singlePlayer=1
		self.info=0
		self.gameStart=0
		self.infoDone=0
		self.hidden = 0
	
	# draws the menu screen with the title and names
	def draw_menu(self,screen):
		
		background_color=(255,255,255)
		font_color = (0,0,0)
		name = (0,0,255)
		
		pygame.draw.rect(screen, background_color, (0,0,self.width,self.height),0)
		
		tetris_font = pygame.font.Font("milky.ttf",32)
		tetris_font.set_bold(1)
		
		label_1 = tetris_font.render("TETRIS",1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (150, 100)
		
		tetris_font = pygame.font.SysFont("monospace", 10)
		
		label_5 = tetris_font.render("By JIWON edition",1, name)
		label_5_rect = label_5.get_rect()
		label_5_rect.center = (150, 350)

		background = pygame.image.load('backmenu.jpg')

		screen.blit(background, (-525, -940)) 
		
		screen.blit(label_1, label_1_rect)
		screen.blit(label_5, label_5_rect)
	
	# displays the info page once it is selected
	# has instructions for how to play the game
	# as well as the scoring system
	def draw_info(self,screen):
		background_color=(255,255,255)
		font_color = (0,0,0)

		pygame.draw.rect(screen, background_color, (50,50,self.width-100,self.height-100),0)
		
		tetris_font = pygame.font.Font("milky.ttf",32)
		tetris_font.set_bold(1)
		
		label_1 = tetris_font.render("INFO",1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (150, 100)
		
		
		tetris_font = pygame.font.SysFont("monospace", 20)
		
		label_2 = tetris_font.render("← : Left move",1, font_color)
		label_2_rect = label_2.get_rect()
		label_2_rect.center = (150, 150)
		
		label_7 = tetris_font.render("→ : Right move",1, font_color)
		label_7_rect = label_7.get_rect()
		label_7_rect.center = (150, 180)

		label_3 = tetris_font.render("↑ : Rotate Block",1, font_color)
		label_3_rect = label_3.get_rect()
		label_3_rect.center = (150, 210)
		
		label_8 = tetris_font.render("↓ : Falling speed Up",1, font_color)
		label_8_rect = label_8.get_rect()
		label_8_rect.center = (150, 240)
		
		label_4 = tetris_font.render("SPACE BAR : Drop block",1, font_color)
		label_4_rect = label_4.get_rect()
		label_4_rect.center = (150, 270)
		
		tetris_font = pygame.font.SysFont("monospace", 15)
		label_5 = tetris_font.render("Score=(number of lines)*100",1, font_color)
		label_5_rect = label_5.get_rect()
		label_5_rect.center = (150, 300)
		
		label_6 = tetris_font.render("Press any button to GO MENU",1, font_color)
		label_6_rect = label_6.get_rect()
		label_6_rect.center = (150, 350)

		background = pygame.image.load('backinfo.jpg')

		screen.blit(background, (-100, -20)) 
		
		screen.blit(label_1, label_1_rect)
		screen.blit(label_2, label_2_rect)
		screen.blit(label_3, label_3_rect)
		screen.blit(label_4, label_4_rect)
		screen.blit(label_5, label_5_rect)
		screen.blit(label_6, label_6_rect)
		screen.blit(label_7, label_7_rect)
		screen.blit(label_8, label_8_rect)
		
	# updates the menu to display the current users selection
	def update_menu(self,screen):
		LITEPURPLE = (255, 0, 255)
		LITEGREEN = (0, 255, 0)	
		LITETEAL = (0, 175, 175)
		Hidden = (240, 240, 240)
		
		tetris_font = pygame.font.Font("milky.ttf",16)
		tetris_font.set_bold(0)
		
		singlePlayerBG=(255*(1-self.singlePlayer),255*(1-self.singlePlayer),255*(1-self.singlePlayer))
		demoBG=(255*(1-self.demo),255*(1-self.demo),255*(1-self.demo))
		infoBG=(255*(1-self.info),255*(1-self.info),255*(1-self.info))
		hiddenBG=(255*(1-self.hidden),255*(1-self.hidden),255*(1-self.hidden))
		
		pygame.draw.rect(screen, singlePlayerBG, (90,180,120,20),0)
		label_2 = tetris_font.render("Single Player",1, LITEPURPLE)
		label_2_rect = label_2.get_rect()
		label_2_rect.center = (150, 190)
		
		pygame.draw.rect(screen, infoBG, (90,240,120,20),0)
		label_3 = tetris_font.render("Info",1, LITEGREEN)
		label_3_rect = label_3.get_rect()
		label_3_rect.center = (150, 250)

		pygame.draw.rect(screen, demoBG, (90,300,120,20),0)
		label_4 = tetris_font.render("EXIT",1, LITETEAL)
		label_4_rect = label_4.get_rect()
		label_4_rect.center = (150, 310)

		pygame.draw.rect(screen, singlePlayerBG, (90,180,120,20),0)
		label_5 = tetris_font.render("Hidden Mode",1, Hidden)
		label_5_rect = label_5.get_rect()
		label_5_rect.center = (150, 400)
		
		screen.blit(label_2, label_2_rect)
		screen.blit(label_3, label_3_rect)
		screen.blit(label_4, label_4_rect)
		screen.blit(label_5, label_5_rect)

	# function to switch the current selection on the menu screen
	def move_cursor(self,direction):
		if self.demo:
			if direction == 1:
				self.demo = 0
				self.hidden = 1
			elif direction == -1:
				self.demo=0
				self.info=1

		elif self.singlePlayer:
			if direction == 1:
				self.singlePlayer = 0
				self.info = 1
			elif direction == -1:
				self.hidden = 1
				self.singlePlayer = 0

		elif self.info:
			if direction == 1:
				self.demo = 1
				self.info = 0

			elif direction == -1:
				self.singlePlayer = 1
				self.info = 0

		elif self.hidden:
			if direction == 1:
				self.hidden = 0
				self.singlePlayer = 1

			elif direction == -1:
				self.demo == 1
				self.hidden = 0


	# function to reset game initialization variables
	def reset_game(self):
		self.demo = 0
		self.singlePlayer = 1
		self.info = 0
		self.gameStart = 0
		self.infoDone=0
		self.hidden=0