import csv
from random import randint, random
import random
import matplotlib.pyplot as plt
import coFilter as co
from math import sqrt
from datetime import datetime
from matplotlib import font_manager, rc  # 한글이 나오게
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def findWord(data, word): ## 전체 리스트 음식이름 칼럼에서 word를 포함하는 레코드를 찾으면 됨
    returnList = {}
    for d in data:
        if word in d:
            # print(d)
            returnList[d] = data[d]
    return returnList #딕셔너리로 {음식이름:재료} 다 갖고 오는 거

def findWordNot(data,word): ##word를 포함하는 모든 레코드를 삭제한 {음식:재료}
    returnList = {}
    for d in data:
        if word not in d:
            # print(d)
            returnList[d] = data[d]
    return returnList

def giveMeRand(data):
    list = []
    returnDic = {}
    for d in data:
        list.append(d)

    it = random.choice(list) ##math.random()이랑 같은 거
    returnDic[it] = data[it]
    return returnDic

def getMenu(data): ## 전체 {음식이름:재료} coFilter랑 같이 돌리면
    alist = {}
    if(randint(1,10)<9):
        thisDict = giveMeRand(findWord(data,'밥')) ##밥만 가져온 거
        for td in thisDict:
            alist[td] = thisDict[td]
        thisDict = giveMeRand(findWordNot(findWord(data, '국'),'국수')) ##국수만 가져온 거를 뺀 거
        for td in thisDict:
            alist[td] = thisDict[td]
        # print(alist)
        thisDict = findSubMenu(data,2) ##반찬만 가져온 거
        for td in thisDict:
            alist[td] = thisDict[td]

    else :
        llist = findWord(data,"국수")

        if llist == []:
            llist = findWord(data,'밥')

        thisDict = giveMeRand(llist) ##국수 식단
        for td in thisDict:
            alist[td] = thisDict[td]

        thisDict = findSubMenu(data, 1)
        for td in thisDict:
            alist[td] = thisDict[td]

    return alist ##식단 리스트

def findSubMenu(data, howMany = 1):
    alist = {}
    for i in range(howMany):
        thisDict = giveMeRand(findWordNot(findWordNot(data, '밥'), '국'))
        for td in thisDict:
            alist[td] = thisDict[td]
    # print(alist)

    return alist

##주 단위 식단 받는거 아직 안 함

class menufiltering:
    def getData(self,rlist):
        alist = co.healthCoFilter(co.loadCsv(), co.loadHealthCsv(), rlist, 100) #rlist = ['감기', '금연']
        c = 0
        names = []
        for a in alist:
            c += 1
            names.append(a[1])
        total = co.loadCsv()
        dic1 = {}

        for n in names:
            dic1[n] = total[n]

        menuList = getMenu(dic1)
        return menuList
