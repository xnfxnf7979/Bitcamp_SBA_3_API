# numpyEx02.py
# 1차원 배열을 형상 변경, 행렬 연산, 전치
import numpy as np

a = np.array([-1, 3, 2, -6]) # 1차원
b = np.array([3, 6, 1, 2])
print(a.ndim)
print(a.shape)

A = np.reshape(a, [2, 2])
print(A.ndim)
print(A.shape)

B = np.reshape(b, [2, 2])
print(A)
print(B)
print('-'*30)

# matmul : MATrix MULtiply
result3_1 = np.matmul(A, B)
result3_2 = np.matmul(B, A)
print(result3_1)
print('-'*30)

print(result3_2)
print('-'*30)

b = np.reshape(b, [1, 4])
a = np.reshape(a, [1, 4])
b2 = np.transpose(b) # 전치

print(a) # 1*4
print('-'*30)

print(b) # 1*4
print('-'*30)

print(b2)
print('-'*30)

result3_3 = np.matmul(a, b2)
print(result3_3)
print('-'*30)









