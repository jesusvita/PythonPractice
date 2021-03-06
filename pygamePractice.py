import pygame
import time
import random

# intialize pygame
pygame.init()

# list of colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# window size variables
display_width = 800
display_height = 600

# Area of the window
gameDisplay = pygame.display.set_mode((display_width, display_height))

# title for the window
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()

# size of block
block_size = 10
apple = 10

FPS = 10

font = pygame.font.SysFont(None, 25)

def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])



# event handling loop
def gameLoop():
    gameExit = False
    gameOver = False

    # start position
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    appleWidth = round(random.randrange(0, display_width)/ 10.0) * 10.0
    appleHeight = round(random.randrange(0 , display_height)/ 10.0) * 10.0

    points = -1
    mrSnake = []

    while not gameExit:

        while gameOver == True:
                gameDisplay.fill(white)
                message_to_screen("Game over, press C to play again or Q to quit", red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                        if event.key == pygame.K_c:
                            gameLoop()

        for event in pygame.event.get():

            #If the user quits, exit the game
            if event.type == pygame.QUIT:
                gameExit = True

            # Controller
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -10
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 10
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -10
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 10
                    lead_x_change = 0
                elif event.key == pygame.K_x:
                    appleWidth = round(random.randrange(0, display_width)/ 10.0) * 10.0
                    appleHeight = round(random.randrange(0 , display_height)/ 10.0) * 10.0

            # Condition to end game
            if lead_x >= display_width or lead_x < 10 or lead_y >= display_height or lead_y < 10:
                gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        # change the background color
        gameDisplay.fill(white)

        # draw a box
        pygame.draw.rect(gameDisplay, red, [appleWidth, appleHeight, apple, apple])

        snakeList = []
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)


        snake(block_size, snakeList)
        # here we print the snake using a list

        if lead_x == appleWidth and lead_y == appleHeight:
            appleWidth = round(random.randrange(0, display_width)/ 10.0) * 10.0
            appleHeight = round(random.randrange(0 , display_height)/ 10.0) * 10.0
            print(appleWidth)
            print(appleHeight)
            snakeHead.append(appleWidth)
            snakeHead.append(appleHeight)
            snakeList.append(snakeHead)
            print(snakeList)


        pygame.display.update()
        clock.tick(FPS)

    message_to_screen("You lose", red)
    # pygame.display.update()
    time.sleep(2)

    # exit pygame
    pygame.quit()

    # exit python
    quit()

gameLoop()
