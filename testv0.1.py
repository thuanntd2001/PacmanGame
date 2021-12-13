import pygame
from BanDo import *
import time




def getPosB(KTI,x,y):
	return {"U":(x+KTI//2,y),"D":(x+KTI//2,y+KTI),"L":(x,y+KTI//2),"R":(x+KTI,y+KTI//2),"C":(x+KTI//2,y+KTI//2),"UL":(x,y),"UR":(x+KTI,y),"DL":(x,y+KTI),"DR":(x+KTI,y+KTI)}

def getCen(KTI,x,y):
	return (x+KTI//2,y+KTI//2)

def getCoo(KTIanh,x,y):
	center= getCen(KTIanh,x,y)
	print(center)
	return int(center[1]/KTI),int(center[0]/KTI)

class NhanVat():
	def __init__(self, i, j, bando):

		self.banDo=bando
		self.x=j*self.banDo.KTI
		self.y=i*self.banDo.KTI
	
	def draw(self,screen):
		screen.blit(self.image,(self.x,self.y))

	def setPos(self,i,j, mode=0):
		if mode==0:
			self.x=j*self.banDo.KTI+KTI//4
			self.y=i*self.banDo.KTI	+KTI//4
		if mode==1:
			self.x=j*self.banDo.KTI+KTI//4
		if mode==2:
			self.y=i*self.banDo.KTI	+KTI//4

class Pacman(NhanVat):

	explosion = False
	game_over = False
	def __init__(self, i, j, bando, speed=5):
		NhanVat.__init__(self,i,j,bando)
		self.player_image=pygame.image.load("Player.png")
		self.image = self.player_image.convert()
		self.image.set_colorkey(BLACK)
		self.rect= self.image.get_rect()                                                                       #pygame.Rect((self.x+self.image.get_width()//4,self.y+self.image.get_height()//4),(self.image.get_width()*1.5,self.image.get_height()*1.5))
		self.KTI=self.rect.width
		self.speed=speed
		self.dx=0
		self.dy=0
		self.huong="s"
		self.point=0



	def moveR(self):
		self.dx=self.speed
	def moveL(self):
		self.dx=-self.speed
	def moveU(self):
		self.dy=-self.speed
	def moveD(self):
		self.dy=self.speed


	def stand(self):
		self.image = self.player_image
		self.dx=self.dy=0



	def stop_move_left(self,i,j):
		if self.dx < 0:
			self.image = pygame.transform.flip(self.player_image,True,False)
			self.dx = 0

	def stop_move_up(self,i,j):
		if self.dy < 0:
			self.image = pygame.transform.rotate(self.player_image,90)
			self.dy = 0

	def stop_move_down(self,ic,jc):
		if self.dy > 0:
			self.image = pygame.transform.rotate(self.player_image,270)
			self.dy = 0
	def stop_move_right(self,ic,jc):
		if self.dx > 0:
			self.image = self.player_image
			self.dx = 0
	

	def update(self,huong="u"):
		if not self.explosion:

			if huong=="s":
				self.stand()
			if huong=="d":
				self.moveD()
			if huong=="u":
				self.moveU()
			if huong=="r":
				self.moveR()
			if huong=="l":
				self.moveL()


			
			pos=getPosB(self.rect.width,self.x,self.y)

			print(pos)

			i,j=getCoo(self.rect.width,self.x,self.y)

			

			if huong=="u" and (pos["U"][1]<=0 or (self.banDo.matran[i-1][j]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i-1,j)].isIn(*pos["U"]))) :
				self.stop_move_up(i,j)


			if huong=="l" and (pos["L"][0]<=0 or (self.banDo.matran[i][j-1]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i,j-1)].isIn(*pos["L"]))) :
				self.stop_move_left(i,j)				


			if huong=="r" and ((pos["R"][0]>=KTI*self.banDo.IPSR-self.speed) or ((j < self.banDo.IPSR-1 and self.banDo.matran[i][j+1]==1) and self.banDo.banDo[f2t1(self.banDo.IPSR,i,j+1)].isIn(*pos["R"]))) :
				self.stop_move_right(i,j)
				

				
			if huong=="d" and ((pos["D"][1]>=KTI*self.banDo.IPS-self.speed) or ((i < self.banDo.IPS-1 and self.banDo.matran[i+1][j]==1) and self.banDo.banDo[f2t1(self.banDo.IPSR,i+1,j)].isIn(*pos["D"]))) :
				self.stop_move_down(i,j)


			A=(pos["U"][1]<=0) #toi canh bien hoac
			B=C=False
			if j>0 and i>0 and (j < self.banDo.IPSR-1) and (i < self.banDo.IPS-1):
				B=self.banDo.matran[i-1][j-1]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i-1,j-1)].isIn(*pos["UL"]) ##goc tren trai dung tuong tren trai hoac
				C=self.banDo.matran[i-1][j+1]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i-1,j+1)].isIn(*pos["UR"]) ##goc tren phai dung tuong tren phai

			if huong=="u" and (A or B or C):
			
				self.stop_move_up(i,j)
				self.setPos(i,j,1)


			A=(pos["L"][1]<=0) #toi canh bien hoac
			B=C=False
			if j>0 and i>0 and (j < self.banDo.IPSR-1) and (i < self.banDo.IPS-1):
				B=self.banDo.matran[i-1][j-1]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i-1,j-1)].isIn(*pos["UL"]) ##goc tren trai dung tuong tren trai hoac
				C=self.banDo.matran[i+1][j-1]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i+1,j-1)].isIn(*pos["DL"]) ##goc duoi trai dung tuong duoi trai

			if huong=="l" and (A or B or C): #tuong tu ben tren

				self.stop_move_left(i,j)
				self.setPos(i,j,2)



			A=(pos["R"][0]>=KTI*self.banDo.IPSR-self.speed)#canh phai cham canh bien ben phai hoac
			B=(j < self.banDo.IPSR-1)#chong tran va
			C=D=False

			if j>0 and i>0 and (j < self.banDo.IPSR-1) and (i < self.banDo.IPS-1):
				C=(self.banDo.matran[i-1][j+1]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i-1,j+1)].isIn(*pos["UR"]))# goc tren phai la tuong va canh tren phai dung tuong tren phai hoac
				D=(self.banDo.matran[i+1][j+1]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i+1,j+1)].isIn(*pos["DR"]))# goc duoi phai la tuong va canh duoi phai dung tuong 

			if (huong=="r") and (A or C or D): # neu dang di sang phai va
			
				self.stop_move_right(i,j)
				self.setPos(i,j,2)



				
			A=(pos["D"][0]>=KTI*self.banDo.IPSR-self.speed) #canh phai cham canh bien ben phai hoac
			B=(i < self.banDo.IPS-1) #chong tran va
			C=D=False

			if j>0 and i>0 and (j < self.banDo.IPSR-1) and (i < self.banDo.IPS-1):
				C=(self.banDo.matran[i+1][j-1]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i+1,j-1)].isIn(*pos["DL"]))   # goc tren phai la tuong va canh tren phai dung tuong tren phai hoac

				D=(self.banDo.matran[i+1][j+1]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i+1,j+1)].isIn(*pos["DR"]))		# goc duoi phai la tuong va canh duoi phai dung tuong 


				
			if (huong=="d") and (A or C or D): # neu dang di xuong va

				self.stop_move_down(i,j)
				self.setPos(i,j,1)
				
			# if huong=="u" and (pos["U"][1]<=0 or (self.banDo.matran[i-1][j]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i-1,j)].isIn(*pos["UL"]))) :
			# 	self.stop_move_up(i,j)


			# if huong=="l" and (pos["L"][0]<=0 or (self.banDo.matran[i][j-1]==1 and self.banDo.banDo[f2t1(self.banDo.IPSR,i,j-1)].isIn(*pos["UL"]))) :
			# 	self.stop_move_left(i,j)				


			# if huong=="r" and ((pos["R"][0]>=KTI*self.banDo.IPSR-self.speed) or ((j < self.banDo.IPSR-1 and self.banDo.matran[i][j+1]==1) and self.banDo.banDo[f2t1(self.banDo.IPSR,i,j+1)].isIn(*pos["DR"]))) :
			# 	self.stop_move_right(i,j)
				

				
			# if huong=="d" and ((pos["D"][1]>=KTI*self.banDo.IPS-self.speed) or ((i < self.banDo.IPS-1 and self.banDo.matran[i+1][j]==1) and self.banDo.banDo[f2t1(self.banDo.IPSR,i+1,j)].isIn(*pos["DR"]))) :
			# 	self.stop_move_down(i,j)

				

			self.x += self.dx
			self.y += self.dy

			if self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].active==False:
				self.point+=1
				self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].active=True

			self.dx=0
			self.dy=0
	


