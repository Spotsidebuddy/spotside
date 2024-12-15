#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    steps = 0
    chksm = steps
    while not wall_is_on_the_right():
        if steps < chksm:
            move_right()
            steps += 1
        else:
            steps = 0
            chksm += 1
            move_right()
            if not wall_is_on_the_right():
                fill_cell()


if __name__ == '__main__':
    run_tasks()
