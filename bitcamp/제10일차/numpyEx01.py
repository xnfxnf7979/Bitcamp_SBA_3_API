# numpyEx01.py
import numpy as np

data = np.array([[10, 20], [30, 40]])
print(data)

# 모든 요소의 합을 구해줍니다.
result = np.sum(data)
print(result)
print('-'*20)

# 행을 따라가면서, 열단위로 합산
result = np.sum(data, axis=0)
print(result)
print('-'*20)

result = np.sum(data, axis=1)
print(result)
print('-'*20)

result = np.mean(data)
print(result)
print('-'*20)

result = np.min(data)
print(result)
print('-'*20)

result = np.max(data)
print(result)
print('-'*20)

result = np.max(data, axis=0)
print(result)
print('-'*20)

print('finished')