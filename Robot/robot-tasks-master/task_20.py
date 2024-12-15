#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    i = 0
    move_right()
    while i < 6:
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        move_down()
        move_left()
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
        move_down()
        move_right()
        i += 1
    pass


if __name__ == '__main__':
    run_tasks()
