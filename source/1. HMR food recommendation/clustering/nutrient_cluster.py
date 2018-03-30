#패키지 불러오기
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
import pandas as pd
from pandas import DataFrame

# Load input data, 파일에서 입력데이터 가져오기 / delimiter - 구분자

X = pd.read_csv('plz.csv')

#kMeans 알고리즘 적용 전 군집의 개수부터 지정
num_clusters = 14

# Create KMeans object / init 매개변수는 군집의 초기 중심점을 선택하기 위한 초기화 방법을 지정, 무작위로 정하지 않고 효과적으로 지정하기 위해 k-means++를 사용
# n_cluster 매개변수는 군집의 수 지정 / n_init 매개변수는 최적의 결과를 도출할 때 까지 알고리즘을 반복할 횟수를 지정
kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)

# Train the KMeans clustering model / 학습!
kmeans.fit(X)

out=pd.DataFrame(kmeans.labels_)

X=pd.concat([X,out],1)

X.to_csv('cluster_plz.csv')

# def saveAsCsv():
#     df2 = X
#     df2.to_csv('return3.csv',index=False, encoding='EUC-KR')
#
# saveAsCsv()