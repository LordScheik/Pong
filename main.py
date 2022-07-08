from microbit import *

paddle_x = 2
paddle_y = 4
paddle_length = 2

ball_x = 2
ball_y = 0
ball_length = 1

change_x = 1
change_y = 1



while True:
    while ball_y < 3:

        if button_b.was_pressed() and paddle_x < 3:
            paddle_x += 1
            display.clear()

        if button_a.was_pressed() and paddle_x > 0:
            paddle_x -= 1
            display.clear()

        for i in range(paddle_length):
            display.set_pixel(paddle_x + i, paddle_y, 9)

        display.set_pixel(ball_x, ball_y, 9)
        sleep(500)
        display.clear()
        ball_y += 1

    while ball_y > 0:
        if button_b.was_pressed() and paddle_x < 3:
            paddle_x += 1
            display.clear()

        if button_a.was_pressed() and paddle_x > 0:
            paddle_x -= 1
            display.clear()

        for i in range(paddle_length):
            display.set_pixel(paddle_x + i, paddle_y, 9)

        display.set_pixel(ball_x, ball_y, 9)
        sleep(500)
        display.clear()
        ball_y -= 1










#    while True:
#                        #von oben mitte nach Rechts mitte
#    while ball_x < 4:
#        if button_b.was_pressed() and paddle_x < 3:
#            paddle_x += 1
#            display.clear()
#
#        if button_a.was_pressed() and paddle_x > 0:
#            paddle_x -= 1
#            display.clear()
#
#        for i in range(paddle_length):
#            display.set_pixel(paddle_x + i, paddle_y, 9)
#
#        display.set_pixel(ball_x, ball_y, 9)
#        sleep(500)
#        display.clear()
#        ball_x += 1
#        ball_y += 1
#                        #von rechts mitte nach unten mitte
#    while ball_y < 4:
#        if button_b.was_pressed() and paddle_x < 3:
#            paddle_x += 1
#            display.clear()
#
#        if button_a.was_pressed() and paddle_x > 0:
#            paddle_x -= 1
#            display.clear()
#
#        for i in range(paddle_length):
#            display.set_pixel(paddle_x + i, paddle_y, 9)
#
#        display.set_pixel(ball_x, ball_y, 9)
#        sleep(500)
#        display.clear()
#        ball_x -= 1
#        ball_y += 1
#                        #von unten mitte nacht links mitte
#    while ball_x > 0:
#        if button_b.was_pressed() and paddle_x < 3:
#            paddle_x += 1
#            display.clear()
#
#        if button_a.was_pressed() and paddle_x > 0:
#            paddle_x -= 1
#            display.clear()
#
#        for i in range(paddle_length):
#            display.set_pixel(paddle_x + i, paddle_y, 9)
#
#        display.set_pixel(ball_x, ball_y, 9)
#        sleep(500)
#        display.clear()
#        ball_x -= 1
#        ball_y -= 1
#                            # von links mitte nach oben mitte
#    while ball_y > 0:
#        if button_b.was_pressed() and paddle_x < 3:
#            paddle_x += 1
#            display.clear()
#
#        if button_a.was_pressed() and paddle_x > 0:
#            paddle_x -= 1
#            display.clear()
#
#        for i in range(paddle_length):
#            display.set_pixel(paddle_x + i, paddle_y, 9)
#
#        display.set_pixel(ball_x, ball_y, 9)
#        sleep(500)
#        display.clear()
#        ball_x += 1
#        ball_y -= 1tton_a.was_pressed() and paddle_x > 0:
