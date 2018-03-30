import csv
from random import randint, random
import random
import matplotlib.pyplot as plt
from math import sqrt
from matplotlib import font_manager, rc  # 한글이 나오게
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

from datetime import datetime

def loadUserData(mainData, username = '동섭'):

    user_list = {}
    with open('user_ref_data.csv') as fr:
        reader = csv.DictReader(fr)

        for row in reader:
            #         print(row)
            if row['사용자'] == username:
                if row['주재료'] != '':
                    user_list.update({row['주재료']: 5.0})
                if row['부재료'] != '':
                    user_list.update({row['부재료']: 2.5})

    # 사용자 냉장고 데이터
    d_list = {}
    d_list.update(user_list)
    mainData['사용자'] = d_list
    return mainData

def loadCsv():
    #########몇 줄 있는지 보게
    f = open('ref_data.csv', 'r', encoding='EUC-KR')
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
    # print(c) ##첫번쨰거는 음식이름이 들어갓으니 뺴기
    # name_list.pop(0)
    # print(len(name_list))
    # print(name_list[1])

    # In[24]:

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
    # ???????????????????????????
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


# In[26]:


def top_match(data, name, index=5, sim_function=sim_distance):
    li = []
    for i in data:
        if name != i:  # 자기 자신은 제외한다
            li.append((sim_function(data, name, i), i))  # 유사도, 이름을 튜플에 묶어 리스트에 추가한다
    li.sort()  # 오름차순 정렬
    li.reverse()  # 내림차순 정렬

    return li[:index]

def findWord(data, word):
    returnList = {}
    for d in data:
        if word in d:
            # print(d)
            returnList[d] = data[d]
    return returnList

def findWordNot(data,word):
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
    it = random.choice(list)
    returnDic[it] = data[it]
    return returnDic

def getMenu(data):
    alist = {}
    if(randint(1,10)<11):
        thisDict = giveMeRand(findWord(data,'밥'))
        for td in thisDict:
            alist[td] = thisDict[td]
        thisDict = giveMeRand(findWordNot(findWord(data, '국'),'국수'))
        for td in thisDict:
            alist[td] = thisDict[td]
        # print(alist)
        thisDict = findSubMenu(data,2)
        for td in thisDict:
            alist[td] = thisDict[td]

    else :
        thisDict = giveMeRand(findWord(data,"국수"))
        for td in thisDict:
            alist[td] = thisDict[td]

        thisDict = findSubMenu(data, 1)
        for td in thisDict:
            alist[td] = thisDict[td]

    return alist
def findSubMenu(data, howMany = 1):
    alist = {}
    for i in range(howMany):
        thisDict = giveMeRand(findWordNot(findWordNot(data, '밥'), '국'))
        for td in thisDict:
            alist[td] = thisDict[td]
    print(alist)

    return alist

def get1weekMenu(data,startDate = (datetime.today().strftime('%Y%m%d'))):
    print(startDate)

    return

alist = loadCsv()
print(alist)
# print(alist)
# findWordNot(alist,'밥')
# for a in alist:
#     print(alist.index(a))
# alist = [1,2,3]
# random.choice(alist)
# print(alist)

menuList = getMenu(alist)
print(menuList)
# print(get1weekMenu(alist))