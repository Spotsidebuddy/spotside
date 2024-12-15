#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
    while wall_is_on_the_right() == False:
        move_right()
    pass


if __name__ == '__main__':
    run_tasks()
