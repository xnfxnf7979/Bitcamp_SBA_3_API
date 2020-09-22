# abs01.py
# 어떠한 숫자에 대하여 절대 값으로 만들어 주는 함수 만들기

# 매개 변수 이름은 임의의 이름이어도 된다.
def absolute(n):
    if n < 0 :
        n = -n
    return n

su = -5
result = absolute(su) # 함수 호출
print('결과01 : {}'.format(result))

# 다음 리스트의 모든 요소를 절대 값으로 변경하여 새로운 리스트로 만들어 주세요.
mylist = [2, -4, -7]

res = [absolute(item) for item in mylist]
print(res)
print('finished')













