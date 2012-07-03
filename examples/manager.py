class Manager:
	def __init__(self):
		self.objects = []
	# __init__

	def add(self, object):
		self.objects.append(object)
	# add

	def remove(self, object):
		self.objects.remove(object)
	# remove

	def remove_by_value(self, attribute, value, multiples=False):
		for object in self.objects:
			if getattr(object, attribute) is value:
				self.remove(object)
				
				if not multiples: return
			# if
		# for
	# remove_by_value

	def remove_by_id(self, id):
		self.remove_by_value('id', id)
	# remove_by_id

	def remove_by_index(self, index):
		self.objects.pop(index)
	# remove_by_index

	def find(self, object_to_find):
		for object in self.objects:
			if object is object_to_find:
				return object
		# for
	# find

	def find_by_value(self, attribute, value):
		for object in self.objects:
			if getattr(object, attribute) is value:
				return object
		# for
	# find_by_value

	def update(self):
		for object in self.objects:
			object.update()
	# update

	def draw(self, surface):
		for object in self.objects:
			object.draw(surface)
	# draw
# Manager
