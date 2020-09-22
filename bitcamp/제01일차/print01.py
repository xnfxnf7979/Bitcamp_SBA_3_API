# print01.py
# 샵을 붙이면 comment가 됩니다.(주석)
# print 함수 : 문장을 출력합니다.
print('동해물과' '백두산이')
print('동해물과' '백두산이' '마르고' '닳도록')
# 콤마를 붙이면 띄워쓰기가 됩니다.
print('동해물과', '백두산이', '마르고', '닳도록')

# 실행을 위한 단축키는 Shift + F10을 누르시면 됩니다.
# end 옵션의 기본 값은 엔터 키
# 내가 값을 입력하게 되면 엔터 키는 없어지고 , 지정한 값으로 대체가 됩니다.
print('안녕하세요', end=' ')
print('홍길동님')

# input() 함수 : 사용자로 하여금 입력을 유도하는 함수
# 주의 : 입력된 데이터는 모두 문자열로 인식을 합니다.
print('이름을 입력 ')
name = input()
age = input('나이 입력')
print('이름 :', name, ', 나이 :', age)

# 데이터 형변환 : 바뀔타입(바꿀데이터)
# int는 정수형, str은 문자열형
newage = int(age) + 5
print('5년뒤 나이 :' + str(newage))

kor = int(input('국어 점수 입력 :'))
eng = int(input('영어 점수 입력 :'))
math = int(input('수학 점수 입력 :'))

total = kor + eng + math
print('총점 :', total)