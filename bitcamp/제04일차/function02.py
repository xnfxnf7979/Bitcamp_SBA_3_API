# function02.py
# 두 정수의 합을 구해주는 함수를 구현하고 테스트하세요.
# add(5, 6) -> 11
# add(100, 200) -> 300

def add(first, second):
    return first + second

su1 = 5
su2 = 6
result = add(su1, su2)
print('결과 : {}'.format(result))

su1 = 100
su2 = 200
result = add(su1, su2)
print('결과 : {}'.format(result))