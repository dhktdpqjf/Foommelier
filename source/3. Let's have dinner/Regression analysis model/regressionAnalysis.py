# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import csv
from pandas import DataFrame as df
np.seterr(divide='ignore', invalid='ignore')

def saveAsCsv(dicList, fileName='dft'):
    df2 = df(dicList)
    df2.to_csv(fileName + '.csv', index=False, encoding='EUC-KR')


def loadAsCsv1(fileName='dft.csv'):
    list = []
    f = open(fileName, 'r', encoding='EUC-KR')
    rdr = csv.reader(f)
    for line in rdr:
        list.append(line)
        print(type(line))
    f.close()

    return list


def loasAsCsv(fileName='dft.csv'):
    tempDf = pd.read_csv(fileName, encoding='EUC-KR')
    alist = []

    for i in tempDf.index:
        tempDic = {}
        for col in tempDf:
            tempDic[col] = tempDf.at[i, col]
        alist.append(tempDic)
    return alist


# csv 파일을 가져옴(1단계)
df = pd.read_csv('gogotest.csv', encoding='EUC-KR')

'''
# 데이터의 컬럼명을 변경
df.columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'dis', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
'''

# 데이터프레임으로 저장
tempList = loasAsCsv('gogotest.csv')


cols = ['satis', 'serving_size', 'kcal', 'carbo', 'sugar', 'protein', 'fat', 'saturated_fat', 'trans_fat', 'cholesterol', 'salt', 'calcium']

# 각 항목들의  상관관계를 그래프로 보여줌
sns.set(style='whitegrid', context='notebook')
#cols = ['satis', 'serving_size', 'kcal', 'carbo', 'sugar', 'protein', 'fat', 'saturated_fat', 'trans_fat', 'cholesterol', 'salt', 'calcium']
sns.pairplot(df[cols], size=2.5)
plt.show()
sns.reset_orig()

'''
#각 항목들의 상관관계를 히트맵으로 보여줌
cm = np.corrcoef(df[cols].values.T)
sns.set(font_scale=1.5)
hm=sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 15}, yticklabels=cols, xticklabels=cols)
plt.show()
'''

# 회귀분석 수행(2단계)
result = sm.ols(formula='satis ~  + fat + kcal + serving_size + carbo + sugar + protein + saturated_fat + trans_fat + cholesterol + salt + calcium', data=df).fit()

# 요약결과 출력
print(result.summary())

'''
# 회귀계수를 리스트로 출력, 리스트 인덱스 0은 절편임.
# print('Parameters : ', result.params)
print(type(result.params))
params_list = []
for num in range(5):
    params_list.append(result.params[num])
print(params_list)
print(type(params_list))
'''

''''
#회귀식 평가

# 평가를 수행할 파일을 가져옴(1단계)
df = pd.read_csv('gogotest.csv', encoding='EUC-KR')
# 데이터프레임으로 저장
xList = loasAsCsv('gogotest.csv')

# 회귀방정식을 이용한 예상 만족도 출력
predic_Y_list = []
predic_Y = 0
for i in range(len(xList)):
    predic_Y += params_list[i + 1] * xList[i]
predic_Y += params_list[0]

predic_Y_list.append(predic_Y)
print(predic_Y_list)




# result.params[0]

# R squared 출력
# print('Rsquaured : ', result.rsquared)

# 회귀계수에 대한 P-value 출력
# print('Pvalue :', result.pvalues)

# 모형의 적합값 출력
# print('Predicted values',  result.predict())
'''


'''


# 기존데이터와 예측결과 합치기(4단계)
print('\n # 리스트 더해주기!(리스트 두개 합치기)')
addedList = [1,2,3,4,5]
for tl in tempList:
    # tempList.index(tl)라는 부분은 tempList 리스트 내에서 tl이 몇번째 줄이냐 라는 값(int)이에요
    tl["새로운 컬럼!"] = addedList[tempList.index(tl)]
print(tempList)

# 파일로 저장하기(5단계)
saveAsCsv(tempList,fileName='최종파일')
'''
print('끗')