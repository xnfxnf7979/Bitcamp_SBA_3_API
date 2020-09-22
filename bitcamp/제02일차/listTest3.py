# listTest3.py
# 중첩 리스트
# 중첩된 갯수만큼 대괄호를 사용하면 됩니다.
saram01 = ['hong', '홍길동', 20, '용산']
saram02 = ['kim', '김철수', 30, '마포']
saram03 = ['kang', '강남', 40, '구로']

mylist = []
mylist.append(saram01)
mylist.append(saram02)
mylist.append(saram03)

print(mylist[1][2])

mylist[2][1] = '강호동'

print(mylist)

mylen = len(mylist)

# 세 사람의 평균 나이 구하기
totalage = mylist[0][2] + mylist[1][2] + mylist[2][2]
print('평균 나이 : %.2f' % (totalage/mylen))

# '홍길동$김철수$강호동' 출력해보기
# 이름만 추출하여 새로운 리스트를 만드세요 .
# join 함수를 사용하여 문자열 조립을 하면 됩니다.
newlist = [mylist[0][1], mylist[1][1], mylist[2][1]]
print('$'.join(newlist))