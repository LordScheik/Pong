from microbit import *
import speech

paddle_x = 2
paddle_y = 4
paddle_length = 2

ball_x = 3
ball_y = 1

change_x = 1
change_y = 1

ANIMATION_SPEED = 150

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


display.scroll('Start')
speech.say('Start')

for i in range(paddle_length):
    display.set_pixel(paddle_x + i, paddle_y, 9)
display.set_pixel(ball_x, ball_y, 9)
sleep(500)

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
    sleep(500)

# game over
display.show(Image.DUCK)
speech.say('Game Over')
