# corrTest03.py
# 상관 관계 분석

# numpy : NUMerical PYthon
# 배열이나 행렬을 이용하여 수치 해석, 머신 러닝 등에 사용되는 모듈
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

def correlation(x, y): # 상관 계수를 구해주는 함수
    bar_x = x.mean()
    bar_y = y.mean()

    bunja = np.sum((x-bar_x)*(y-bar_y))
    print('분자 : ', bunja)

    left = np.sum((x-bar_x)**2)
    right = np.sum((y - bar_y) ** 2)
    bunmo = np.sqrt(left*right)
    print('분모 : ', bunmo)

    return bunja / bunmo

x = np.array([3, 5, 8, 11, 13]) # 배열
y = np.array([1, 2, 3, 4, 5]) # 배열

print('상관 계수 : ', correlation(x, y))

mymean = y.mean()
print(mymean)

mysum = np.sum(y)
print(mysum)

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


