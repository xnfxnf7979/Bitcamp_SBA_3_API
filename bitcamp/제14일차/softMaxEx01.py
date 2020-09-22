# softMaxEx01.py
filename = 'softMaxEx01.csv'

import numpy as np
data = np.loadtxt(filename, delimiter=',')

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y = data[:, x_column:]

# 정답이 가질 수 있는 클래스 갯수
NB_CLASSES = 3

from sklearn.model_selection import train_test_split
seed = 1234
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3, random_state=seed)

# print(y_train) # 원핫 인코딩 적용 하기 이전

# np_utils : 원핫 인코딩을 수행해 줍니다.
from keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, num_classes=NB_CLASSES, dtype='float32')

# print(y_train) # 원핫 인코딩 적용한 이후의 값

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

model = Sequential()

model.add(Dense(units=NB_CLASSES, input_shape=(x_column,), activation='softmax'))

# 모델의 간략한 정보를 출력해줍니다.
model.summary()

# 'sgd' : 확률적 경사 하강법
# 산 정상에서 지면으로 가고자 할 때, 경사가 가장 급한 곳으로 이동하는 기법
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=1000, verbose=0)
print(history)
print('-'*30)

for idx in range(len(x_test)):
    H = model.predict(np.array([x_test[idx]]))
    pred = np.argmax(H, axis=-1)
    print('예측값 :', pred, end=' ')
    print('정답 : [%s]', int(y_test[idx]))
    print('가설 정보 :', H.flatten())
    print('*' * 30)

print('finished')










