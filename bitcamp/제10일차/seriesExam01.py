# seriesExam01.py
import matplotlib.pyplot as plt
from pandas import Series

plt.rc('font', family='Malgun Gothic')

myindex = ['강감찬', '홍길동', '이순신', '최영']
members = Series(data=[20, 60, 80, 40], index=myindex)
print(members)

# 그래프의 종류별 예제

# kind는 line, bar, barh, pie, kde(커널 밀도 추정)
# rot : 눈금 rotation
# ylim : y축 상하한 값
# color : 색상 지정
# legend: 범례, label : 범례에 들어갈 문자열
# stacked : 누적 그래프
members.plot(kind='bar', use_index = True, color=['r', 'g', 'b', 'y'], rot=0, ylim=[0, members.max() + 20])
# members.plot(kind='bar', use_index = False, color=['r', 'g', 'b', 'y'], rot=0, ylim=[0, members.max() + 20])

plt.title('학생별 국어 시험')
plt.xlabel('학생 이름')
plt.ylabel('점수')
# plt.grid(True)

ratio = 100 * members / members.sum()
print(ratio)

for idx in range(members.size):
    value = str(members[idx]) + '건' # 60건
    ratioval = '%.1f%%' % (ratio[idx]) # 20.0%
    plt.text(x=idx, y=members[idx] + 1, s=value, horizontalalignment='center')
    plt.text(x=idx, y=members[idx]/2, s=ratioval, horizontalalignment='center')

meanval = members.mean()

average = '평균 : %d건' % meanval
plt.axhline(y=meanval, color='r', linewidth=1, linestyle='dashed')
plt.text(x=0, y=meanval + 1, s=average, horizontalalignment='center')

filename = 'graph01.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨' )
print('finished')
