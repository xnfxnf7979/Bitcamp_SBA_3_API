# surgeryTest.py
import numpy as np

filename = 'surgeryTest.csv'
data = np.loadtxt(filename, delimiter=',')

print(data.shape)

table_col = data.shape[1]
y_column = 1
x_column = table_col - 1

x = data[:, 0:x_column]
y = data[:, x_column:]

from sklearn.model_selection import train_test_split
# seed = 0
# x_train, x_test, y_train, y_test = \
#     train_test_split(x, y, test_size=0.2, random_state=seed)

x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.2)

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

model = Sequential()

model.add(Dense(units=30, input_dim=x_column, activation='relu'))

model.add(Dense(units=y_column, activation='sigmoid'))

# 정확도('accuracy')를 보여 주세요.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=30, batch_size=10, verbose=0)

# 모델 관련 속성
# input 텐서의 정보
print(model.inputs)
print('-'*30)

# output 텐서의 정보
print(model.outputs)
print('-'*30)

# model.add() 함수를 사용한 레이어들의 주소 정보
print(model.layers)
print('-'*30)

# metrics : 성능에 대한 지표
# 기본 값으로 비용 함수('loss')는 무조건 보여 줍니다.
# 더 추가하려면 compile 함수의 매개 변수 metrics에 리스트 형식을 넣어 주면 됩니다.
print(model.metrics_names)
print('-'*30)

pred = model.predict_classes(x_test)
for idx in range(len(pred)):
    label = y_test[idx]
    print('real : %.3f, prediction : %.3f' % (label, pred[idx]))

print('finished')









