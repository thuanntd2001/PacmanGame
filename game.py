
from pygame.font import Font
from Slime import Slime
from Char import Pacman
from BanDo import *
import pygame

def rapePM(pacman,slimeTup):
	for slime in slimeTup:
		if slime.rape(pacman):
			pacman.explosion=True
			
def rapeSlime(slime,pacman):
		if pacman.rape(slime):
			slime.explosion=True  

def main():
	pygame.init()


	matrix1=[
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,9,1,0,0,3,0,0,0,1,0,0,0,3,0,0,1,9,0,1],
		[1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1],
		[1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1],
		[1,1,0,1,0,1,1,0,1,3,0,3,1,0,1,1,0,1,0,1,1],
		[0,1,3,0,3,0,1,0,0,0,1,0,0,3,1,0,3,0,0,1,0],
		[0,0,0,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,0,0,0],
		[1,1,1,1,0,0,0,3,0,0,3,0,0,3,0,0,0,1,1,1,1],
		[1,0,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,0,1],
		[1,1,0,0,3,1,3,0,1,9,3,9,1,0,3,1,0,0,3,1,1],
		[0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0],
		[3,0,3,1,0,0,0,3,0,0,0,0,0,3,0,0,0,1,3,0,3],
		[0,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0],
		[0,0,3,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,3,0,0],
		[1,1,1,1,9,1,1,1,1,0,1,0,1,1,1,1,9,1,1,1,1],
		

        
	]    

	RIGHT = 1073741903
	LEFT = 1073741904
	UP = 1073741906
	DOWN = 1073741905

	huong="s"

	screen = pygame.display.set_mode((KTI*len(matrix1[0]), KTI*len(matrix1))) # 1 man hinh du lon de chua map và du thêm buffer 

	clock = pygame.time.Clock()

	
	font=pygame.font.SysFont('vnibendigo',80)
	soundstart=pygame.mixer.Sound("sound/Pacman.ogg")
	soundstart.play()

	bg_end_game=pygame.transform.scale(pygame.image.load("background/bg4.png"),(700,438))

	map0 = BanDo(matrix1, KTI)
	
	slime0=Slime('character/inky.png',1,2,map0)
	slime1=Slime('character/inky.png',14,4,map0)
	slime2=Slime('character/Pinky.png',14,16,map0)
	slime3=Slime('character/Pinky.png',1,18,map0)
	slime4=Slime('character/Clyde.png',9,6,map0)
	slime5=Slime('character/Clyde.png',9,14,map0)
	slime6=Slime('character/Clyde.png',4,10,map0)
	#slime7=Slime(4,11,map0)
	

	tupSlime=(slime0,slime1,slime2,slime3,slime4,slime5,slime6)
	
	pacman=Pacman(9,10, map0,15)

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
		
		map0.draw(screen)
		label=font.render("Score: "+ str(pacman.point),True,(0,0,0))
		

		
		for slime in tupSlime:
			slime.draw(screen)
			slime.update()
		
		

		pacman.draw(screen)
		pacman.update(huong,screen)


		
		rapePM(pacman,tupSlime)
		for slime in tupSlime:
			rapeSlime(slime,pacman)
		
		if pacman.game_over==True: done=True
		if pacman.end==map0.end:
			screen=pygame.display.set_mode((1000,638))
			screen.fill(WHITE)
			screen.blit(bg_end_game,(150,100))
			screen.blit(label,(350,460))
			pygame.display.flip()
			pygame.time.wait(5000)
			done=True
		
    			

		pygame.display.flip()
		clock.tick(20)

    
if __name__ == '__main__':
	main()
	pygame.quit()