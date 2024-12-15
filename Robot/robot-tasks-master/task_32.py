#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    n = 0
    while wall_is_beneath():
        if wall_is_above():
            if cell_is_filled():
                n += 1
            else:
                fill_cell()
        elif not wall_is_above():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    n += 1
                else:
                    fill_cell()

            while not wall_is_beneath():
                move_down()
        move_right()
    mov('ax', n)

    mov('ax', n)
    pass


if __name__ == '__main__':
    run_tasks()
