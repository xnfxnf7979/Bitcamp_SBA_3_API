# for01.py
# range() 함수 : 반복문에서 특정 횟수만큼 요소들을 반복시키고자 할 때 사용합니다.
# range([start, ]end[, step])
# for idx in range(1, 11):
#     print(idx)
# print('-'*30)
#
# for idx in range(11):
#     print(idx)
# print('-'*30)
#
# for idx in range(1, 10, 2):
#     print(idx)
# print('-'*30)
#
# # index
# for idx in range(10, 1, -1):
#     print(idx)
# print('-'*30)

# 1부터 10까지의 총합 구하기
total = 0

for xxx in range(1, 11):
    total += xxx

print('총합 01 : %d' % (total))

# 1 + 4 + 7 + 10 + .... + 100 = 1717
total = 0

for xxx in range(1, 101, 3):
    total += xxx

print('총합 02 : %d' % (total))

# 97 + 92 + 87 +... + 7 + 2 = 990
total = 0

for xxx in range(97, 1, -5):
    total += xxx

print('총합 03 : %d' % (total))

# 1*1 + 6*6 + 11*11 + ... + 96*96 = 63670
total = 0

for xxx in range(1, 97, 5):
    total += pow(xxx, 2)
    # total += xxx ** 2
    # total += xxx * xxx

print('총합 04 : %d' % (total))

# abs() : 절대 값으로 변경해주는 함수입니다.
print(abs(-15))

# 사용자가 숫자를 하나 입력 받고, 1부터 해당 수까지의 총합 구하기
# 숫자 입력 : 5
# 출력 결과 : 1부터 5까지의 합은 55입니다.
# 만약 음수 값을 입력하면 절대 값으로 변경하도록 합니다.
# 숫자 입력 : -10
# 출력 결과 : 1부터 10까지의 합은 55입니다.

su = int(input('정수 입력 : '))

if su < 0 :
    su = abs(su)

total = 0
for idx in range(1, su+1):
    total += idx

print('총합 05 : %d' % (total))