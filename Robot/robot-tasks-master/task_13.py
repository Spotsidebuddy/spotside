#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    '''Это вот мое решение, но ниже - более элегантное'''
    # while wall_is_above() == True:
    #     move_right()
    # move_up()
    # while wall_is_on_the_left() == False:
    #     move_left()
    # while wall_is_on_the_right() == False:
    #     if wall_is_beneath() == False:
    #         fill_cell()
    #     move_right()
    # if wall_is_beneath() == False:
    #     fill_cell()
    # while cell_is_filled() == False:
    #     move_left()
    # move_down()
    # while wall_is_beneath():
    #     move_left()
    # move_down()
    # while wall_is_on_the_left() == False:
    #     move_left()
    # while wall_is_on_the_right() == False:
    #     if wall_is_above() == False:
    #         fill_cell()
    #     move_right()
    # if not wall_is_above():
    #     fill_cell()
    # while wall_is_above():
    #     move_left()
    # move_up()
    # while not wall_is_on_the_right():
    #     move_right()
    # pass

    def fill_up_down():
        if not wall_is_above():
            move_up()
            fill_cell()
            move_down()
        if not wall_is_beneath():
            move_down()
            fill_cell()
            move_up()

    fill_up_down()
    while not wall_is_on_the_right():
        move_right()
        fill_up_down()

if __name__ == '__main__':
    run_tasks()
