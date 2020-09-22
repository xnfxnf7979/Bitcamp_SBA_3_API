# arrayDimShape.py
# 배열의 크기(dimension)와 형상(shape)
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6]])

# ndarray : n(정수) d(차원) array(배열/행렬)
print(type(data))

# ndim 속성
print('rank :', data.ndim)
print('형상 :', data.shape)
print('몇행이니 :', data.shape[0])
print('몇열이니 :', data.shape[1])

# int8 , int16, int32, float64
print('자료형 :', data.dtype)

print(data[0][0], data[1][1], data[1][2])
print('-'*30)

print( data + data )
print('-'*30)

mylist = [1, 2]
print( mylist + mylist )
print('-'*30)

print( data * 10 )
print('-'*30)

print( data * data )
print('-'*30)

print( 1 / data )
print('-'*30)

print( data ** 0.5 )
print('-'*30)


print('finished')








