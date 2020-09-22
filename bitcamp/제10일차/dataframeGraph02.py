# dataframeGraph02.py
import pandas as pd
import matplotlib.pyplot as plt
filename = 'ex802.csv'

plt.rc('font', family='Malgun Gothic')

myframe = pd.read_csv(filename, index_col='type', encoding='utf-8')
myframe.index.name = '자동차 유형'
myframe.columns.name = '도시(city)'

myframe.plot(kind='bar', rot=0, title='차량 유형별 지역 등록 댓수', legend=True)

# plt.legend(loc='best')
# plt.legend(loc=4)

filename = 'graph01.png'
plt.savefig(filename)
print(filename + ' 파일 저장')

print(myframe)

myframeT = myframe.T
print(myframeT)

myframeT.plot(kind='bar', rot=0, title='지역별 차량 유형 등록 댓수', legend=True)
filename = 'graph02.png'
plt.savefig(filename)
print(filename + ' 파일 저장')

myframeT.plot(kind='bar', rot=0, stacked=True, title='지역별 차량 유형 등록 댓수', legend=True)
filename = 'graph03.png'
plt.savefig(filename)
print(filename + ' 파일 저장')

print('finished')

