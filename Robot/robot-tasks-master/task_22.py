#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    def color_line():
        n = 0
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
            n += 1
        fill_cell()
        if not wall_is_on_the_left():
            move_left(n)

    while not wall_is_beneath():
        color_line()
        move_down()
    color_line()
    pass


if __name__ == '__main__':
    run_tasks()
