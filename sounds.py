import pygame
import sys

pygame.mixer.init()
pygame.mixer.music.load("Sounds/polka.wav")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

get_point = pygame.mixer.Sound("Sounds/get_point.wav")
hit_wall = pygame.mixer.Sound("Sounds/hit_wall.wav")
hit_racket = pygame.mixer.Sound("Sounds/hit_paddle.wav")
plask = pygame.mixer.Sound("Sounds/splat.wav")
game_over = pygame.mixer.Sound("Sounds/game_over.wav")
new_life = pygame.mixer.Sound("Sounds/new_life.wav")
add_life = pygame.mixer.Sound("Sounds/add_life.wav")

get_point.set_volume(0.30)
hit_wall.set_volume(0.30)
hit_racket.set_volume(0.30)
plask.set_volume(0.50)
game_over.set_volume(0.30)
new_life.set_volume(0.30)
add_life.set_volume(0.30)
