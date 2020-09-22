# dictControl.py
# 100번 반복한다.
# 매번 1부터 10사이의 임의의 수를 추출한다.(random 모듈)
# 이것을 사전에 담고, 최종 결과를 출력하도록 한다.('1':2, '2':5, ...)
# list comprehension을 사용하여 리스트로 만든 다음 mylist.sort() 함수를 사용하여 정렬하세요.

import random

mydict = {} # empty dict

for idx in range(1, 101):
    data = random.randint(1, 10)
    if data in mydict :
        mydict[data] += 1
    else:
        mydict[data] = 1

print(mydict)

mylist = [key for key in mydict.keys() ]
mylist.sort()

for key in mylist:
    print('숫자 %d는 %d번 추출' % (key, mydict[key]))

print('finished')


# 출력 결과 예시
# 숫자 1은 12번 추출
# 숫자 2은 5번 추출
# ...
# 숫자 10은 4번 추출