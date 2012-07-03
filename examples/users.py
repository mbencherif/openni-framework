#!/usr/bin/python

from openni import *
import pygame
from pygame.locals import *
import numpy
import cv

from main import Main
from manager import Manager
from user import User
from recorder import Recorder

main = Main('users', (1280, 480))
# recorder = Recorder()
# recorder.start()

rgb = pygame.Surface((640, 480))
black = pygame.Surface((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            main.user_manager.refresh()
    # for

    main.update()

    rgb_frame = main.capture_rgb()

    rgb.blit(rgb_frame, (0, 0))
    black.fill((0, 0, 0))

    main.user_manager.update()
    main.user_manager.draw_skeletons(black)
    main.user_manager.draw(rgb)

    main.screen.blit(rgb, (0, 0))
    main.screen.blit(black, (640, 0))

    # recorder.add(main.screen)

    pygame.display.flip()
# while