# whileTest01.py
# 숫자 5를 입력 받고 5단 출력하기
# 5 *1 = 5
# 5 * 2 = 10
# 음수가 들어 오면 절대값으로 변경하여 출력하기
dan = int(input('몇 단 출력 : '))

if dan < 0 :
    dan = abs(dan)

i = 1

while i < 10 :
    mystring = '%d * %d = %2d' % (dan, i, (dan*i))
    print(mystring)
    i += 1

print('finished')
