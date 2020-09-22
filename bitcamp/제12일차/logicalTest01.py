# logicalTest01.py
#
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

filename = 'logicalTest01.csv'
data = np.loadtxt(filename, delimiter=',')

table_col = data.shape[1] # 2
y_column= 1
x_column = table_col - 1 # 2 - 1 = 1

# 기출 문제
x_train = data[:, 0:x_column]
y_train = data[:, x_column:]

model = Sequential()

# 퍼셉트론 : 전구(0, 1)처럼 0과 1의 값을 가지고 있는 신경망
# 퍼셉트론이 회귀나 로지스틱 회귀이나 다른 머신러닝으로 바뀌기 위해서는 함수를 지정해줄 필요가 있다.
# 이때 사용되는 함수를 활성화 함수(activation function)라고 부릅니다.
# 회귀 : 'linear', 로지스틱 회귀 : sigmoid 등등
model.add(Dense(units=y_column, input_dim=x_column, activation='sigmoid'))

# 비용(손실_loss) 함수는 이진 분류이므로 'binary_crossentropy'을 사용하면 됩니다.
# optimizer 사용시 지정 문자열을 사용해도 되지만, 객체 생성을 통하여 만들 수 있습니다.
learning_rate = 0.1 # 학습율

import tensorflow as tf
sgd = tf.keras.optimizers.SGD(lr=learning_rate) # 객체 생성
model.compile(loss='binary_crossentropy', optimizer=sgd)

model.fit(x = x_train, y = y_train, epochs=2000, verbose=0)

x_test = [[5], [11]] # 풀어 볼 문제

# 해당 모델에 훈련용 데이터를 이용하여 확률 값을 예측합니다.
H2 = model.predict(x_train)
print(H2)
print('-'*30)

for item in x_test :
    # H = model.predict(np.array([item]))
    # print(H)
    # print('-'*30)

    # predict_classes : 정답이 가지고 있는 클래스의 값을 출력해 줍니다.
    pred = model.predict_classes(np.array([item])) # 예측 값
    # pred = np.argmax(model.predict([item]), axis=1)
    print('테스트 데이터 :', np.array([item]))
    print(pred)

print('finished')