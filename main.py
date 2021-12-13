import pygame
import testv02 as game
import testv04 as level2

screen_width=700

screen_height=483

class Menu(object):
    state=1
    def __init__(self,items):
        self.font_color=(150,150,0)#chữ để in start ,exit
        self.select_color=(200,50,50)#font chữ để in khi mà con trỏ chỉ vào
        self.items=items# start ,exit, ....
        self.font=pygame.font.SysFont(None,50)

    def update(self,screen):

        for index, item in enumerate(self.items):
            if self.state == index:
                label=self.font.render(item,True,self.select_color)
            else:
                label=self.font.render(item,True,self.font_color)
            
            posX=screen_width//4+(screen_width//5*index)
            posY = screen_height//2.8

            screen.blit(label,(posX,posY))
        
            
            
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_RIGHT:
                if self.state < len(self.items) -1:
                    self.state += 1

def main():
    pygame.init()

    screen=pygame.display.set_mode((screen_width,screen_height))

    pygame.display.set_caption("Game Pacman")
    clock=pygame.time.Clock()
    #clock=pygame.time.Clock()
    bg=pygame.image.load('background.jpg').convert()

    MENU=Menu(('Level','Start','Exit'))

    run=True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            MENU.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if MENU.state == 0:
                        # --- About ------
                            run=True

                    elif MENU.state == 1:
                        # --- Start ------
                            game.main()
                            run=True
                    elif MENU.state == 2:
                        run=False
        screen=pygame.display.set_mode((screen_width,screen_height))
        screen.blit(bg,(0,0))
        MENU.update(screen)
        
        
        
        clock.tick(20)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
