# listTest4.py
# list 자료 구조
# 순서를 가지고 있는 데이터 유형
# 인덱싱, 슬라이싱이 가능하고, 대괄호를 사용한다.
# 모든 유형의 데이터 사용이 가능하다.
# 관련 함수 : list()
# 함수들 : len(), append(), insert(), clear()
# sort(), reverse(), remove(), extend(), count(), index()

mylist = ['강감찬', '김유신']
print(mylist)

mylist.append('이순신')
mylist.append('안중근')
mylist.insert(2, '이성계')

# 마지막 요소 구하기
print(mylist[len(mylist)-1])

print(len(mylist))

# mylist.clear()
mylist.sort()
print(mylist)

mylist.reverse()
print(mylist)

# 인덱싱을 이용한 읽기와 쓰기
print(mylist[2]) # 읽기
mylist[2] = '이완용' # 쓰기

mylist.remove('김유신')

newlist = ['윤봉길', '신사임당', '강감찬']
mylist.extend(newlist)

print(mylist.count('강감찬'))

# '이완용'은 몇번째 있나요?(힌트 : index 함수 사용)
print('index :', mylist.index('이완용'))
print('index2 :', mylist.index('강감찬', 4))

print(mylist)

# 슬라이싱 테스트
mylen = len(mylist) # 전체 갯수
print(mylist[4:6])
print(mylist[1:mylen:2])
print(mylist[0:mylen:2])

# 요소의 인덱스가 3의 배수인 항목들만 추출
print(mylist[0:mylen:3])

anydata = [10, '가가', 12.34, [10, 20, 30]]
print(anydata)