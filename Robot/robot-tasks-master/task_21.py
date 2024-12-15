#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    def color_line_from_start(steps):
        i = 1
        while i <= steps:
            move_right()
            fill_cell()
            i += 1
        move_left(i - 1)
    lines_total = 15
    line_current = 1
    while line_current < lines_total - 1:
        move_down()
        line_current += 1
        color_line_from_start(line_current - 1)
    move_down()
    move_right()
    pass


if __name__ == '__main__':
    run_tasks()
