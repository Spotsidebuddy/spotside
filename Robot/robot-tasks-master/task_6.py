#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    while wall_is_beneath() == False:
        move_right()
    while wall_is_beneath() == True:
        move_right()
    pass


if __name__ == '__main__':
    run_tasks()
