# function01.py
# 함수 : 반복적인 행위를 수행하기 위하여 미리 작성해 놓은 소스 코드
# 매개 변수 : 함수의 소괄호 부분에 입력해주는 값
# = 인자 = 인수 = argument = parameter
# 함수의 종류 : 내장 함수(abs, pow, sum, min 등등)
#              사용자 정의 함수

# 함수를 작성하는 절차
# step 1 : 함수 구현
# def는 define의 줄인말입니다. ~~를 정의하다
# 함수 이름은 임의로 작성하시면 됩니다.
# return 구문은 데이터를 반환할 때 사용하고, 옵션 사항입니다.
# return 구문을 사용하지 않으면 None이 반환합니다.
# None 키워드는 부정적인 용어인데, void, empty, no 등의 의미로 사용되는 개념입니다.

'''
def 함수이름(매개변수1, 매개변수2, ...):
    하고자 하는 일을 작성
    [return 반환할 데이터 명시]
'''
# step 2 : 함수 호출

# 어떠한 숫자를 입력하면 5를 더해주는 함수 구현
def plus5(su): # 함수의 정의(구현)
    return su + 5

su1 = 14
result = plus5(su1) # 함수를 호출
print('결과 01 : {}'.format(result))
print('결과 02 : {}'.format(plus5(100))) # 함수 호출

for idx in range(3, 12, 4):
    print(plus5(idx))

print('-'*30)

mylist = [10, 20, 30]

total = 0
for item in mylist:
    total += plus5(item)

print(total)
print('-'*30)

mytuple = tuple([4, 8, 12])
for item in mytuple:
    print(plus5(item))
print('-'*30)







