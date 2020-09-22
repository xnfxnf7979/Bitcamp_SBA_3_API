# linearRegression01.py
# 사이킷-런을 이용한 회귀 분석
# 결정 계수 : 실제 값이 예측 값과 얼마 정도의 일치성을 보이는지를 나타내는 척도
# 값은 0부터 1사이의 값으로, 1에 가까우면 설명력이 좋다 라고 표현합니다.
# R-squared = 1 - Σ(y-H)**2 / Σ(y-bary)**2
# y는 실제 정답, H: 가설로 도출된 값, bary의 실제 정답의 평균 값

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

# 학습용 데이터 셋 : 'linearTest01.csv'
# 테스트용 데이터 셋 : 'linearTest02.csv'

filename = 'linearTest01.csv'
# skiprows : 머리글 1행은 제외
training = np.loadtxt(filename, delimiter=',', skiprows=1)
print(training)

x_column = training.shape[1] - 1

x_train = training[:, 0:x_column]
y_train = training[:, x_column:]

# 모델 객체 생성
model = LinearRegression()

model.fit(x_train, y_train) # 학습

print('기울기(w) : ', model.coef_) # w 값
print('절편(b) : ', model.intercept_) # b 값

# residual(잔차)
print('잔차의 제곱 합(cost) : ', model._residues)

# 시각화
plt.title('그래프')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x_train, y_train, 'bo')

train_pred = model.predict(x_train)

plt.plot(x_train, train_pred, 'r') # 회귀 선

filename = 'linearRegression.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')

# 테스트 용 데이터 셋
filename = 'linearTest02.csv'
testing = np.loadtxt(filename, delimiter=',', skiprows=1)
print(training)

x_column = testing.shape[1] - 1

x_test = testing[:, 0:x_column]
y_test = testing[:, x_column:]

# print(y_test)
# 산술 연산에 의한 결정 계수 구하기
y_test_mean = np.mean(np.ravel(y_test))

# TSS) 편차의 제곱의 총합
TSS = np.sum((np.ravel(y_test)-y_test_mean)**2)

# RSS) 회귀식과 평균 값의 차이의 총합
RSS = np.sum((np.ravel(y_test)-np.ravel(model.predict(x_test)))**2)

# 결정 계수 = 1 - RSS/TSS
R_Squared = 1 - (RSS/TSS)
print('R_Squared 01 : ', R_Squared)

print('R_Squared 02 : ', model.score(x_test, y_test))

print('finished')