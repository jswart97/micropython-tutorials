# Flappy Bit Game!
import music
from microbit import (accelerometer,
                      display,
                      sleep,
                      Image,
                      reset,
                      )

display.scroll('Happy?')

bird = 2
terrain = [
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 2),
    (0, 0),
    (0, 0),
    (3, 0),
    (3, 0),
    (4, 0),
    (3, 0),
    (0, 0),
    (0, 0),
    (0, 1),
    (2, 0),
    (3, 0),
    (4, 0),
    (3, 0),
    (0, 0),
    (0, 1),
    (2, 0),
]

terrain_multiplier = 5
pos = 0

while True:
    sleep(100)
    if -256 < accelerometer.get_y() < 200:
        bird = max(0, bird - 1)
    elif 568 < accelerometer.get_y() < 1024:
        bird = min(4, bird + 1)

    display.clear()
    display.set_pixel(0, bird, 9)

    pos_terrain = pos // terrain_multiplier
    lost_status = False
    for column, (top, bottom) in enumerate(
            terrain[pos_terrain:pos_terrain + 5]):
        for y in range(top):
            display.set_pixel(column, y, 4)
            if column == 0 and bird == y:
                lost_status = True
        for y in range(bottom):
            display.set_pixel(column, 4 - y, 4)
            if column == 0 and bird == (4 - y):
                lost_status = True
    if lost_status:
        display.show(Image.SAD)
        music.play(music.FUNERAL)
        reset()
    pos += 1
    if pos_terrain > len(terrain):
        pos = 0