# if04.py
# 다중 택일 구문
name = '김철수'
score = 82
grade = '' # 학점(A, B, C, D, F)

if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else : # 나머지 다른 조건들(the others)
    grade = 'F'

print('이름 : %s' % (name))
print('점수 : %d' % (score))
print('학점 : %s' % (grade))