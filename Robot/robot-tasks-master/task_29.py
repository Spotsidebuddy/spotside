#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    n = 0
    if cell_is_filled():
        n += 1
    while n != 3:
        if not wall_is_on_the_right():
            move_right()
        if cell_is_filled():
            n+= 1
        # if not cell_is_filled():
        else:
            n = 0



if __name__ == '__main__':
    run_tasks()
