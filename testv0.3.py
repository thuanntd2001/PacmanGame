from slime import Slime
from Char import Pacman
from BanDo import *
import pygame

def rapePM(pacman,slimeTup):
	for slime in slimeTup:
		if slime.rape(pacman):
			pacman.explosion=True


def main():
	pygame.init()


	matrix1=[
		[9,1,3,1,1,0,0,0,0,0,1,1,9,3],
		[0,0,0,0,0,0,1,0,1,0,0,0,1,0],
		[1,0,1,0,1,0,1,0,0,0,1,0,0,0],
		[0,0,1,0,0,0,1,0,1,0,1,1,0,1],
		[1,0,0,1,0,1,1,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,1,0,1,0,1,1,0,0],
		[0,1,0,1,1,0,3,1,0,1,0,0,0,1],
		[0,0,0,0,0,0,1,1,0,0,0,0,1,1],
		[1,0,1,0,1,0,1,0,1,0,1,0,0,1],
		[3,0,1,0,0,0,1,0,0,0,0,1,1,0],
		[1,0,0,1,0,1,1,0,0,1,0,0,0,0],
		[0,0,0,0,0,0,1,0,0,0,1,0,1,0],
		[9,1,0,1,1,0,0,1,0,0,3,1,9,3],
	]

	RIGHT = 1073741903
	LEFT = 1073741904
	UP = 1073741906
	DOWN = 1073741905

	W=119
	A=97
	D=100
	S=115

	huong="s"
	huong2="s"

	screen = pygame.display.set_mode((KTI*len(matrix1[0]), KTI*len(matrix1))) # 1 man hinh du lon de chua map và du thêm buffer 

	clock = pygame.time.Clock()

	map0 = BanDo(matrix1, KTI)

	slime0=Slime(1,1,map0)
	slime1=Slime(7,7,map0)
	slime2=Slime(11,1,map0)
	slime3=Slime(1,11,map0)
	slime4=Slime(11,11,map0)

	tupSlime=(slime0,slime1,slime2,slime3,slime4)

	pacman=Pacman(3,3, map0)
	pacman2=Pacman(10,10,map0)

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

				if event.key==D:
					huong2="r"
				elif event.key==A:
					huong2="l"
				elif event.key==S:
					huong2="d"
				elif event.key==W:
					huong2="u"
					

				elif event.key == pygame.K_ESCAPE:
					done = True
		
		map0.draw(screen)


		for slime in tupSlime:
			slime.draw(screen)
			slime.update()

		

		pacman.draw(screen)
		pacman.update(huong)

		pacman2.draw(screen)
		pacman2.update(huong2)

		

		rapePM(pacman,tupSlime)
		rapePM(pacman2,tupSlime)

		pygame.display.flip()
		clock.tick(20)


if __name__ == '__main__':
	main()
	pygame.quit()