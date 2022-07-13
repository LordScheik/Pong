from microbit import *
import speech
import os
import random

paddle_x = 2
paddle_y = 4
paddle_length = 2

ball_x = random.choice([1, 2, 3])
ball_y = random.choice([1, 2])

change_x = random.choice([-1, 1])
change_y = random.choice([-1, 1])

highscore = 0
score = 0

time = 500

ANIMATION_SPEED = 130

FILE_NAME = 'score.txt'


while True:
    for x in range(0, 5):
        y = 0
        while x >= 0:
            display.set_pixel(x, y, 9)
            sleep(ANIMATION_SPEED)
            x -= 1
            y += 1
    if button_a.is_pressed() and button_b.is_pressed():
        break
    for y in range(1, 5):
        x = 4
        while y <= 4:
            display.set_pixel(x, y, 9)
            sleep(ANIMATION_SPEED)
            x -= 1
            y += 1
    if button_a.is_pressed() and button_b.is_pressed():
        break
    for x in range(0, 5):
        y = 0
        while x >= 0:
            display.set_pixel(x, y, 0)
            sleep(ANIMATION_SPEED)
            x -= 1
            y += 1
    if button_a.is_pressed() and button_b.is_pressed():
        break
    for y in range(1, 5):
        x = 4
        while y <= 4:
            display.set_pixel(x, y, 0)
            sleep(ANIMATION_SPEED)
            x -= 1
            y += 1
    if button_a.is_pressed() and button_b.is_pressed():
        break

# read saved highscore
for file_name in os.listdir():
    if file_name == FILE_NAME:
        with open(file_name) as file:
            highscore = int(file.read())

display.scroll(highscore)

speech.say('Start')
display.scroll('Start')

for i in range(paddle_length):
    display.set_pixel(paddle_x + i, paddle_y, 9)

display.set_pixel(ball_x, ball_y, 9)
sleep(time)

while True:
    # update
    if ball_x == 0 or ball_x == 4:
        change_x *= -1
    if ball_y == 0:
        change_y *= -1
    if ball_y == 4:
        break

    if ball_x in range(paddle_x, paddle_x + paddle_length) and ball_y == 3:
        change_y *= -1
        score += 1
        if time > 150:
            time -= 10

    ball_x += change_x
    ball_y += change_y

    if button_b.was_pressed() and paddle_x < 3:
        paddle_x += 1

    if button_a.was_pressed() and paddle_x > 0:
        paddle_x -= 1

    # draw
    display.clear()
    for i in range(paddle_length):
        display.set_pixel(paddle_x + i, paddle_y, 9)

    display.set_pixel(ball_x, ball_y, 9)
    sleep(time)

# game over
display.show(Image.DUCK)
speech.say('Game Over')

# save score
if score > highscore:
    with open(FILE_NAME, 'w') as file:
        file.write(str(score))
display.scroll(score)


