# whileTest02.py
# 무한 whileLoop : 반복 횟수가 몇 번인지 모른 경우
# 어느 조건을 충족하면 break 구문을 사용하여 반드시 종료해야 합니다.

# cnt = 0
# while True:
#     print('a' + str(cnt))
#     cnt += 1
#     if cnt == 5 :
#         break

# 사용자가 입력한 시험 점수에 대한 평균과 개수를 구해 봅니다.
# 음수 값이 입력되면 프로그램을 종료하도록 합니다.
total = 0 # 총점
count = 0 # 시험 본 횟수
average = 0.0 # 평균 점수

while True :
    jumsu = int(input('점수 입력 :'))
    if jumsu <= 0 :
        break
    total += jumsu
    count += 1

average = total / count

print('총 시험 횟수 : {}'.format(count))
print('총점 : {}'.format(total))
print('평균 : %.3f' % (average))

print('finished')





