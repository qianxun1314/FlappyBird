from Methods import *

def initObject(screen, imageDict, bgListNight, bgListDay, pipeList, birdListAlive, birdListDeath):
    for i in range(3):  #实例化三张夜晚背景
        bgListNight.append(Background(screen, 288*i, 0, imageDict[7]))
    for i in range(3):  #实例化三张白天背景
        bgListDay.append(Background(screen, 288*i + 864, 0, imageDict[8]))   
    for i in range(6):  #实例化水管
        rand = random.randrange(-200, -50)
        pipeList.append([Pipe(screen, 304+220*i, rand, imageDict[9]), Pipe(screen, 304+220*i, 500+rand, imageDict[10])]) 
    for i in range(3):      #初始化活鸟
        birdListAlive.append(Bird(screen, 36, 200, imageDict[i+1])) 
    for i in range(3):      #初始化死鸟
        birdListDeath.append(Bird(screen, 36, 200, imageDict[i+4])) 