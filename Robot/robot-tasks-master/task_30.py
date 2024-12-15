#!/usr/bin/python3

from pyrob.api import *


# def draw_cycle(side):
#     side = side()
#     i = 1
#     while i < side:
#         move_right()
#         fill_cell()
#         i += 1
#     move_right()


@task(delay=0.01)
def task_9_3():
    def side():
        length = 1
        while not wall_is_on_the_right():
            move_right()
            length += 1
        move_left(length - 1)
        return length

    sq_side = side()

    def draw_square(side):
        i = 0
        move_right()
        while i < side:
            fill_cell()
            move_right()
            i += 1
        move_down()
        i = 0
        while i < side:
            fill_cell()
            move_down()
            i += 1
        move_left()
        i = 0
        while i < side:
            fill_cell()
            move_left()
            i += 1
        move_up()
        i = 0
        while i < side:
            fill_cell()
            move_up()
            i += 1
        move_down()
        move_right()

    side = sq_side - 2
    cycles = sq_side // 2
    k = 1
    while k <= cycles:
        draw_square(side)
        side -= 2
        k += 1

    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()


if __name__ == '__main__':
    run_tasks()
