from openni import *

from manager import Manager
from user import User

class UserManager(Manager):
	def __init__(self, context, depth_generator):
		Manager.__init__(self)

		self.depth_generator = depth_generator

		self.user_generator = UserGenerator()
		self.user_generator.create(context)

		self.user_generator.register_user_cb(self.new_user, self.lost_user)

		self.skel_cap = self.user_generator.skeleton_cap
		self.skel_cap.set_profile(SKEL_PROFILE_ALL)
	# __init__

	def draw_skeletons(self, surface):
		for user in self.objects:
			user.draw_skeleton(surface)
	# draw_skeletons

	def refresh(self):
		for user in self.objects:
			user.refresh()
	# refresh

	def new_user(self, src, id):
		self.skel_cap.start_tracking(id)
		self.add(User(id, self.skel_cap, self.depth_generator))
	# new_user

	def lost_user(self, src, id):
		self.remove_by_id(id)
	# lost_user
# UserManager