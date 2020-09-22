# mnistInfo.py
# 손글씨 데이터 셋을 다운로드 하고, 데이터의 구조를 살펴 보도록 합니다.
# 임의의 하나의 데이터를 이용하여 시각화 해 봅니다.
from tensorflow.python.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print('x_train.shape : ', x_train.shape)
print('-'*40)

print('x_train.dtype : ', x_train.dtype)
print('-'*40)

print('x_train.ndim : ', x_train.ndim)
print('-'*40)

print('y_train : ', y_train)
print('-'*40)

print('x_test.shape : ', x_test.shape)
print('-'*40)

print('len(y_test) : ', len(y_test))
print('-'*40)

print('y_test : ', y_test)
print('-'*40)

import matplotlib.pyplot as plt

digit = x_train[100] # 숫자 1개
plt.imshow(digit)
filename = 'mnist_image.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')
print('finished')