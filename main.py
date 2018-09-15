import pygame
import time
from random import randint

black = (0, 0, 0)
white = (255, 255, 255)
green = (50, 205, 50)
screenWidth = 800
screenHeight = 500
img = pygame.image.load('birdy.png')

image_height = 80
image_width = 86

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Flappy Bird!")
clock = pygame.time.Clock()
background_image = pygame.image.load("sky.jpeg").convert_alpha()

def flappy_bird(x, y, image):
    screen.blit(img, (x, y))

def background(x, y, image):
    screen.blit(background_image, (screenHeight, screenWidth))

def getColor():
    x = randint(0, 255)
    y = randint(0, 255)
    z = randint(0, 255)
    return (x, y, z)

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: "+str(count), True, white)
    screen.blit(text, [0,0])

def gameOver():
    sendMessage("game over!")

def makeTextObjs(text, font, color):
    textSurf = font.render(text, True, color)
    return textSurf, textSurf.get_rect()

def sendMessage(text):
    sText = pygame.font.Font('freesansbold.ttf', 20)
    lText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, lText, white)
    titleTextRect.center = screenWidth / 2, screenHeight / 2
    screen.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue!', sText, white)
    typTextRect.center = screenWidth / 2, ((screenHeight / 2) + 100)
    screen.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()


def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None

def blocks(x, y, wid, height, gap, color):
    pygame.draw.rect(screen, color, [x, y, wid, height])
    pygame.draw.rect(screen, color, [x, y + height + gap, wid, screenHeight])

def main():
    x = 5
    y = 10
    y_move = 1
    game_over = False

    x_block = screenWidth
    y_block = 0

    block_width = 75
    block_height = randint(0, screenHeight / 2)
    gap = image_height * 3
    block_move = 6

    current_score = 0
    color = getColor()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5
        y += y_move
        screen.fill(black)
        score(current_score)
        # pygame.transform.scale(background_image, (1280, 1024))
        # screen.blit(background_image, (0,0))
        flappy_bird(x, y, img)
        blocks(x_block, y_block, block_width, block_height, gap, color)
        x_block -= block_move

        roof = 0
        if y > screenHeight - 80 or y < roof:
            gameOver()
        if x_block < (-1 * block_width):
            x_block = screenWidth
            color = getColor()
            current_score += 1
            block_move += 1
            block_height = randint(0, screenHeight / 2)

        if image_width + x > x_block:
            if x < x_block + block_width:
                if y < block_height:
                    if x - image_width < block_width + x_block:
                        gameOver()
        if image_width + x > x_block:
            if y + image_height > block_height + gap:
                if x < block_width + x_block:
                    gameOver()

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()

