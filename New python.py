import pygame
import random
import time

pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Snake attributes
snake_block = 20
snake_speed = 10

# Clock to control game speed
clock = pygame.time.Clock()

def display_score(score):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, (10, 10))

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])

def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    rendered_msg = font_style.render(msg, True, color)
    screen.blit(rendered_msg, [screen_width / 6, screen_height / 3])

def game_loop():
    game_over = False
    game_close = False

    # Snake position and movement
    snake_list = []
    length_of_snake = 1
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake_x_change = 0
    snake_y_change = 0

    # Food position
    food_x = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block
                    snake_x_change = 0

        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_close = True

        snake_x += snake_x_change
        snake_y += snake_y_change
        screen.fill(white)
        pygame.draw.rect(screen, black, [food_x, food_y, snake_block, snake_block])
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
            food_y = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
if __name__ == "__main__":
    game_loop()