# DataFrameExam01.py
from pandas import DataFrame

sdata = {
    '도시':['서울', '서울', '서울', '부산', '부산'],
    'year':[2000, 2001, 2002, 2001, 2000],
    'pop':[1.5, 1.7, 3.6, 2.4, 2.9]
}
print(sdata)

myindex = ['one', 'two', 'three', 'four', 'five']
myframe = DataFrame(sdata, index=myindex)
print(type(myframe))
print('-' *30)

myframe.index.name = '호호호'
print(myframe.index)
print('-' *30)

myframe.columns.name = '하하하'
print(myframe.columns)
print('-' *30)

print(myframe.values)
print(type(myframe.values))
print('-' *30)

print(myframe.dtypes)
print('-' *30)

# T : 전치
print(myframe.T)
print('-' *30)

print(myframe)
print('-' *30)

mycolumns = ['pop', '도시', 'year']
newframe = DataFrame(sdata, columns=mycolumns)
print(newframe)
print('-' *30)


print('finished')