class Animation():
	def __init__(self,*imgList):
		
		self.image_list = []
		for img in imgList:
			self.image_list.append(img)
	
		self.index = 0
		self.clock = 1

	def currentImage(self):
		return self.image_list[self.index]


	def update(self,fps=30):
		step = 30 // fps#bước nhảy bằng 30 chia hết cho số fps truyền vào
		l = range(1,30,step)#ở đây fps truyền vào mặc định là 30 nên step sẽ là 1
		if self.clock == 30:#nếu clock =30 thì t xét nó lại =1 còn nếu ch tới thì +1 clock
			self.clock = 1
		else:
			self.clock += 1
		if self.clock in l:#nếu số clock nằm trong l
			self.index += 1#index+=1
			if self.index == len(self.image_list):
				self.index = 0
