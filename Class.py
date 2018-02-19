from Headers import *


#定义基类
class BaseClass:

    def __init__(self, screen, x, y, imagePath, rectX, rectY):
        self.screen = screen
        self.x = x
        self.y = y

        self.rect = Rect(self.x, self.y, rectX, rectY)
        self.image = pygame.image.load(imagePath).convert_alpha()

    def display(self):      #渲染到屏幕上
        self.screen.blit(self.image, self.rect)


#定义背景类，继承基类
class Background(BaseClass):

    def __init__(self, screen, x, y, imagePath):
        super().__init__(screen, x, y, imagePath, 288, 512)

    def moveLeft(self):     #向左移动
        if self.rect.x < -288:
            self.rect.x = 1440
        self.rect = self.rect.move([-5, 0])


#定义水管类，继承基类
class Pipe(BaseClass):
    def __init__(self, screen, x, y, imagePath):
        super().__init__(screen, x, y, imagePath, 52, 320)
    
    def moveLeft(self):
        self.rect = self.rect.move([-5, 0])        
   
   
   
#定义小鸟类，继承基类
class Bird(BaseClass):
    def __init__(self, screen, x, y, imagePath):
        super().__init__(screen, x, y, imagePath, 48, 48)
        
    def moveDown(self):
            self.rect = self.rect.move([0, 10]) 
            
    def deathDown(self):
        if self.rect.y <= 400:
            self.rect = self.rect.move([0, 50])  
        
    def moveUp(self):
        self.rect = self.rect.move([0, -20])     
        