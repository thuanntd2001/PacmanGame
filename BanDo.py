import pygame as pg
import copy


GREY = (150,150,150)
WHITE = (255,255,255)
BLACK=(0,0,0)
pg.init()
MAUCHU=WHITE
KTI=32 #kich thuoc cua 1 khoi, thay doi độ to nhỏ cua bản đồ
COCHU=KTI #kich thuoc dau cham


COLOR_WALL = pg.Color('lightskyblue3')
COLOR_GROUND = BLACK                         #pg.Color('dodgerblue2')
COLOR_ACTIVE=(128,128,128)

FONT = pg.font.Font(None, COCHU)


# doi tuong square cung cap các pixel tren ban do co the tuỳ chỉnh màu sac va thay doi trang thai

class Square:


    def __init__(self, x, y, KTI, style, khoangCachX=0,khoangCachY=0):
        self.rect = pg.Rect(x+khoangCachX, y+khoangCachY, KTI, KTI)
        self.KTI=KTI
        self.style=style
        if style == 0:
            self.color = COLOR_GROUND
        elif style == 1:
            self.color = COLOR_WALL
        elif style == 2:
            self.color = COLOR_ACTIVE
        self.active = False



    def draw(self, screen):

        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect)
        if self.active ==False and self.style==0:
            self.printTT(screen,".")

    def chuyenTT(self, dolui=0):
        return self.rect.left+self.KTI/2-dolui,self.rect.top+self.KTI/2-COCHU/2

    def printTT(self, screen, noiDung):
        txt_surface = FONT.render(noiDung, True, MAUCHU)
        screen.blit(txt_surface, self.chuyenTT(COCHU/10))





"""
    doi tuong ban do cung cap cac phuong thuc tao, sua, di chuyen den 1 toa do tren map và vẽ
    chỉ co ban do hinh vuong dc su dung, ko the co ban do hinh chu nhat
"""
class BanDo:

    def __init__(self, matran, KTI):
        self.matran = matran
        self.IPS = len(matran) #so hang 
        self.IPSR = len(matran[0]) #so cot
        self.KTI=KTI # kich thuoc 1 o
        self.banDo=self.sinhBD(matran)

    def chuyen(self,x,y,space=0):
        return (x+space)*self.KTI,(y+space)*self.KTI




    def sinhBD(self,matran):
        img=[]
        for i in range(self.IPS):
            for j in range(self.IPSR):
                xij,yij=self.chuyen(i,j)
                tmp=Square(yij,xij,self.KTI,matran[i][j]) #sua cho nay doi cho xij,yij
                img.append(tmp)
        return img    



    def draw(self,screen):
        for i in range(self.IPS*self.IPSR):
                self.banDo[i].draw(screen)


    def suaBD(self,matran):
        if (len(matran)!=self.IPS) or (len(matran[0]!=self.IPSR)):
            print("sai ma tran")
        else:
            for i in range(self.IPS):
                for j in range(self.IPSR):
                    self.banDo[i][j].style=matran[i][j]


def main():


# 0 la dat, 1 la tuong
    matrix1=[
        [0,1,0,1,1,0],
        [0,0,0,0,0,0],
        [1,0,1,0,1,0],
        [0,0,1,0,0,0],
        [1,0,0,1,0,0]
    ]



    screen = pg.display.set_mode((KTI*len(matrix1[0])*1.1, KTI*len(matrix1)*1.1)) # 1 man hinh du lon de chua map và du thêm buffer 

    clock = pg.time.Clock()

    map0 = BanDo(matrix1, KTI)

    done = False

    while not done:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        map0.draw(screen)


        pg.display.flip()
        clock.tick(30)



if __name__ == '__main__':
    main()
    pg.quit()
