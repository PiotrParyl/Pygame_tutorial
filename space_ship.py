
import os
import pygame


WHITE = (255,255,255)
WYSOKOSC, SZEROKOSC = 900,500

ROCK_WYSOKOSC, ROCK_SZEROKOSC = 55,65

WIN = pygame.display.set_mode((WYSOKOSC,SZEROKOSC))

#niezmienne

MAX_BULETS = 10
ROCKS_LVL_1 = 10
ROCKS_LVL_2 = 20


#kolorki

RED = (255,0,0)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "spaceship_yellow.png"))
ROCK_Image_1 = pygame.image.load(os.path.join("assets", "rock_2.jpg"))
ROCK_IMAGE_2 =  pygame.image.load(os.path.join("assets", "rock_4.png"))



YELLOW_SPACESHIP = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "spaceship_yellow.png")), (45, 55))
ROCK_1 = pygame.transform.scale(ROCK_Image_1,(ROCK_WYSOKOSC,ROCK_SZEROKOSC))
ROCK_2 = pygame.transform.scale(ROCK_IMAGE_2,(ROCK_WYSOKOSC,ROCK_SZEROKOSC))


class Game():

    def __init__(self):
        self.rock_1_x = 400
        self.rock_1_y = 0

myGame = Game()




class Player():

    def __init__(self):
        self.yellow_x = 200
        self.yellow_y = 300

player = Player()



def hendle_bullets(bullets):

    for bulet in bullets:
        bulet.y -= 7

        if bulet.y < 0:
            bullets.remove(bulet)


def update_screen(bullets,rock_1,player_1,rocks):




    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (player_1.x, player_1.y))

    WIN.blit(ROCK_1,(rock_1.x,rock_1.y))


    for bullet in bullets:
        pygame.draw.rect(WIN,RED,bullet)






    pygame.display.update()

def moving_rock(rock_1,rocks):

    if len(rocks) < 1:
        rocks.append(rock_1)

    falling_rock = True



    if  falling_rock and len(rocks) < 2:
        rock_1.y += 2

    if rock_1.y > 500:
        rocks.remove(rock_1)







def moving_the_spaceship(keys_pressed,player_1):
    # Sterowanie statkiem
    if keys_pressed[pygame.K_RIGHT]:
        player_1.x += 5

    if keys_pressed[pygame.K_LEFT]:
        player_1.x -= 5
    if keys_pressed[pygame.K_UP]:
        player_1.y -= 5
    if keys_pressed[pygame.K_DOWN]:
        player_1.y += 5

def generate_random_number():

    random_x = randint(0,900)

    return random_x



def main():
    run_game = True

    #skały


    #rock_2 = pygame.Rect(50,0,55,60)


    player_1 = pygame.Rect(100,100, 45,55)
    rock_1 = pygame.Rect(450, 0, ROCK_WYSOKOSC, ROCK_SZEROKOSC)

    clock = pygame.time.Clock()
    bullets = []
    rocks = []


    while run_game:



        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False


            #Dodawanie pocisku do listy
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        bullet = pygame.Rect(player_1.x+20, player_1.y, 5, 20)
                        bullets.append(bullet)







        keys_pressed = pygame.key.get_pressed()




        print(rocks)
        print(bullets)

        moving_rock(rock_1,rocks)
        hendle_bullets(bullets)
        moving_the_spaceship(keys_pressed,player_1)
        update_screen(bullets,rock_1,player_1,rocks)


main()