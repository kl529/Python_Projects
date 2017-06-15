from random import *
import pygame

class Pause:
	
	"""
	Class that is used for the drawing of the gameover 
	screen.
	"""
	
	def __init__(self, width, height, score):
		self.width = width
		self.height = height
		self._score = score
		self.pressContinue=0

	# Draws the Gameover screen and displays the score
	def draw_Pause(self,screen):
		background_color = (255,255,255)
		font_color = (0,0,0)
		LITERED = (255, 0, 0)
		LITEYELLOW = (255, 255, 0)
		LITEORANGE = (255, 128, 0)
		
		pygame.draw.rect(screen, background_color, (0, 0, self.width, self.height), 0)
		
		tetris_font = pygame.font.Font("milky.ttf",32)
		tetris_font.set_bold(1)
		
		label_1 = tetris_font.render("Pause", 1, LITERED)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (150, 150)

		background = pygame.image.load('hos.jpg')

		screen.blit(background, (-100, -20)) 
		screen.blit(label_1, label_1_rect)

	# Prints the continue message
	def press_continue(self,screen):
		DARKGREEN = (0, 180, 0)
		tetris_font = pygame.font.SysFont("monospace", 12)
		font_color = (0,0,0)
		
		label_1 = tetris_font.render("Press any button to continue",1, DARKGREEN)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (150, 350)
		
		screen.blit(label_1, label_1_rect)