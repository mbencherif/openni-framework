import pygame
from openni import *

class User:
	def __init__(self, id, skel_cap, depth_generator):
		self.id = id
		self.skel_cap = skel_cap
		self.depth_generator = depth_generator

		self.color = (0, 255, 0)
		self.depth = 0

		self.head = (0, 0)
		self.neck = (0, 0)
		self.torso = (0, 0)
		self.waist = (0, 0)

		self.left_shoulder = (0, 0)
		self.left_elbow = (0, 0)
		self.left_hand = (0, 0)
		self.left_hip = (0, 0)
		self.left_knee = (0, 0)
		self.left_foot = (0, 0)

		self.right_shoulder = (0, 0)
		self.right_elbow = (0, 0)
		self.right_hand = (0, 0)
		self.right_hip = (0, 0)
		self.right_knee = (0, 0)
		self.right_foot = (0, 0)
	# __init__

	def update(self):
		self.tracking = True

		self.set('head', self.skel_cap.get_joint_position(self.id, SKEL_HEAD))
		self.set('neck', self.skel_cap.get_joint_position(self.id, SKEL_NECK))
		self.set('torso', self.skel_cap.get_joint_position(self.id, SKEL_TORSO))
		self.set('left_shoulder', self.skel_cap.get_joint_position(self.id, SKEL_LEFT_SHOULDER))
		self.set('left_elbow', self.skel_cap.get_joint_position(self.id, SKEL_LEFT_ELBOW))
		self.set('left_hand', self.skel_cap.get_joint_position(self.id, SKEL_LEFT_HAND))
		self.set('left_hip', self.skel_cap.get_joint_position(self.id, SKEL_LEFT_HIP))
		self.set('left_knee', self.skel_cap.get_joint_position(self.id, SKEL_LEFT_KNEE))
		self.set('left_foot', self.skel_cap.get_joint_position(self.id, SKEL_LEFT_FOOT))
		self.set('right_shoulder', self.skel_cap.get_joint_position(self.id, SKEL_RIGHT_SHOULDER))
		self.set('right_elbow', self.skel_cap.get_joint_position(self.id, SKEL_RIGHT_ELBOW))
		self.set('right_hand', self.skel_cap.get_joint_position(self.id, SKEL_RIGHT_HAND))
		self.set('right_hip', self.skel_cap.get_joint_position(self.id, SKEL_RIGHT_HIP))
		self.set('right_knee', self.skel_cap.get_joint_position(self.id, SKEL_RIGHT_KNEE))
		self.set('right_foot', self.skel_cap.get_joint_position(self.id, SKEL_RIGHT_FOOT))

		self.waist = ((self.left_hip[0]+self.right_hip[0])/2, (self.left_hip[1]+self.right_hip[1])/2)
		self.depth = self.skel_cap.get_joint_position(self.id, SKEL_HEAD).point[2]
	# update

	def draw(self, surface):
		self.draw_line(surface, self.head, self.neck)
		self.draw_line(surface, self.neck, self.torso)
		self.draw_line(surface, self.torso, self.waist)

		self.draw_line(surface, self.left_shoulder, self.right_shoulder)

		self.draw_line(surface, self.left_shoulder, self.left_elbow)
		self.draw_line(surface, self.left_elbow, self.left_hand)
		self.draw_line(surface, self.left_hip, self.left_knee)
		self.draw_line(surface, self.left_knee, self.left_foot)

		self.draw_line(surface, self.left_hip, self.right_hip)

		self.draw_line(surface, self.right_shoulder, self.right_elbow)
		self.draw_line(surface, self.right_elbow, self.right_hand)
		self.draw_line(surface, self.right_hip, self.right_knee)
		self.draw_line(surface, self.right_knee, self.right_foot)
	# draw

	def draw_line(self, surface, start_point, end_point):
		pygame.draw.line(surface, self.color, (start_point[0], start_point[1]), (end_point[0], end_point[1]), 5)
	# draw_line

	def set(self, joint, pos):
		projective_pos = self.depth_generator.to_projective([pos.point])[0]
		setattr(self, joint, projective_pos)
	# set
# User
