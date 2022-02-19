import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pygame.rect import Rect

TITLE = 'ARCANOID'
WIDTH = 800
HEIGHT = 500
ball_speed_x = 2
ball_speed_y = 2
SCORE = 0
paddle = Actor('paddleblue')
paddle.x = 120
paddle.y = 400

ball = Actor('ballblue')
ball.x = 30
ball.y = 300

line_list = []
game_over = False

box = Rect((30, 20), (80, 30))



def count(x):
    if x % 10 == 1 and x != 11:
        return 'очко'
    elif (x % 10 == 2 and x != 12) or (x % 10 == 3 and x != 13) or (x % 10 == 4 and x != 14):
        return 'очка'
    else:
        return 'очков'


# _____________________________________________________________________________--
def draw():
    if not game_over:
        screen.blit('background.png', (0, 0))
        screen.draw.filled_rect(box, 'red')
        paddle.draw()
        ball.draw()
        for line in line_list:
            line.draw()
        screen.draw.text(f'Счёт:{SCORE}', (WIDTH - 70, HEIGHT + 20))
    else:
        screen.blit('background.png', (0, 0))
        screen.draw.text(f'Game Over Ты набрал: {SCORE} {count(SCORE)}', (350, 150))


def update():
    if not game_over:
        global ball_speed_x, ball_speed_y, SCORE
        update_ball()
        if keyboard.left and paddle.x > 50:
            paddle.x -= 5
        if keyboard.right and paddle.x < WIDTH - 50:
            paddle.x += 5

        if paddle.colliderect(ball):
            ball_speed_y *= -1
        for line in line_list:
            if ball.colliderect(line):
                SCORE += 1
                line_list.remove(line)
                ball_speed_y *= -1


# _________________________________________________________________________________--
def update_ball():
    global ball_speed_x, ball_speed_y, game_over
    ball.x -= ball_speed_x
    ball.y -= ball_speed_y
    if ball.x <= 10 or ball.x >= WIDTH - 10:
        ball_speed_x *= -1
    if ball.y <= 10 or ball.y >= HEIGHT - 10:
        ball_speed_y *= -1
    if ball.y > 400:
        game_over = True


def place_lines(image, x, y):
    line_x = x
    line_y = y
    for i in range(10):
        line = Actor(image)
        line.x = line_x
        line.y = line_y
        line_x += 70
        line_list.append(line)


color_line_list = ['element_blue_rectangle_glossy.png', 'element_green_rectangle_glossy.png',
                   'element_red_rectangle_glossy.png']
x = 90
y = 60
for line in color_line_list:
    place_lines(line, x, y)
    y += 35

pgzrun.go()
