# randomExam01.py
import random

# 주사위를 10번 던져서 나온 눈의 총합을 구해주는 jusawee 함수를 만들어 보세요.
# 단, 시도 회수가 입력 되지 않으면 5번을 던진다.
def jusawee(su=5):
    total = 0
    for idx in range(su):
        rnd = random.randint(1, 6)
        print('%d번째 나온 눈금 : %d' % (idx+1, rnd))
        total += rnd

    print('총합 : %2d' % total )

sido = 10 # 시도 회수
jusawee(sido)
print('-'*20)

jusawee()
print('-'*20)