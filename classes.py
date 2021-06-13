import pygame
import sys
from sounds import *
import random
import time

pygame.init()
screen = pygame.display.set_mode([640, 640])
background = pygame.image.load("Images/meadow.jpg")


class Bee(pygame.sprite.Sprite):
    '''
    The class responsible for creating the Bee object. 

    Parameters
    ----------
        image_file : string
            A .png file

        speed : double
            A decimal number

        position : list
            A list of decimal numbers
    '''

    def __init__(self, image_file, speed, position):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(self.image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed

    def move(self, score):
        '''
        Method which moves the bee and add speed.

        Parameters
        ----------
        score : int
            The points earned
        '''

        newPosition = self.rect.move(self.speed)
        self.rect = newPosition
        if self.rect.left <= 0 or self.rect.right >= screen.get_width():
            self.speed[0] = -self.speed[0]
            if float(self.speed[0]) < 0:
                self.image = pygame.image.load("Images/bee.png")
            else:
                self.image = pygame.image.load(self.image_file)

        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            if float(self.speed[0]) < 0:
                self.speed[0] -= 0.50
            else:
                self.speed[0] += 0.50

            score.add_point()

    def get_position(self):
        '''
        Method which get the bee position.

        Returns
        ----------
        self.rect.left, self.rect.top
            A left and top position.
        '''

        return self.rect.left, self.rect.top


class Racket(pygame.sprite.Sprite):
    '''
    The class responsible for creating the Racket object.

    Parameters
    ----------
        position : list
            A list of decimal numbers

        lives : int
            Number of lives

        points : int
            Number of points
    '''

    def __init__(self, position, lives=2, points=0):
        pygame.sprite.Sprite.__init__(self)
        surface_image = pygame.surface.Surface(
            [100, 20])  # pierwsza -> długość
        surface_image.fill([0, 0, 0])
        self.image = surface_image.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.lives = lives
        self.points = points

    def move_on(self, incident):
        '''
        The method that moves the racket.

        Parameters:
        ----------
        incident : str
            Defines the mouse motion
        '''

        if incident.pos[0] > 50 and incident.pos[0] < 590:
            self.rect.centerx = incident.pos[0]

    def hit(self, bee_class):
        '''
        Method for hitting the racket

        Parameters:
        ----------
        bee_class : str (object from game-body)
            Bee class object
        '''

        bee_position = bee_class.get_position()
        racket_position = [self.rect.left, self.rect.top]

        if bee_position[0] <= 0 or bee_position[0] >= 610:
            hit_wall.play()

        if (racket_position[0] < bee_position[0] + 15 < racket_position[0] + 100) and (racket_position[1] == bee_position[1] + 30):
            bee_class.speed[1] = -bee_class.speed[1]
            hit_racket.play()

    def get_position(self):
        '''
        Method which get the bee position.

        Returns
        ----------
        self.rect.left, self.rect.top
            A left and top position.
        '''

        return self.rect.left, self.rect.top


class Score:
    '''
    The class responsible for counting points.
    '''

    def __init__(self):
        self.points = 0

    def add_point(self):
        '''
        The method that adds points.
        '''

        get_point.play()
        self.points += 1

    def generate_font(self):
        '''
        The method that generates font.

        Returns
        ----------

        score_surface
            Surface of score

        score_position
            Position of score 
        '''

        score_font = pygame.font.Font(None, 50)
        score_surface = score_font.render(
            str("Score {}".format(self.points)), 1, (0, 0, 0))
        score_position = [10, 10]
        return score_surface, score_position

    def draw_points(self):
        '''
        The method that draws points.
        '''

        word = self.generate_font()
        screen.blit(word[0], word[1])
        pygame.display.update()

    def return_points(self):
        return self.points


class Lives(pygame.sprite.Sprite):
    '''
    The class responsible for counting lives.
    '''

    def __init__(self, speed=[0, 10]):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 2
        self.image = pygame.image.load("Images/bee.png")

        self.life_image = pygame.image.load("Images/bee2.png")
        self.speed = speed
        self.rect = self.life_image.get_rect()
        self.rect.left = 0
        self.rect.top = 0
        self.b_speed = 0
        self.bonus_life_active = False
        self.bonus_life_position = [0, 0]
        self.last_dropped = 0

    def draw_added_life(self):
        if self.bonus_life_active:
            screen.blit(self.life_image, self.rect)

    def move_life(self, racket_class):
        newPosition = self.rect.move(self.speed)
        racket_position = racket_class.get_position()
        width = screen.get_rect().width

        self.rect = newPosition
        life_position = [self.rect.left, self.rect.top]

        if (racket_position[0] < life_position[0] + 15 < racket_position[0] + 100) and (racket_position[1] == life_position[1] + 30):
            add_life.play()
            self.lives += 1
            self.bonus_life_active = False

        if life_position[1] >= width:
            self.bonus_life_active = False

    def add_life(self, racket_class):
        self.bonus_life_active = True
        racket_position = racket_class.get_position()
        self.rect.top = 0
        self.rect.left = random.randint(50, 600)

    def return_lives(self):
        return self.lives

    def minus_life(self):
        '''
        The method that subtracts lives.

        Returns
        ----------

        bool
        '''

        plask.play()
        self.lives -= 1
        if self.lives == 0:
            self.no_lives()
            return False
        else:
            pygame.time.delay(2000)
            return True

    def draw_lives(self):
        '''
        The method that draws lives.
        '''

        if self.lives > 0:
            for i in range(self.lives):
                width = screen.get_rect().width
                screen.blit(self.image, [width-40 * i, 20])
        pygame.display.update()

    def no_lives(self):
        '''
        The method that lives are over.
        '''

        pygame.time.delay(500)
        game_over.play()

        pygame.time.delay(2000)


class Button(pygame.sprite.Sprite):
    '''
    The class responsible for creating the Button object. 

    Parameters
    ----------
        screen : pygame.Surface
            Screen surface

        position : list
            A list of decimal numbers

        text : str
            A text on the button
    '''

    def __init__(self, screen, position, text):
        self.screen = screen
        self.position = position
        self.text = text
        self.font = font = pygame.font.Font("Fonts/Summerbee.ttf", 40)

    def button(self):
        '''
        The method that lives are over.

        Returns
        ----------
        self.screen.blit(text_render, (x, y))

        '''
        text_render = self.font.render(
            self.text, 100, (0, 0, 0))  # rysuje tekst na powierzchni
        x, y, w, h = text_render.get_rect()
        x, y = self.position
        pygame.draw.rect(self.screen, (255, 240, 0), pygame.Rect(
            x-20, y-20, w+40, h+40),  100, 100)
        return self.screen.blit(text_render, (x, y))
