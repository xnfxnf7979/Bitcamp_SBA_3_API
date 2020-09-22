# graphSigmoid.py
# 시그모이드 함수를 그려 봅니다.
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(weight, x, b = 0, asc = True):
    if asc == True:
        return 1/(1+ np.exp(-weight * x - b))
    else:
        return 1 / (1 + np.exp(+weight * x + b))

# arange 함수는 파이썬의 range와 유사함
x = np.arange(-5.0, 5.1, 0.1)

weight, bias = 1, 0
y1 = sigmoid(weight, x)
mylabel = 'y=' + str(weight) + '*x' + str(bias)
plt.plot(x, y1, color='g', label=mylabel)

weight, bias = 5, 0
y2 = sigmoid(weight, x, bias)
mylabel = 'y=' + str(weight) + '*x' + str(bias)
plt.plot(x, y2, color='b', label=mylabel)

weight, bias = 5, 3
y3 = sigmoid(weight, x, bias)
mylabel = 'y=' + str(weight) + '*x' + str(bias)
plt.plot(x, y3, color='r', label=mylabel)

weight, bias = 5, 3
y4 = sigmoid(weight, x, bias, asc=False)
mylabel = 'y=' + str(weight) + '*x' + str(bias)
plt.plot(x, y4, color='r', label=mylabel)


plt.axhline(y=0, color='black', linewidth=1, linestyle='dashed')
plt.axhline(y=1, color='black', linewidth=1, linestyle='dashed')

plt.title('sigmoid function')
plt.ylim(-0.1, 1.1)
plt.legend(loc='best')

filename = 'sigmoid_function.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')
print('finished')