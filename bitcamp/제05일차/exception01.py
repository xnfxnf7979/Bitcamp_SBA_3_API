# exception01.py

try :
    x = 4
    y = 0

    mydict = {'a':10}

    print(mydict['b'])

    mylist = [1, 2, 3]
    print(mylist[4])

    z = x / y
    print(z)

except ZeroDivisionError as err:
    # err이란 이름은 임의의 이름이어도 됩니다.
    print('0으로 나누시면 안됩니다.')
    print(err)

except IndexError as err:
    print('인덱스 범위 관련 오류 발생')
    print(err)

except KeyError as err:
    print('사전에 해당 키가 없습니다')
    print('찾고자 하는 키')
    print(err)

except Exception as err:
    print('기타 나머지 예외 발생')
    print(err)

else:
    print('예외가 없으면 이 라인이 실행됩니다.')

finally:
    print('예외 발생 여부와 상관이 없이 무조건 실행됩니다.')

# ZeroDivisionError

'''
예외 처리 : 예외가 사전에 발생하지 않도록 막음 조치를 취하는 것

ZeroDivisionError : 0으로 나누고자 했을 때
IndexError : 인덱스의 범위를 초과하여 접근시도 시 발생
KeyError : 사전에 해당 키가 존재하지 않을 때 

except 구문은 1번 이상 사용 가능하다.

예외 처리 방법
try :
    일반적인 코드 작성
except 예외클래스이름 [as 예외별칭]:
    적당한 오류 메시지 보여주기
else :
    예외가 없을 때 하고자 하는 내용 기록
finally :
    예외 발생 여부와 상관 없이 하고자 하는 내용 기록
    주로 마감 작업(파일 닫기, 데이터베이스 접속을 종료)    
'''