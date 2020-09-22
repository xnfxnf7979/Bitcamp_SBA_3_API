# logicalTest02.py

# 엑셀 파일을 읽어서 훈련합니다.
# 테스트용 데이터를 이용하여 로지스틱 분류를 수행해 봅니다.
# 테스트 데이터) x_test = [[2, 1], [6, 5], [11, 6]]

import numpy as np
import tensorflow as tf

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

filename = 'logicalTest02.csv'
data = np.loadtxt(filename, delimiter=',')

table_col = data.shape[1]
y_column = 1
x_column = table_col - 1
x_data = data[:, 0:x_column]
y_data = data[:, x_column:]

model = Sequential()

model.add(Dense(units=y_column, input_dim=x_column, activation='sigmoid'))

learning_rate = 0.1 # 학습율

sgd = tf.keras.optimizers.SGD(lr = learning_rate )

model.compile(optimizer = sgd, loss='binary_crossentropy' )

model.fit(x = x_data, y = y_data, epochs = 2000, verbose=0 )

x_result = model.predict(x_data)
print(x_result)
print('-' * 30)

# 0 : 강아지, 1 : 고양이
x_test = [[2, 1], [6, 5], [11, 6]]

def getCategory(mydata):
    mylist = ['강아지', '고양이']
    print('예측 : %s, %s' % (mydata, mylist[mydata[0]]))

# flatten() : 차원을 1차원으로 만들어 주는 함수
for item in x_test :
    H = model.predict(np.array([item]))
    print(H.flatten())
    print('*' * 30)

    pred = model.predict_classes(np.array([item]))
    print('테스트 데이터 :', np.array([item]))
    getCategory(pred.flatten())
    print('-'*30)

print('finished')