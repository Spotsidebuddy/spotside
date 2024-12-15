#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
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


    def do_a_line(n=1):
        for i in range(n - 1):
            draw_cross_and_reset()
            next_position_horizontal()
        draw_cross_and_reset()


    def move_to_next_line():
        move_down(4)
        while not wall_is_on_the_left():
            move_left()

    def go_to_linestart():
        while not wall_is_on_the_left():
            move_left()

    for i in range(4):
        do_a_line(10)
        move_to_next_line()
    do_a_line(10)
    go_to_linestart()



if __name__ == '__main__':
    run_tasks()
