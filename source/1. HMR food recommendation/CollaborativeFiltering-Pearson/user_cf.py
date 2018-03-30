

from numpy import sqrt

critics = {
    '이승미': {
        '육교자': 6.0,
        '볼로네이즈 스파게티': 8.0,
        '피자게티': 5.0,
        '쌀떡볶이': 9.0,
        '상하목장 유기농우유': 2.5,
        '우유치즈롤': 3.0,
    },
    '김지현': {
        '우유치즈롤': 1.0,
        '쌀떡볶이': 8.5,
        '피자게티': 4.5,
        '우유치즈롤': 7.0,
        '맛있는 김치찌개': 9.5,
        '육교자': 6.5,
    },
    '나태호': {
        '전복죽': 3.0,
        '생가쓰오우동': 3.5,
        '고르곤졸라 씬피자': 1.5,
        '사골우거지국': 5.0,
        '고기참만두': 3.0,
        '새우부추만두': 3.5,
    },
    '구동섭': {
        '육교자': 7.0,
        '볼로네이즈 스파게티': 6.0,
        '피자게티': 6.0,
        '쌀떡볶이': 3.0,
        '상하목장 유기농우유': 4.5,
        '우유치즈롤': 2.0,
    },
    '정산': {
        '쌀떡볶이': 9.5,
        '상하목장 유기농우유': 3.0,
        '고구마 스프': 4.5,
        '피자게티': 4.0,
        '볼로네이즈 스파게티': 8.5,
    },
    '김대규': {
        '고구마 스프': 3.0,
        '치즈어묵고로케': 4.0,
        '아보카도베이글': 2.0,
        '상하목장 유기농 요구르트': 3.0,
        '미니돈까스': 3.5,
        '유산슬': 2.0,
    },
    '최재용': {
        '유산슬': 3.0,
        '상하목장 유기농 요구르트': 4.0,
        '해산물 빠에야': 3.0,
        '리얼치즈김밥': 5.0,
        '발렌시아 오렌지': 3.5,}
    }
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

hi = ''


def loadAsCsv(fileName='dft.csv'):
    tempDf = pd.read_csv(fileName, encoding='EUC-KR')
    alist = []

    for i in tempDf.index:
        tempDic = {}
        for col in tempDf:
            tempDic[col] = tempDf.at[i, col]
        alist.append(tempDic)
    return alist


jio =''


def transList(givenList):
    returnDic = {}
    tempList = []
    for gl in givenList:
        tempList.append(gl['이름'])
    tempList = list(set(tempList))
    tempDic = {}
    for tl in tempList:
        for gl in givenList:
            if (tl == gl['이름']):
                tempDic[gl['음식명']] = gl['평점']
        returnDic[tl] = tempDic
        tempDic = {}


    return returnDic

# 피어슨 상관계수 구하기
def sim_pearson(data, name1, name2):
    sumX = 0  # X의 합
    sumY = 0  # Y의 합
    sumPowX = 0  # X 제곱의 합
    sumPowY = 0  # Y 제곱의 합
    sumXY = 0  # X*Y의 합
    count = 0  # 음식 개수

    for i in data[name1]:  # i = key
        if i in data[name2]:  # 같은 음식을 평가했을때만
            sumX += data[name1][i]
            sumY += data[name2][i]
            sumPowX += pow(data[name1][i], 2)
            sumPowY += pow(data[name2][i], 2)
            sumXY += data[name1][i] * data[name2][i]
            count += 1

    return (sumXY - ((sumX * sumY) / count)) / sqrt(
        (sumPowX - (pow(sumX, 2) / count)) * (sumPowY - (pow(sumY, 2) / count)))

# 딕셔너리 돌면서 상관계수순으로 정렬
def top_match(data, name, index=2, sim_function=sim_pearson):
    li=[]
    for i in data: #딕셔너리를 돌고
        if name!=i: #자기 자신이 아닐때만
            li.append((sim_function(data,name,i),i)) #sim_function()을 통해 상관계수를 구하고 li[]에 추가
    li.reverse() #내림차순
    return li[:index]

#음식 추천 알고리즘
def getRecommendation(data, person, sim_function=sim_pearson):
    result = top_match(data, person, len(data))

    simSum = 0  # 유사도 합을 위한 변수

    score = 0  # 평점 합을 위한 변수

    li = []  # 리턴을 위한 리스트

    score_dic = {}  # 유사도 총합을 위한 dic

    sim_dic = {}  # 평점 총합을 위한 dic

    for sim, name in result:  # 튜플이므로 한번에

        if sim < 0: continue  # 유사도가 양수인 사람만

        for music in data[name]:

            if music not in data[person]:  # name이 평가를 내리지 않은 음식

                score += sim * data[name][music]  # 그사람의 음식평점 * 유사도

                score_dic.setdefault(music, 0)  # 기본값 설정

                score_dic[music] += score  # 합계 구함

                # 조건에 맞는 사람의 유사도의 누적합을 구한다

                sim_dic.setdefault(music, 0)

                sim_dic[music] += sim

            score = 0  # 음식이 바뀌었으니 초기화한다

    for key in score_dic:
        score_dic[key] = score_dic[key] / sim_dic[key]  # 평점 총합/ 유사도 총합

        li.append((score_dic[key], key))  # list((tuple))의 리턴을 위해서.

    li.reverse()  # 내림차순

    return li

#실행 부분!----------------------------------------------------------------------------------
loadLIst = [] # 파일을 로드할 리스트를 선언 했어요.

loadLIst = loadAsCsv('temp_file3.csv') # 파일로드해서 담아요.
dataList = transList(loadLIst) # 로드한 데이터를 추천 시스템을 위한 데이터 셋 형태로 변환하는 메소드에요
print(dataList) # 잘 변환됐나 확인해보고

print(getRecommendation(dataList, "이승미")) #추천 시스템에 사용해 보면!

