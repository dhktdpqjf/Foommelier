# -*-coding: utf-8
import csv
from math import sqrt
def loadUserList():
    f = open('user2.csv', 'r', encoding='EUC-KR')
    rdr = csv.reader(f)
    user_list={}

    for line in rdr:
        if line[0] != '재료':
            user_list[line[0]] = float(line[1])
            # user_list.append((line[0],line[1]))
    f.close()
    return user_list

class Filtering:
    def sim_distance(self, data, name1, name2):  # 두 점 사이의 거리를 구하는 함수
        sum = 0
        for i in data[name1]:
            if i in data[name2]:
                sum += pow(data[name1][i] - data[name2][i], 2)
            else:
                sum += pow(data[name1][i], 2)

        return 1 / (1 + sqrt(sum))

    def top_match(self, data, name, index=5, sim_function=sim_distance):
        self.li = []
        # index = 5
        # sim_function = self.sim_distance
        for i in data:
            if name != i:  # 자기 자신은 제외한다
                self.li.append((sim_function(self,data, name, i), i))  # 유사도, 이름을 튜플에 묶어 리스트에 추가한다
        self.li.sort()  # 오름차순 정렬
        self.li.reverse()  # 내림차순 정렬

        return self.li[:index]

    def __init__(self):
        # self.func = func

        f = open('return.csv', 'r', encoding='EUC-KR')
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

        self.dict_list = {
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
        with open('return.csv') as fr:
            reader = csv.DictReader(fr)

            for row in reader:
                if row['음식이름'] == ch:
                    if row['주재료'] != '':
                        d_list.update({row['주재료']: 5.0})
                    if row['부재료'] != '':
                        d_list.update({row['부재료']: 2.5})

                if row['음식이름'] != ch:
                    self.dict_list[ch] = d_list
                    s += 1
                    d_list = {}
                    ch = name_list[s]
                    if row['주재료'] != '':
                        d_list.update({row['주재료']: 5.0})
                    if row['부재료'] != '':
                        d_list.update({row['부재료']: 2.5})

                if s == 800:
                    break

            user_list = loadUserList()
            dict_list['사용자'] = user_list
