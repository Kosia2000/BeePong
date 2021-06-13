import pygame
import sys
from classes import Bee, Racket, Lives, Score
from sounds import new_life
from menu import *
from end import *
import time


SIZE = [640, 640]
BC_COLOR = [50, 205, 50]
BEE_SPEED = [10, 5]
RACKET_POS = [270, 500]

pygame.init()
pygame.display.set_caption('BeePong')
screen = pygame.display.set_mode(SIZE)
background = pygame.image.load("Images/meadow.jpg")
clock = pygame.time.Clock()


running = menu()


def start_game():

    bee = Bee("Images/bee2.png", BEE_SPEED, [10, 10])
    beeGroup = pygame.sprite.Group(bee)
    racket = Racket(RACKET_POS)
    score = Score()
    lives = Lives()

    global running

    while running:

        lives.draw_lives()

        for incident in pygame.event.get():
            if incident.type == pygame.QUIT:
                running = False

            elif incident.type == pygame.MOUSEMOTION:
                racket.move_on(incident)

        if bee.rect.top >= screen.get_rect().bottom:
            bee.rect.topleft = [50, 50]
            running = lives.minus_life()
            if lives.return_lives() == 0:
                running = end()
                lives = Lives()
                score = Score()
            new_life.play()

        clock.tick(48)
        bee.move(score)
        racket.hit(bee)

        screen.blit(background, (0, 0))
        screen.blit(bee.image, bee.rect)
        screen.blit(racket.image, racket.rect)

        score.draw_points()

        if (score.points % 5 == 0) and not lives.bonus_life_active and lives.last_dropped != score.points:
            lives.add_life(racket)
            lives.last_dropped = score.points

        if lives.bonus_life_active:
            lives.move_life(racket)
            lives.draw_added_life()

    pygame.quit()


start_game()
