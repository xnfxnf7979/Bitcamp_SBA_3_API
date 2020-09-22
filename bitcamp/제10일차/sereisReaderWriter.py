# sereisReaderWriter.py

from pandas import Series

myindex = ['서울', '부산', '광주', '대구', '울산', '목포', '여수']
mylist = [50, 60, 40, 80, 70, 30, 20]
myseries = Series(data=mylist, index=myindex)
print(myseries)
print('-'*30)

print(myseries['대구'])
print(type(myseries['대구']))
print('-'*30)

print(myseries[['대구']])
print(type(myseries[['대구']]))
print('-'*30)

# 문자열 색인으로 슬라이싱하는 경우 양쪽 모두 포함됨.
print(myseries['대구':'목포'])
print('-'*30)

print(myseries[[2]])
print('-'*30)

# 콜론으로 슬라이싱하는 경우에는 대괄호 1개
print(myseries[0:5:2])
print('-'*30)

# 콤마를 사용하는 경우 대괄호 2개
print(myseries[[1, 3, 5]])
print('-'*30)

myseries[2] = 22 # 쓰기
print(myseries)
print('-'*30)

myseries[2:5] = 33
print(myseries)
print('-'*30)

# 서울과 대구만 55로 변경하기
myseries[['서울', '대구']] = 55
print(myseries)
print('-'*30)

myseries[0::2] = 77
print(myseries)
print('-'*30)