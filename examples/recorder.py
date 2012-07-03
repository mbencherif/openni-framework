import pygame
from threading import Thread

class Recorder(Thread):
	def __init__(self):
		Thread.__init__(self)

		self.frames = []
		self.index = 0
	# __init__

	def run(self):
		while True:
			if len(self.frames) > 0:
				frame = self.frames.pop(0)
				pygame.image.save(frame, 'frames/frame%06d.png' % self.index)
				self.index += 1
			# if
		# while
	# run

	def add(self, frame):
		self.frames.append(frame)
	# add
# Recorder