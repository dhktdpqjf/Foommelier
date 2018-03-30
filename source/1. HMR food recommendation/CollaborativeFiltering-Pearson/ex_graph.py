##csv 불러오기

import pandas as pd
import csv

from pandas import DataFrame as df

def saveAsCsv(dicList,fileName='dft'):
    df2 = df(dicList)
    df2.to_csv(fileName+'.csv',index= False , encoding='EUC-KR')

def loadAsCsv1(fileName='dft.csv'):
    print('hi')
    tempDf = pd.read_csv(fileName)
    alist = []

    for i in tempDf.index:
        tempDic = {}
        for col in tempDf:
            tempDic[col] = tempDf.at[i,col]
        alist.append(tempDic)
    return alist

    return list
def loadAsCsv(fileName='dft.csv'):

    tempDf = pd.read_csv(fileName, encoding='EUC-KR')
    alist = []

    for i in tempDf.index:
        tempDic = {}
        for col in tempDf:
            tempDic[col] = tempDf.at[i,col]
        alist.append(tempDic)
    return alist

def transList(givenList):
    returnDic = {}
    tempList = []
    for gl in givenList:
        tempList.append(gl['이름'])
    tempList = list(set(tempList))
    tempDic = {}
    for tl in tempList:
        for gl in givenList:
            if(tl==gl['이름']):
                tempDic[gl['음식명']] = gl['평점']
        returnDic[tl] = tempDic
        tempDic = {}

    return returnDic

#그래프
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc #한글 출력을 위해 matplotlib의 font_manager를 import한다.
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
import numpy as np

# critics data 이용해 scatter plot 그리기
def drawGraph(data, name1, name2):
    plt.figure(figsize=(12, 6))  # plot 크기설정

    # plot 좌표를 위한 list 선언
    li = []
    li2 = []

    for i in data[name1]:  # i = 키 값
        if i in data[name2]:  # 같은 음식을 평가했을때만
            li.append(data[name1][i])  # name1의 평점 li[]에 추가
            li2.append(data[name2][i])  # name2의 평점 li2[]에 추가
            plt.text(data[name1][i], data[name2][i], i)  # 제품명 text 찍기

    plt.plot(li, li2, 'ro')  # plot그리기

    # 각 축의 크기 설정 (0에서 10까지)
    plt.axis([0, 10, 0, 10])
    # 눈금 갯수 설정
    numOfDgr = 11
    plt.xticks(np.linspace(0, 10, numOfDgr, endpoint=True))
    plt.yticks(np.linspace(0, 10, numOfDgr, endpoint=True))
    # x축과 y축 이름 설정
    plt.xlabel(name1)
    plt.ylabel(name2)

    # 그리기
    plt.show()




# 실행 부분!----------------------------------------------------------------------------------
loadLIst = []  # 파일을 로드할 리스트를 선언 했어요.

loadLIst = loadAsCsv('temp_file3.csv')  # 파일로드해서 담아요.
print(loadLIst)  # 어떻게 가져오나 확인 하고
dataList = transList(loadLIst)  # 로드한 데이터를 추천 시스템을 위한 데이터 셋 형태로 변환하는 메소드에요
print(list)  # 잘 변환됐나 확인해보고
print(drawGraph(dataList, '이승미', '김지현'))