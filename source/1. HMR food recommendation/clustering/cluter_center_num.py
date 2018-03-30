import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth
from itertools import cycle
import pandas as pd

# Load data from input file / 데이터 가져오기

X = pd.read_csv('delete.csv')

# Estimate the bandwidth of X / X에 대한 대역폭 계산하기
#평균이동알고리즘에서 사용하는 내부커널의 밀도 추정 프로세스에 대한 매개변수로, 윈도우의 크기
#매우 중요 - 대역폭에 따라 알고리즘의 수렴속도와 최종 결과로 나올 군집의 수가 달라지기 때문
#대역폭이 작으면 군집수가 너무 많아지고, 대역폭이 크면 서로 구분해야 할 군집이 합쳐진다.
#quantile 매개변수는 대역폭의 추정 방식에 영향을 미침, 이 값이 클수록 추정한 대역폭의 값이 커져서 군집의 수가 줄어듦
bandwidth_X = estimate_bandwidth(X, quantile=0.035, n_samples=len(X))

# Cluster data with MeanShift / 평균 이동 군집화 모델을 학습
meanshift_model = MeanShift(bandwidth=bandwidth_X, bin_seeding=True)
meanshift_model.fit(X)

# Extract the centers of clusters / 각 군집의 중심 구하기
cluster_centers = meanshift_model.cluster_centers_
print('\nCenters of clusters:\n', cluster_centers)

# Estimate the number of clusters / 군집의 개수 구하기
labels = meanshift_model.labels_
num_clusters = len(np.unique(labels))
print("\nNumber of clusters in input data =", num_clusters)

# Plot the points and cluster centers / 그래프 그리기
# plt.figure()
# markers = 'o*xvs'
# for i, marker in zip(range(num_clusters), markers):
#     # Plot points that belong to the current cluster
#     plt.scatter(X[labels==i, 0], X[labels==i, 1], marker=marker, color='black')
#
#     # Plot the cluster center / 현재 군집의 중심을 그래프로 그리기
#     cluster_center = cluster_centers[i]
#     plt.plot(cluster_center[0], cluster_center[1], marker='o',
#             markerfacecolor='black', markeredgecolor='black',
#             markersize=15)

#plt.title('Clusters')
#plt.show()
