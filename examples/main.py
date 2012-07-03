import pygame
from openni import *
import numpy
import cv

from user_manager import UserManager

class Main:
	def __init__(self, screen_title='OpenNI', screen_size=(640, 480), res=RES_VGA, fps=30):
		self.context = Context()
		self.context.init()

		self.res = res
		self.fps = fps

		self.depth_generator = DepthGenerator()
		self.depth_generator.create(self.context)
		self.depth_generator.set_resolution_preset(self.res)
		self.depth_generator.fps = self.fps

		self.image_generator = ImageGenerator()
		self.image_generator.create(self.context)
		self.image_generator.set_resolution_preset(self.res)
		self.image_generator.fps = self.fps

		self.user_manager = UserManager(self.context, self.depth_generator)

		self.context.start_generating_all()

		pygame.init()
		self.screen = pygame.display.set_mode(screen_size)
		pygame.display.set_caption(screen_title)
	# __init__

	def capture_rgb(self):
		rgb_frame = numpy.fromstring(self.image_generator.get_raw_image_map_bgr(), dtype=numpy.uint8).reshape(480, 640, 3)
		image = cv.fromarray(rgb_frame)
		cv.CvtColor(cv.fromarray(rgb_frame), image, cv.CV_BGR2RGB)
		pyimage = pygame.image.frombuffer(image.tostring(), cv.GetSize(image), 'RGB')

		return pyimage
	# capture_rgb

	def update(self):
		n_ret_val = self.context.wait_one_update_all(self.image_generator)
		cv.WaitKey(10)
	# update
# Main
