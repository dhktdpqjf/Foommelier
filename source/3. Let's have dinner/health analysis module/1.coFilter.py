import csv
from random import randint, random
import random
import matplotlib.pyplot as plt
from math import sqrt
from matplotlib import font_manager, rc  # 한글이 나오게
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

from datetime import datetime

def loadUserList(mainData, userName = '사용자'):
    f = open('user2.csv', 'r', encoding='EUC-KR')
    rdr = csv.reader(f)
    user_list={}

    for line in rdr:
        if line[0] != '재료':
            user_list[line[0]] = float(line[1])
            # user_list.append((line[0],line[1]))
    f.close()
    # return user_list

    mainData[userName] = user_list
    return mainData

def loadHealthCsv(fileName = 'health_data.csv'):
    f = open(fileName, 'r', encoding = 'EUC-KR')
    rdr = csv.reader(f)
    c = 0
    dict_list = {}

    play = '금연'
    alist = []

    for line in rdr:
        if line[0] == '음식이름':
            continue

        elif line[0] == play: ##이름이 같으면 재료를 계속 넣고 딕셔너리에 저장
            alist.append(line[1])

        else:
            dict_list[play] = alist ##이름 다르면 play가 바뀌고 재료리스트에 넣고 딕셔너리에 저장.
            alist = []
            play = line[0]
            alist.append(line[1])

    return dict_list

def loadCsv(fileName = "ref_data.csv"):
    f = open(fileName, 'r', encoding='EUC-KR')
    rdr = csv.reader(f)
    c = 0
    play = '연근조림'
    name_list = []
    mm_list = []
    sm_list = []

    for line in rdr:
        if line[0] != play:
            play = line[0]
            c += 1
            name_list.append(play)

    s = 0
    dict_list = {
        '연근조림': {
            '연근': 1,
            '간장': 1,
            '식초': 0.3,
            '양념': 0.3,
            '물엿': 0.3,
            '식용유': 0.3,
            '설탕': 0.3,
            '참기름': 0.3
        }}

    d_list = {}
    dd_list = []

    mi_list = []
    si_list = []

    ch = '연근조림'
    with open('ref_data.csv') as fr:
        reader = csv.DictReader(fr)

        for row in reader:
            #         print(row)
            if row['음식이름'] == ch:
                if row['주재료'] != '':
                    d_list.update({row['주재료']: 5.0})
                if row['부재료'] != '':
                    d_list.update({row['부재료']: 2.5})

            if row['음식이름'] != ch:
                dict_list[ch] = d_list
                s += 1
                d_list = {}
                ch = name_list[s]
                if row['주재료'] != '':
                    d_list.update({row['주재료']: 5.0})
                if row['부재료'] != '':
                    d_list.update({row['부재료']: 2.5})

            if s == 800:
                break

    return dict_list

def sim_distance(data, name1, name2):
    sum = 0
    for i in data[name1]:
        if i in data[name2]:  # 같은 영화를 봤다면
            sum += pow(data[name1][i] - data[name2][i], 2)
        else:
            sum += pow(data[name1][i], 2)

    return 1 / (1 + sqrt(sum))

def top_match(data, name, index=5, sim_function=sim_distance):
    li = []
    for i in data:
        if name != i:  # 자기 자신은 제외한다
            li.append((sim_function(data, name, i), i))  # 유사도, 이름을 튜플에 묶어 리스트에 추가한다
    li.sort()  # 오름차순 정렬
    li.reverse()  # 내림차순 정렬

    return li[:index]

def getUsersRequest(healthMaterialData,requestList): # 유저가 요구한 건강 지표 정보를 받아 가져온다.
    returnDic = {} #여기에 이제 재료이름과 가중치가 들어가야 하는것.
    tempList = []

    for rl in requestList:
        #requestList 는 지금은 ['감기','임신부'] 여기서 rl이랑 일치하는 재료를 가져와서 사용자로 저장하고 여기서 유사도 높은 거를 추천.
        mlist = healthMaterialData[rl]
        for m in mlist:
            returnDic[m] = float(5.0)

    userDic={}
    userDic['사용자'] = returnDic

    return userDic

def healthCoFilter(mainData, HealthData, requestList, howManyDish = 30):
    returnDic = {}
    topList = []

    userReque = getUsersRequest(HealthData,requestList)
    mainData['사용자'] = userReque['사용자']
    topList = top_match(mainData,"사용자",howManyDish)

    return topList



rl = ['갱년기','임신부']
print(healthCoFilter(loadCsv(),loadHealthCsv(),rl))
