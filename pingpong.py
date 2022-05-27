import sys
import pygame
import random

# intialize the pygame
pygame.init()

# clock
clock = pygame.time.Clock()


def ball_animation():
    global ball_s_x, ball_s_y

    ball.x += ball_s_x
    ball.y += ball_s_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_s_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        restart()
        #ball_s_x *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_s_x *= -1


def player_animation():
    global player_s

    player.y += player_s

    if player.top <= 0:
        player.top = 5
    if player.bottom >= screen_height:
        player.bottom = screen_height-5


def opponent_animation():
    global opponent_s

    opponent.y += opponent_s

    if opponent.top < ball.y:
        opponent.y += opponent_s
    if opponent.bottom > ball.y:
        opponent.y -= opponent_s
    if opponent.top <= 0:
        opponent_s *= -1
    if opponent.bottom >= screen_height:
        opponent_s *= -1


def restart():
    global ball_s_x, ball_s_y, player_score, opponent_score, score_time

    if ball.left <= 0:
        player_score += 1
    if ball.right >= screen_height:
        opponent_score += 1
    score_time = pygame.time.get_ticks()
    ball.center = (screen_width/2 - 15, screen_height/2 - 15)
    ball_s_x *= random.choice((1, -1))
    ball_s_y *= random.choice((1, -1))


# create screen size and caption
screen_width = 1040
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ping pong")

# create the game rectangles - מייצר את הדמויות
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 15, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(5, screen_height/2 - 70, 10, 140)

# create 2 colors..
bg_color = pygame.Color('green12')
light_grey = (100, 100, 100)

# def ball speed
ball_s_x = 10
ball_s_y = 10
player_s = 0
opponent_s = 8

# text veriables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# score timer
score_time = None

# the game loop
while True:

    # handling input - עובר על כל פעולה ובודק אם היא יציאה
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_s += 10
            elif event.key == pygame.K_UP:
                player_s -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_s -= 10
            elif event.key == pygame.K_UP:
                player_s += 10

    # call the ball animation function
    ball_animation()
    player_animation()
    opponent_animation()

    # fill the screen in color - ממלא את רקע המסך בכל פעם מחדש כדי שהדמויות יופיעו שוב ושוב לפי העדכון שלהן
    screen.fill(bg_color)

    # drawing the rectangles in the selected shape - מצייר את הדמויות שייצרנו
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    player_text = game_font.render(f"{player_score}", True, light_grey)
    screen.blit(player_text, (540, 300))
    player_text = game_font.render(f"{opponent_score}", True, light_grey)
    screen.blit(player_text, (486, 300))


    # update the screen
    pygame.display.flip()

    # 60 per second
    clock.tick(60)
