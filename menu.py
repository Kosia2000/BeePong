import pygame
from classes import Button

SIZE = [640, 640]
BC_COLOR = [50, 205, 50]
pygame.init()
pygame.display.set_caption('BeePong')
title_font = pygame.font.Font("Fonts/Summerbee.ttf", 100)
title_surface = title_font.render(str("BeePong"), 1, (0, 0, 0))
title_position = [180, 50]


screen = pygame.display.set_mode(SIZE)
#background = pygame.Surface(SIZE)
# background.fill(BC_COLOR)
background = pygame.image.load("Images/bumblebee.jpg")


b1 = Button(screen, (100, 400), "Quit")
b2 = Button(screen, (480, 400), "Start")


def menu():
    screen.blit(background, (0, 0))
    screen.blit(title_surface, title_position)

    button1 = b1.button()
    button2 = b2.button()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(pygame.mouse.get_pos()):
                    return False
                elif button2.collidepoint(pygame.mouse.get_pos()):
                    return True

        pygame.display.update()
    pygame.quit()
