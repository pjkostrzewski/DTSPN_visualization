import pygame
import pygame.gfxdraw
from random import randint
from math import pi, atan2
from time import sleep
from Car import Car
from itertools import cycle
import copy
import math
from FileManager import FilesOperations
import os


build_path = "../../build"
SIZE = 800
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
BACK_COLOR = (30, 30, 30)
RADIUS_START = 20
TURN_START = 10

pygame.init()


def remove_files(*paths):
    for path in paths:
        try:
            os.remove(path)
        except FileNotFoundError as e:
            print(e)
            pass


def run_dtspn_exe(path, exe_file):
    os.system(f"cd {path} && ./{exe_file}")


def convert_from_radians(rad):
    return rad * 180 / math.pi
