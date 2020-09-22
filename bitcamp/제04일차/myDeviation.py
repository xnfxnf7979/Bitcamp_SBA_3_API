# myDeviation.py

# 표준 편차 구하기
import math # 수학과 관련된 모듈

def deviation(list1):
    length = len(list1)
    total = 0.0
    for item in list1:
        total += item

    average = total / length

    imsi = 0.0
    for item in list1:
        imsi += (average - item) ** 2

    imsi = imsi / length

    return math.sqrt(imsi)

# 다음 리스트를 이용하여 표준 편차를 구해주는 함수 deviation을 구현해 보세요.
mylist = [10, 30, 40, 80]
result = deviation(mylist)
print('표준 편차 :', result)

# print(math.sqrt(650))
# print(math.sqrt(4))

'''
1) 평균을 구합니다.
평균 = 총합(160)/요소갯수 = 160/4 = 40

2) (점수 - 평균)을 제곱을 모두 누적시킵니다.
900 + 100 + 0 + 1600 = 2600

3) 2)의 결과에 돗수를 나눕니다.
2600/요소갯수 = 2600/4 = 650

4) 3)에 루트를 씌웁니다.
루트 650 = 25.4950975

힌트 : sqrt( 650 )
루트는 외부 모듈인 math 모듈의 sqrt를 사용하면 됩니다.
'''