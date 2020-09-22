# indexingSlicing.py
str1 = 'Hello Korea'

# 인덱싱 : 대괄호를 사용하여 특정 위치의 요소를 추출해 내는 것
print(str1[0])
print(str1[1], str1[6])
# 마이너스가 나오는 경우 뒷쪽에서 카운터 하되 1 base가 됩니다.
print(str1[-3])

# 'KHa'를 출력해 보세요.
print(str1[6], str1[0], str1[10], sep='')

# 슬라이싱 : 전체 내용 중에서 일부 내용을 연속적으로 추출하는 것
# [from:to:step] : step의 기본 값은 1, from의 기본 값은 0
# from <= 슬라이싱 < to
print(str1[0:5])
print(str1[:5])
print(str1[0:5:2])

ssn = '881120-1234567'

apos = ssn[0:6]
print('앞자리 :', apos)

# 뒤자리 추출
dpos = ssn[7:]
print('뒤자리 :', dpos)

aa = ssn[7]

if aa == '1' or aa == '3':
    print('남')
else:
    print('여')

rainbow = ['빨', '주', '노', '초', '파', '남', '보']

another = rainbow[4:7]
print(another)

even = rainbow[0:7:2]
print(even)

odd = rainbow[1:7:2]
print(odd)

abcd = rainbow[-3:-1]
print(abcd)


