#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    def gotostart():
        move_down()


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

    def next_position_horizontal():
        move_right(4)


    gotostart()
    for i in range(4):
        draw_cross_and_reset()
        next_position_horizontal()
    draw_cross_and_reset()

if __name__ == '__main__':
    run_tasks()
