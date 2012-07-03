#!/usr/bin/python

from openni import *
import pygame
import numpy
import cv

from main import Main
from manager import Manager
from user import User

main = Main('users', (1280, 480))

rgb = pygame.Surface((640, 480))
black = pygame.Surface((640, 480))

while True:
    main.update()

    rgb_frame = main.capture_rgb()
    rgb.blit(rgb_frame, (0, 0))

    black.fill((0, 0, 0))

    main.user_manager.update()
    main.user_manager.draw(black)

    main.screen.blit(rgb, (0, 0))
    main.screen.blit(black, (640, 0))

    pygame.display.flip()
# while