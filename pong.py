import pygame
import random

# Use Arrow Keys (Up and Down) to play
# Ball gets Faster with more Hits
# Bot has a slight advantage (faster paddle)
# Lakshman Chelliah 2023-04-13
# First Finished Experience with PyGame

# set up the screen
pygame.init()
width, height = 1000, 700 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

#colors
white = (255, 249, 237)
black = (0, 0, 0)
red = (250,87,75)

#paddles
paddle_width = 10
paddle_height = 100
left_paddle_x = 50
left_paddle_y = height/2 - paddle_height/2
right_paddle_x = width - 50 - paddle_width
right_paddle_y = height/2 - paddle_height/2

#ball
ball_size = 10
ball_x = width/2 - ball_size/2
ball_y = height/2 - ball_size/2
ball_dx = 5
ball_dy = random.choice([-5, 5])

#score
left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)

speed_of_ball = width/20000

# the main game loop
running = True;
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        
    #paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= width/2500
    if keys[pygame.K_DOWN] and right_paddle_y < height - paddle_height:
        right_paddle_y += width/2500
    
    # move ball
    ball_x += ball_dx * speed_of_ball
    ball_y += ball_dy * speed_of_ball
    
    # check for collisions with paddles
    if ball_dx < 0 and left_paddle_x + paddle_width > ball_x > left_paddle_x and left_paddle_y < ball_y + ball_size < left_paddle_y + paddle_height:
        speed_of_ball +=width/10000 / 10;
        ball_dx *= -1
    if ball_dx > 0 and right_paddle_x < ball_x + ball_size < right_paddle_x + paddle_width and right_paddle_y < ball_y + ball_size < right_paddle_y + paddle_height:
        speed_of_ball +=width/10000 / 10;
        ball_dx  *= -1

        
    # check for collision with walls
    if ball_y <= 0 or ball_y + ball_size >= height:
        ball_dy *= -1
    
    # check for scoring
    if ball_x <= 0:
        speed_of_ball = width/20000
        right_score += 1
        ball_x = width/2 - ball_size/2
        ball_y = height/2 - ball_size/2
        ball_dx = 5
        ball_dy = random.choice([-5, 5])
    if ball_x + ball_size >= width:
        speed_of_ball = width/20000
        left_score += 1
        ball_x = width/2 - ball_size/2
        ball_y = height/2 - ball_size/2
        ball_dx = -5
        ball_dy = random.choice([-5, 5])
        
    if ball_y < left_paddle_y :
        if left_paddle_y > 0:
            left_paddle_y -= width/2000
    elif ball_y > left_paddle_y +50 :
        if left_paddle_y < height - paddle_height:
            left_paddle_y += width/2000
    
    # draw the paddles, ball, and score
    screen.fill(black)
    pygame.draw.rect(screen, white, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, red, (ball_x, ball_y, ball_size, ball_size))
    
    # draw the score
    left_score_text = font.render(str(left_score), True, white)
    right_score_text = font.render(str(right_score), True, white)
    screen.blit(left_score_text, (width/2 - 50 - left_score_text.get_width(), 20))
    screen.blit(right_score_text, (width/2 + 50, 20))
    
    # update the screen
    pygame.display.update()

pygame.quit()


    
    
