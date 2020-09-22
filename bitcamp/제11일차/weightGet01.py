# weightGet01.py
# 경사 하강법을 이용한 w 값의 갱신
# 다음 데이터와 지정한 가중치를 이용하여 w의 값이 어떻게 변화되는 살펴 보도록 합니다.

# 가중치 가정 (w1, w2, w3, b) = (1 0 1 0)
# 비용 함수(E) = (H-y)**2 * 1/2
# 학습률은 alpha = 0.001이라고 가정합니다.
'''
x1  x2 x3 b  y
1   2  3  1  3
5   6  7  1  6

y = H = w1*x1 + w2*x2 + w3* x3 + b
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

alpha = 0.001
weight = np.array([[1, 0, 1, 0]])
x=np.array([[1, 5], [2, 6], [3, 7], [1, 1]])
y=np.array([[3, 6]])

Hypo = list() # 가설 데이터 리스트
Error = list() # 비용 함수의 오차 목록

def get_new_weight(weight, x):
    H=np.dot(weight, x) # 가설 데이터 정보
    # print('H :', H)
    # tolist()는 넘파이 배열을 파이썬 list으로 변환
    Hypo.append(H.tolist())

    E=0 # 비용 함수
    for idx in range(H.shape[1]):
        E += 1/2 * (H[0][idx] - y[0][idx])**2
    # print('E :', E)
    Error.append(E)

    deltaE=np.dot(np.subtract(H, y), np.transpose(x))
    # print('deltaE :', deltaE)

    new_weight = weight - alpha * deltaE
    # print('new_weight :', new_weight)

    return new_weight

for idx in range(15000):
    weight = get_new_weight(weight, x)
    # print('weight :', weight)
    # print('-'*30)

plt.figure()
first = [item[0][0] for item in Hypo]
plt.plot(first)

plt.title('y1 label에 대한 가설 H1 그래프')
plt.xlabel('epoch')
plt.ylabel('가설')
filename = 'weightGet01_01.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')

plt.figure()
second = [item[0][1] for item in Hypo]
plt.plot(second)

plt.title('y2 label에 대한 가설 H2 그래프')
plt.xlabel('epoch')
plt.ylabel('가설')
filename = 'weightGet01_02.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')

plt.figure()
plt.plot(Error)
plt.title('비용 함수 그래프')
plt.xlabel('epoch')
plt.ylabel('비용')
filename = 'weightGet01_03.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')

print('finished')
