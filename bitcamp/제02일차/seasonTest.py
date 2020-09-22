# seasonTest.py
# 해당 월과 계절을 출력해주는 프로그램 작성

month = int(input('달을 입력하세요.'))

# 힌트 : 가을(7~9) --> 7이상이고, 9이하이면 가을
# 입력 : 9
# 9월은 가을입니다.
if month >= 3 and month <= 5 :
    season = '봄'
elif month >= 6 and month <= 8 :
    season = '겨울'
elif month >= 9 and month <= 11 :
    season = '가을'
elif month in [12, 1, 2]:
    season = '겨울'
else :
    season = '무제'

print('%d월은 %s입니다' % (month, season))