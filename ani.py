class Animation():
	def __init__(self,*imgList):
		
		self.image_list = []
		
		for img in imgList:
			self.image_list.append(img)
	

		self.index = 0
		
		self.clock = 1

	def currentImage(self):
		return self.image_list[self.index]

	def get_length(self):
		return len(self.image_list)

	def update(self,fps=30):
		step = 30 // fps
		l = range(1,30,step)
		if self.clock == 30:
			self.clock = 1
		else:
			self.clock += 1

		if self.clock in l:
			# Increase index
			self.index += 1
			if self.index == len(self.image_list):
				self.index = 0
