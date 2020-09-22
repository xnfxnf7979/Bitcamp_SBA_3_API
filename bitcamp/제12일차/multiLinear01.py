# multiLinear01.py
# 파일을 이용하여 7대 3으로 나누어서 테스트 하기
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

filename = 'multiLinear01.csv'
data = np.loadtxt(filename, delimiter=',')
print(data.shape)

table_col = data.shape[1]
y_column = 1 # 정답
x_column = table_col - y_column # 3-1=2, 입력

x = data[:, 0:x_column]
y = data[:, x_column:]

seed = 0
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3, random_state=seed)

model = Sequential()

model.add(Dense(units=y_column, input_dim=x_column, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(x_train, y_train, epochs=5000, batch_size=10, verbose=0)

# 가중치 정보를 출력해줍니다.
print(model.get_weights())

prediction = model.predict(x_test)

for idx in range(len(y_test)):
    label = y_test[idx]
    pred = prediction[idx]

    print('real : %f, prediction : %f' % (label, pred))

print('finished')