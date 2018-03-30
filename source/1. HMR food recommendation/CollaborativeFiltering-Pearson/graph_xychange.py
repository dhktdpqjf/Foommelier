from matplotlib import pyplot as plt
from matplotlib import font_manager, rc #한글 출력을 위해 matplotlib의 font_manager를 import한다.
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
import numpy as np

def drawGraph2():
    plt.figure(figsize=(12, 6))  # plot 크기설정

    # plot 좌표를 위한 list 선언
    li = []
    li2 = []
    li.append(4)
    li2.append(9)
    plt.text(4, 9, "구동섭")

    li.append(6)
    li2.append(8)
    plt.text(6,8,"정산")

    li.append(8)
    li2.append(2)
    plt.text(8, 2, "이승미")
    # for i in data[names1]:  # i = 키 값
    #     if i in data[name2]:  # 같은 음식을 평가했을때만
    #         li.append(data[name1][i])  # name1의 평점 li[]에 추가
    #         li2.append(data[name2][i])  # name2의 평점 li2[]에 추가
    #         plt.text(data[name1][i], data[name2][i], i)  # 제품명 text 찍기

    plt.plot(li, li2, 'ro')  # plot그리기

    # 각 축의 크기 설정 (0에서 10까지)
    plt.axis([0, 10, 0, 10])
    # 눈금 갯수 설정
    numOfDgr = 11
    plt.xticks(np.linspace(0, 10, numOfDgr, endpoint=True))
    plt.yticks(np.linspace(0, 10, numOfDgr, endpoint=True))
    # x축과 y축 이름 설정
    plt.xlabel("육교자")
    plt.ylabel("돼지바핫도그")

    # 그리기
    plt.show()

drawGraph2()
