# logisticRegression01.py

# 카페  https://cafe.naver.com/ugcadman/1113  아이리스 데이터 셋

import pandas as pd

filename= 'iris.csv'
data = pd.read_csv(filename)

# print(data.shape)
# print('-'*40)
#
# print(data.columns)
# print('-'*40)

x_data = data[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
y_data = data['Name']

# 총 150행 중에서 훈련 105행, 테스트 45행

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = \
    train_test_split(x_data, y_data, test_size=0.3)

# 데이터 속성들의 값의 차이가 너무 크면 학습이 잘 안됩니다.
# StandardScaler 클래스를 사용하여 평균 0, 표준 편차 1인 표준 정규 분포로 표준화를 수행합니다.

# print(x_train)
# print('-'*30)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

# print(x_train)
# print('-'*30)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)

train_score = model.score(x_train, y_train)
print('train 정확도 : %.3f' % (train_score))

test_score = model.score(x_test, y_test)
print('test 정확도 : %.3f' % (test_score))

print('회귀 계수')
print(model.coef_)
print(model.intercept_)

from sklearn.metrics import confusion_matrix

print('test result')
prediction = model.predict(x_test)

# confusion_matrix(정답데이터, 예측값)
cf_matrix = confusion_matrix(y_test, prediction)
print('confusion_matrix :')
print(cf_matrix)
print('-'*30)

# accuracy_score : 정확도를 구해주는 함수
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, prediction)
print('accuracy(정확도) : %.3f' % (100 * accuracy))
print('-'*30)

# 주요 분류와 관련된 metrics(지표)에 대한 보고서
from sklearn.metrics import classification_report

print('classification_report :')
cl_report = classification_report(y_test, prediction)
print(cl_report)
print('-'*30)

import seaborn as sns
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

#                                                      와이 엘
sns.heatmap(pd.DataFrame(cf_matrix), annot=True, cmap='YlGnBu', fmt='g')

plt.title('confusion matrix')
plt.ylabel('actual label')
plt.xlabel('prediction label')

filename = 'logisticRegression01_01.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')

'''
엑셀 파일을 이용하여 데이터를 읽습니다.
학습용 데이터와 훈련용 데이터를 7대3으로 나눕니다.
StandardScaler 클래스를 사용하여 평균 0, 표준 편차 1인 표준 정규 분포로 표준화를 수행합니다.
정확도를 구해봅니다.
confusion matrix 및 각 지표에 대하여 확인합니다.
HeatMap를 그려 봅니다.
'''
print('finished')
