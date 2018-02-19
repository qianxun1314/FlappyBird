from Class import *


#检查停止事件
def checkEvent():
    time.sleep(0.1)
    press = pygame.key.get_pressed()    #检测按下ESC键退出游戏
    if(press[K_ESCAPE]):
        sys.exit()
#     elif press[K_SPACE]:
#         return "buttonDownKSpace"
    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:   #检测单击X,退出游戏
            sys.exit()
            
        elif event.type == MOUSEBUTTONDOWN:     #获取鼠标单击位置
            buttonDownPos = event.pos
            return ("buttonDownPos", buttonDownPos)
        
        elif event.type == KEYDOWN and event.key == K_SPACE:     #检测是否按下SPACE键
#             if event.key == K_SPACE: 
                return "buttonDownK_SPACE"
                
        
            
#三张夜晚背景和三张白天背景交替出现，向左移动
def movingBackground(bgListNight, bgListDay):
    for i in range(3):
        bgListNight[i].display()
        bgListNight[i].moveLeft()

    for i in range(3):
        bgListDay[i].display()
        bgListDay[i].moveLeft()
        
def movingPipe(pipeList):
    for i in pipeList:
        i[0].display()
        i[0].moveLeft()
        i[1].display()
        i[1].moveLeft()
        
def birdAnimationAlive(pipeList, birdList, isButtonDownK_SPACE):   #自由下落的鸟
    deltaTime  = time.time()  
    frameIndex = (int)(deltaTime/(1.0/frameCountPerSeconds))   
    
    
    if isButtonDownK_SPACE == "buttonDownK_SPACE":
        for i in range(3):
            birdList[i].moveUp()
    else:
        for i in range(3):
            birdList[i].moveDown()
  
    if frameIndex % 3 == 0: 
        birdList[0].display()         
    if frameIndex % 3 == 1:
        birdList[1].display()     
    if frameIndex % 3 == 2: 
        birdList[2].display() 
    
    for i in pipeList:
        if birdList[0].rect.colliderect(i[0].rect) or birdList[0].rect.colliderect(i[1].rect):
            return "birdHasDeath"
    if birdList[0].rect.y >= 512:
        return "birdHasDeath"
    else:
        return "birdIsAlive"
    

def birdAnimationDeath(birdList):
    deltaTime  = time.time()  
    frameIndex = (int)(deltaTime/(1.0/frameCountPerSeconds))   
    if frameIndex % 3 == 0: 
        birdList[0].display()         
    if frameIndex % 3 == 1:
        birdList[1].display()     
    if frameIndex % 3 == 2: 
        birdList[2].display() 
    for i in range(3):
            birdList[i].deathDown()
    
        
        
        
def showScore(moveDistance):
    score = moveDistance // 220
    if score <= 0:
        score = 0
    if score >= 6:
        score = 6
        screen.blit(good, (30, 200))  
    getScoreStart =  font.render(str(score), True, (255, 0, 0))
    screen.blit(getScoreStart, (260, 0))
    
    
    
    
    
    
    