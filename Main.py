from InitObject import *

def startGame():
    moveDistance = -20
    isButtonPlay = False    #是否按下开始按钮
    isAlive = "birdIsAlive"      #鸟是否死亡
    initObject(screen, imageDict, bgListNight, bgListDay, pipeList, birdListAlive, birdListDeath)     #初始化对象
    buttonPlay = BaseClass(screen, 90, 300, imageDict[11], 116, 70)     #实例一个开始按钮
    gameOver = BaseClass(screen, 50, 240, imageDict[13], 204, 54)
    
    while True:      
        ret = checkEvent()     #停止事件检测
        movingBackground(bgListNight, bgListDay)        #交替移动的背景
        movingPipe(pipeList)    #移动的管道
        screen.blit(textScore, (140, 0))
        if not isButtonPlay:    #判断开始按钮是否按下
            buttonPlay.display()
            if ret and ret[0] == "buttonDownPos" and buttonPlay.rect.collidepoint(ret[1]):
                    isButtonPlay = True
            screen.blit(getScore, (260, 0))
        else:       #已经按下开始按钮
            moveDistance += 5
            showScore(moveDistance)
            
            if isAlive == "birdIsAlive":    #鸟是活着的状态
                isButtonDownK_SPACE = ret   #判断是否应该向上跳跃，如果不跳跃，则自由落体
                isAlive = birdAnimationAlive(pipeList, birdListAlive, isButtonDownK_SPACE)
                
            if isAlive == "birdHasDeath":   #鸟是死了的状态
                birdAnimationDeath(birdListDeath)   #鸟的死亡动画 
                gameOver.display()  #显示makeover按钮
                #单击gameover按钮，退出游戏
                if ret and ret[0] == "buttonDownPos" and gameOver.rect.collidepoint(ret[1]):
                    sys.exit()
               
        
        pygame.display.update()
        
if __name__ == "__main__":
    startGame()
  
    