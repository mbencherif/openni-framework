import pygame
from openni import *
import random

from skeleton import Skeleton

class User:
	def __init__(self, id, skel_cap, depth_generator):
		self.id = id
		self.skeleton = Skeleton(self, skel_cap, depth_generator)

		self.depth = 0
		self.face = None
		self.image_path = ''

		self.choose_image()
	# __init__

	def update(self):
		self.skeleton.update()
	# update

	def draw(self, surface):
		if self.skeleton.status:
			rate = 900/(self.depth-500)
			if rate < 0: rate = 0

			try:
				transformed_image = pygame.transform.scale(self.face, (int(self.face.get_width()*rate), int(self.face.get_height()*rate)))
				surface.blit(transformed_image, (self.skeleton.head[0]-0.5*transformed_image.get_width(), self.skeleton.head[1]-0.3*transformed_image.get_height()))
			except:
				pass
			# try
		# if
	# draw

	def draw_skeleton(self, surface):
		if self.skeleton.status:
			self.skeleton.draw(surface)
	# draw_skeleton

	def choose_image(self, banned_image='none'):
		images = ['forever.png', 'lol.png', 'poker.png', 'spider.png', 'troll.png', 'fuckyeah.png']
		try:
			images.remove(banned_image)
		except:
			pass

		random.shuffle(images)
		self.image_path = images[0]
		self.face = pygame.image.load('images/%s' % self.image_path)
	# choose_image

	def refresh(self):
		self.choose_image(self.image_path)
	# refresh
# User
