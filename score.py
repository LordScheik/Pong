from microbit import *
import os

FILE_NAME = 'score.txt'

highscore = 0
score = 0

# read saved highscore
for file_name in os.listdir():
    if file_name == FILE_NAME:
        with open(file_name) as file:
            highscore = int(file.read())

display.scroll(highscore)

while True:
    # reset score
    if button_a.was_pressed():
        score = 0
        display.scroll(score)
    # increase score
    elif button_b.was_pressed():
        score += 1
        # save score
        if score > highscore:
            with open(FILE_NAME, 'w') as file:
                file.write(str(score))
        display.scroll(score)
