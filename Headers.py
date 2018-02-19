import pygame
import time
import sys
import random
from pygame.locals import *

pygame.init()

font = pygame.font.SysFont("arial", 40)
goodFont = pygame.font.SysFont("arial", 80)
textScore = font.render("Score: ", True, (255, 0, 0))
getScore =  font.render("0", True, (0, 255, 0))
good =  goodFont.render("Good!", True, (255, 0, 0))
frameCountPerSeconds = 10       #设置帧率
moveDistance = 0

imageDict = {1: "./images/bird1_0.png", 2: "./images/bird1_1.png", 3: "./images/bird1_2.png", 4: "./images/bird2_0.png", 5: "./images/bird2_1.png", 6: "./images/bird2_2.png", 7: "./images/bg_night.png", 8: "./images/bg_day.png", 9: "./images/pipe2_down.png", 10: "./images/pipe2_up.png", 11: "./images/button_play.png", 12: "./images/text_ready.png", 13: "./images/text_game_over.png"}

screen = pygame.display.set_mode((288, 512))    #加载图片到缓冲区，还没有展示在屏幕上，返回Surface对象
pygame.display.set_caption("Author:筵")      #设置标题


bgListNight = []      #三张夜晚背景容器
bgListDay = []        #三张白天背景容器
pipeList = []
birdListAlive = []
birdListDeath = []


    




