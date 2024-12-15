#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    # def flag_door_left():
    #     flag = False
    #     while not wall_is_on_the_left():
    #         if not wall_is_beneath():
    #             flag = True
    #         move_left()
    #         if not wall_is_beneath():
    #             flag = True
    #     return flag
    #
    # def down_and_right():
    #     while wall_is_beneath() and not wall_is_on_the_right():
    #         move_right()
    #     if not wall_is_beneath():
    #         move_down()
    #     while not wall_is_on_the_right():
    #         move_right()
    #
    # while not wall_is_on_the_left():
    #     move_left()
    # n = True
    #
    # while n:
    #     flag_door_left()
    #     down_and_right()
    #     if not flag_door_left():
    #         break
    flag_search_door = True
    while flag_search_door:
        flag_search_door = False
        while not wall_is_on_the_right():
            move_right()
            while not wall_is_beneath():
                move_down()
                flag_search_door = True

        while not wall_is_on_the_left():
            move_left()
            while not wall_is_beneath():
                move_down()
                flag_search_door = True

if __name__ == '__main__':
    run_tasks()
