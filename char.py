import pygame
from pygame.constants import SCRAP_SELECTION
from BanDo import *
import time
from ani import *
import time

def getNow():
    return round(time.time() * 1000)


def getPosB(KTI,x,y):# toa do tren duoi trai phai  
	return {"U":(x+KTI//2,y),"D":(x+KTI//2,y+KTI),"L":(x,y+KTI//2),"R":(x+KTI,y+KTI//2),"C":(x+KTI//2,y+KTI//2),"UL":(x,y),"UR":(x+KTI,y),"DL":(x,y+KTI),"DR":(x+KTI,y+KTI)}

def getCen(KTI,x,y):
	return (x+KTI//2,y+KTI//2)

def getCoo(KTIanh,x,y): #tra ve toa do cua anh tren ban do
	center= getCen(KTIanh,x,y)
	print(center)
	return int(center[1]/KTI),int(center[0]/KTI)


		
				
	
class NhanVat():
	def __init__(self, i, j, bando):

		self.banDo=bando
		self.x=j*self.banDo.KTI #doi tu toa do tuong doi sang toa do 
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
	def __init__(self,i, j, bando, speed=5):
		NhanVat.__init__(self,i,j,bando)
		self.player_image=pygame.image.load("Player.png")
		self.image = self.player_image.convert()
		self.image.set_colorkey(BLACK)
		self.rect= self.image.get_rect()																	   #pygame.Rect((self.x+self.image.get_width()//4,self.y+self.image.get_height()//4),(self.image.get_width()*1.5,self.image.get_height()*1.5))
		self.KTI=self.rect.width
		self.speed=speed
		self.dx=0
		self.dy=0
		self.huong="s"
		self.point=0
		self.pacman_sound = pygame.mixer.Sound("pacman_sound.ogg")
		self.game_over_sound = pygame.mixer.Sound("game_over_sound.ogg")

		self.bg_end_game=pygame.transform.scale(pygame.image.load("bg2.png"),(700,438))
		#self.bg_end_game=pygame.image.load("bg3.png")

		

		self.font=pygame.font.SysFont('vninhatban',70)
		#self.font=pygame.font.SysFont('vnibendigo',80)

		img=pygame.image.load('1.png').convert_alpha()
		img1=pygame.image.load('2.png').convert_alpha()
		img2=pygame.image.load('3.png').convert_alpha()
		img3=pygame.transform.scale(pygame.image.load('4.png'),(32,32))
		self.moveRight=Animation(img,img1,img2)
		self.moveLeft=Animation(pygame.transform.flip(img,True,False),pygame.transform.flip(img1,True,False),pygame.transform.flip(img2,True,False))
		self.moveUp=self.move_up_animation = Animation(pygame.transform.rotate(img,90),pygame.transform.rotate(img1,90),pygame.transform.rotate(img2,90))
		self.moveDown=self.move_down_animation = Animation(pygame.transform.rotate(img,270),pygame.transform.rotate(img1,270),pygame.transform.rotate(img2,270))
		self.explosion_animation = Animation(img,img1,img3)
		self.mode=0
		self.bd=0
		self.cc=0
		
	def moveR(self):
		self.dx=self.speed
		self.moveRight.update(10)
		self.image=self.moveRight.currentImage()
	def moveL(self):
		self.dx=-self.speed
		self.moveLeft.update(10)
		self.image=self.moveLeft.currentImage()
	def moveU(self):
		self.dy=-self.speed
		self.moveUp.update(10)
		self.image=self.moveUp.currentImage()
	def moveD(self):
		self.dy=self.speed
		self.moveDown.update(10)
		self.image=self.moveDown.currentImage()


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
	

	def update(self,huong,screen):
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


				

			self.x += self.dx
			self.y += self.dy

			

			if self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].active==False and self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].style in (0,3):
				self.pacman_sound.play()
				self.point+=1
				self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].active=True
				self.cc+=1

			elif self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].active==False and self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].style==9:
				self.pacman_sound.play()
				self.point+=1
				self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].active=True
				self.bd=getNow()
				self.cc+=1
				
    		
			self.redTime()
			self.dx=0
			self.dy=0
		else:
			self.biRape(screen,self.bg_end_game)
	
	def redTime(self):
		time=getNow()
		print(time-self.bd)
		if (time-self.bd)<10000:
			self.image=pygame.image.load("slime.png")#sửa 
			self.mode=1
		else:
			self.mode=0
	
	
    	
    	
	def rape(self,slime):
		for x,y in getPosB(slime.KTI,slime.x,slime.y).values():
			if self.x<x<self.x+self.KTI and self.y<y<self.y+self.KTI:
				self.point+=1
				return True

		return False
			
	def biRape(self,screen,bg_end_game):
		self.game_over=True
		
		self.game_over_sound.play()
		label=self.font.render("Score "+ str(self.point),True,(255,215,0))
		print("bi hiep dam")
		screen.fill(BLACK)
		
		pygame.display.flip()
		for i in range(len(self.explosion_animation.image_list)):
			print(i)
			screen.fill(BLACK)
			pygame.display.flip()
			self.image=self.explosion_animation.image_list[i]
			self.draw(screen)
			
			pygame.display.flip()
			pygame.time.wait(500)

		screen.fill(BLACK)
		screen.blit(bg_end_game,(150,100))
		screen.blit(label,(300,420))
		
		pygame.display.flip()
		pygame.time.wait(5000)

		
		


def main():
	pygame.init()


	matrix1=[
		[9,1,0,1,1,0,0,0,0,0,1,1,9,0],
		[0,0,0,0,0,0,1,1,1,0,0,0,1,0],
		[1,0,1,0,1,0,1,0,0,0,1,0,0,0],
		[0,0,1,0,0,0,1,0,1,0,1,1,0,1],
		[1,0,0,1,0,1,1,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,1,0,1,0,1,1,0,0],
		[0,1,0,1,1,0,0,1,0,1,0,0,0,1],
		[0,0,0,0,0,0,1,1,0,0,0,0,1,1],
		[1,0,1,0,1,0,1,0,1,0,1,0,0,1],
		[0,0,1,0,0,0,1,0,0,0,0,1,1,0],
		[1,0,0,1,0,1,1,0,0,1,0,0,0,0],
		[0,0,0,0,0,0,1,0,0,0,1,0,1,0],
		[9,1,0,1,1,0,0,1,0,0,0,1,9,0],
	]

	RIGHT = 1073741903
	LEFT = 1073741904
	UP = 1073741906
	DOWN = 1073741905

	huong="s"

	screen = pygame.display.set_mode((KTI*len(matrix1[0]), KTI*len(matrix1))) # 1 man hinh du lon de chua map và du thêm buffer 

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
		if pacman.game_over==True: done=True

		pygame.display.flip()
		clock.tick(20)


if __name__ == '__main__':
	main()
	pygame.quit()