def main():
	pygame.init()


	matrix1=[
		[0,1,0,1,1,0,0],
		[0,0,0,0,0,0,1],
		[1,0,1,0,1,0,1],
		[0,0,1,2,0,0,1],
		[1,0,0,1,0,1,1],
		[0,0,0,0,0,0,1],
		[0,1,0,1,1,0,0],
	]

	RIGHT = 1073741903
	LEFT = 1073741904
	UP = 1073741906
	DOWN = 1073741905

	huong="s"

	screen = pygame.display.set_mode((KTI*len(matrix1[0]), KTI*len(matrix1)+KTI)) # 1 man hinh du lon de chua map và du thêm buffer 

	clock = pygame.time.Clock()

	map0 = BanDo(matrix1, KTI)

	pacman=Pacman(3,3, map0)

	done = False

	while not done:

		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				print("nhan",event.key)
				if event.key==RIGHT:
					huong="r"
				elif event.key==LEFT:
					huong="l"
				elif event.key==DOWN:
					huong="d"
				elif event.key==UP:
					huong="u"
				elif event.key == pygame.K_ESCAPE:
					done = True
			# if event.type == pygame.KEYUP:
			# 	print("tha")
			# 	huong="s"

		map0.draw(screen)

		pacman.draw(screen)
		pacman.update(huong)


		pygame.display.flip()
		clock.tick(20)


if __name__ == '__main__':
	main()
	pygame.quit()