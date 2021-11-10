import pygame as pg
from BanDo import *
import time

class NhanVat():
	def __init__(self, i, j, img, bando):
		self.i=i
		self.j=j
		self.image = pg.image.load(img)
		self.banDo=bando
		self.xThat=self.j*self.banDo.KTI
		self.yThat=self.i*self.banDo.KTI
	def draw(self,screen):
		screen.blit(self.image,(self.xThat,self.yThat))

	def move(self,screen, huong='d', fps=30):
		hop=self.banDo.KTI//fps
		if huong=='r':
			if self.j < len(self.banDo.matran[0])-1 and self.banDo.matran[self.i][self.j+1]!=1:
				tmp=self.xThat+self.banDo.KTI-hop

				while self.xThat<tmp:
					self.xThat+=hop
					self.draw(screen)
					time.sleep(1/fps)
					pg.display.flip()
				self.xThat=tmp+hop
				self.draw(screen)
				self.j+=1
		elif huong=='l':
			if self.j > 0 and self.banDo.matran[self.i][self.j-1]!=1:
				tmp=self.xThat-self.banDo.KTI+hop

				while self.xThat>tmp:
					self.xThat-=hop
					self.draw(screen)
					time.sleep(1/fps)
					pg.display.flip()
				self.xThat=tmp-hop
				self.draw(screen)
				self.j-=1
		elif huong=='u':
			if self.i > 0 and self.banDo.matran[self.i-1][self.j]!=1:
				tmp=self.yThat-self.banDo.KTI+hop

				while self.yThat>tmp:
					self.yThat-=hop
					self.draw(screen)
					time.sleep(1/fps)
					pg.display.flip()
				self.yThat=tmp-hop
				self.draw(screen)
				self.x-=1
		elif huong=='d':
			if self.i < len(self.banDo.matran)-1 and self.banDo.matran[self.i+1][self.j]!=1:
				tmp=self.yThat+self.banDo.KTI-hop

				while self.yThat<tmp:
					self.yThat+=hop
					self.draw(screen)
					time.sleep(1/fps)
					pg.display.flip()
				self.yThat=tmp+hop
				self.draw(screen)
				self.j+=1


def main():



	matrix1=[
		[0,1,0,1,1,0],
		[0,0,0,0,0,0],
		[1,0,1,0,1,0],
		[0,0,1,0,0,0],
		[1,0,0,1,0,0]
	]




	screen = pg.display.set_mode((KTI*len(matrix1[0]), KTI*len(matrix1))) # 1 man hinh du lon de chua map và du thêm buffer 

	clock = pg.time.Clock()

	map0 = BanDo(matrix1, KTI)

	pacman=NhanVat(1,1,"player.png", map0)

	done = False

	while not done:

		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True

		map0.draw(screen)

		pacman.draw(screen)
		pacman.move(screen)

		pg.display.flip()
		clock.tick(30)


if __name__ == '__main__':
	main()
	pg.quit()