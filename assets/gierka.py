import pygame
import os

#kolory i inne pierdoly
WHITE = (255,255,255)
WYSOKOSC, SZEROKOSC = 900,500


WIN = pygame.display.set_mode((WYSOKOSC,SZEROKOSC))
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets","spaceship_yellow.png"))

YELLOW_SPACESHIP = pygame.transform.scale(pygame.image.load(os.path.join("assets","spaceship_yellow.png")),(45,55))

class Player():

    def __init__(self):
        self.yellow_x = 300
        self.yellow_y = 200



class Game():


    def update_screen(self):
        WIN.fill(WHITE)
        #WIN.blit(YELLOW_SPACESHIP,(self.yellow_x,self.yellow_y))

        pygame.display.update()


    def main(self):


            run_game = True

            while run_game:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run_game = False

                self.update_screen()


            self.main()








