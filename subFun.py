from time import time
from BanDo import *
import time

def getNow():
    return round(time.time() * 1000)#hàm dùng để tính thời gian thực của máy 


def getPosB(KTI,x,y):# toa do tren duoi trai phai  
	return {"U":(x+KTI//2,y),"D":(x+KTI//2,y+KTI),"L":(x,y+KTI//2),"R":(x+KTI,y+KTI//2),"C":(x+KTI//2,y+KTI//2),"UL":(x,y),"UR":(x+KTI,y),"DL":(x,y+KTI),"DR":(x+KTI,y+KTI)}

def getCen(KTI,x,y):#toa độ chính giữa của ảnh
	return (x+KTI//2,y+KTI//2)

def getCoo(KTIanh,x,y): #tra ve toa do cua anh tren ban do
	center= getCen(KTIanh,x,y)
	print(center)
	return int(center[1]/KTI),int(center[0]/KTI)

