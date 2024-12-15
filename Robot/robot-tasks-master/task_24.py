#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    def gotostart():
        move_down()
        move_right()


    def draw_cross_and_reset():
        move_right()
        fill_cell()
        move_down()
        fill_cell()
        move_down()
        fill_cell()
        move_right()
        move_up()
        fill_cell()
        move_left(2)
        fill_cell()
        move_up()

    gotostart()
    draw_cross_and_reset()

if __name__ == '__main__':
    run_tasks()
