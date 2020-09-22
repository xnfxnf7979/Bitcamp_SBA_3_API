# for02.py
# 1부터 10까지의 정수중에서 짝수의 총합과 홀수의 총합을 각각 구해 보세요.
odd = even = 0 # 합산을 누적할 변수

for idx in range(1, 11):
    if idx % 2 == 0 :
        even += idx
    else :
        odd += idx

print('홀수 총합 : %d' % (odd))
print('짝수 총합 : %d' % (even))

# 1부터 50까지의 정수중에서 3의 배수가 아닌 수
# sumA = 1 + 2 + 4 + 5 + ... + 50
# sumB = 3 + 6 + 9 + ... + 48
# sumA - sumB = 459
sumA = sumB = 0
for idx in range(1, 51):
    if idx % 3 == 0:
        sumB += idx
    else :
        sumA += idx

result = sumA - sumB
print('결과 : %d' % (result))