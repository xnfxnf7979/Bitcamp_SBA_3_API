# juminNumber.py
# 주민 번호는 반드시 14자리이어야 한다.
# 6번째 항목은 반드시 '-'이어야 합니다.
# 2번째 항목은 '0'또는 '1'이어야 합니다.
# 7번째 항목은 '0', '1', '2', '3'이어야 합니다.
def findSsn(juminno):
    if len(juminno) != 14 :
        return False

    if juminno[6] != '-' :
        return False

    if not juminno[2] in ['0', '1'] :
        return False

    if not juminno[7] in ['1', '2', '3', '4'] :
        return False

    if not(juminno[0:6].isdigit()) or not (juminno[7:].isdigit()):
        return False

    return True

# 문자열.isdigit() 함수를 이용하면 숫자들로 구성되었는지 확인이 가능
juminList = ['701226-1710566', '7012261710566', '703226-1710566', '701226-5710566', '911211-1나다라마바사']

for juminno in juminList :
    result = findSsn(juminno)
    if result == True :
        print('{}는 올바른 주민 번호'.format(juminno))
    else :
        print('{}는 잘못된 주민 번호'.format(juminno))

print('-'*30)