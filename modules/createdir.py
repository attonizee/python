#!/bin/python3

import os, sys

def create_dir(name):
    for i in range(1,10):
        os.mkdir(f'{name}_{i}')


def delete_dir(name):
    for dir in os.listdir():
        if dir.rfind(name) != -1:
            os.removedirs(dir)
        else:
            pass
