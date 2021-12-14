from numpy import False_
import pygame
import random

from BanDo import *

from Char import getPosB,getCoo,getPosB,NhanVat

class Slime(NhanVat):

	def __init__(self,img, i, j, bando,speed=5):
		NhanVat.__init__(self,i, j, bando)
		self.image=pygame.image.load(img).convert()
		self.image.set_colorkey(BLACK)
		self.rect=self.image.get_rect()
		self.KTI=self.rect.width
		self.speed=speed
		self.dx=0
		self.dy=0
		self.huong="r"
		self.daDoi=True
		self.explosion=False

	def moveRight(self):
		self.dx=self.speed
	def moveLeft(self):
		self.dx=-self.speed
	def moveUp(self): 
		self.dy=-self.speed
	def moveDown(self):
		self.dy=self.speed

	def setPosSlime(self,i,j,mode=0):
		if mode==0:
			self.x=j*self.banDo.KTI+self.KTI//4
			self.y=i*self.banDo.KTI	+self.KTI//4
		
	def rape(self,pacman):
		if pacman.mode==0:
			for x,y in getPosB(pacman.KTI,pacman.x,pacman.y).values():
				if self.x<x<self.x+self.KTI and self.y<y<self.y+self.KTI:
					return True
		return False

	

	def update(self):
		if self.explosion==False:
		
			if self.huong=="r":
				self.moveRight()
			elif self.huong=="l":
				self.moveLeft()
			elif self.huong=="u":
				self.moveUp()
			elif self.huong=="d":
				self.moveDown()

			pos=getPosB(self.rect.width,self.x,self.y)

			i,j=getCoo(self.rect.width,self.x,self.y)

			if self.huong=="u" and (pos["U"][1]<=0 or (self.banDo.matran[i-1][j]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i-1,j)].isIn(*pos["U"]))) :
				self.setPosSlime(i,j)
				self.huong=random.choice(("r","l","d"))


			if self.huong=="l" and (pos["L"][0]<=0 or (self.banDo.matran[i][j-1]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i,j-1)].isIn(*pos["L"]))) :
				self.setPosSlime(i,j)
				self.huong=random.choice(("r","d","u"))				


			if self.huong=="r" and ((pos["R"][0]>=KTI*self.banDo.IPSR-self.speed) or ((j < self.banDo.IPSR-1 and self.banDo.matran[i][j+1]==1) and self.banDo.banDo[f2t1(self.banDo.IPSR,i,j+1)].isIn(*pos["R"]))) :
				self.setPosSlime(i,j)
				self.huong=random.choice(("u","l","d"))
					

					
			if self.huong=="d" and ((pos["D"][1]>=KTI*self.banDo.IPS-self.speed) or ((i < self.banDo.IPS-1 and self.banDo.matran[i+1][j]==1) and self.banDo.banDo[f2t1(self.banDo.IPSR,i+1,j)].isIn(*pos["D"]))) :
				self.setPosSlime(i,j)
				self.huong=random.choice(("r","l","u"))

			
			if self.banDo.matran[i][j]!=3: self.daDoi=False
		

			if self.banDo.matran[i][j]==3 and self.daDoi==False and pos["C"]:
				self.huong=random.choice(("r","l","u","d"))

				print("doihuong")
				if self.huong=="r" and j<self.banDo.IPSR-1 and self.banDo.matran[i][j+1] !=1 :
					
						self.daDoi=True
						self.setPosSlime(i,j)
				#		 self.x-=KTI//3+self.speed

				if self.huong=="l" and  j>0 and self.banDo.matran[i][j-1] !=1 :
					
						self.daDoi=True
						self.setPosSlime(i,j)
				#		 self.x+=KTI//3-self.speed

				if self.huong=="u" and i>0 and self.banDo.matran[i-1][j] !=1 :
					
						self.daDoi=True
						self.setPosSlime(i,j)
				#		 self.y+=KTI//3-self.speed
				if self.huong=="d" and i<self.banDo.IPS-1 and self.banDo.matran[i+1][j] !=1 :
					
						self.daDoi=True
						self.setPosSlime(i,j)
				#		 self.y-=KTI//3+self.speed

			self.x += self.dx
			self.y += self.dy
			self.dx=0
			self.dy=0
		else:
			self.biRape()
	
	def biRape(self):
		self.setPosSlime(9,10)
		self.explosion=False
    		

def main():
	pygame.init()
	matrix1=[
		[0,1,0,1,1,0,0],
		[0,3,0,3,0,3,1],
		[1,0,1,0,1,0,1],
		[0,0,1,0,0,3,1],
		[1,0,0,1,0,1,1],
		[0,0,0,0,3,0,1],
		[0,1,0,1,1,0,0],
	]
	
	screen=pygame.display.set_mode((KTI*len(matrix1[0]),KTI*len(matrix1)+KTI))

	clock=pygame.time.Clock()
	map0=BanDo(matrix1,KTI)

	slime=Slime(3,3,map0)
	slime2=Slime(1,3,map0)

	

	run=True

	while run:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False
			
		
	
		map0.draw(screen)
		slime.draw(screen)

		slime.update()
		slime2.draw(screen)

		slime2.update()

		pygame.display.flip()
		clock.tick(20)

if __name__=='__main__':
	main()
	

	