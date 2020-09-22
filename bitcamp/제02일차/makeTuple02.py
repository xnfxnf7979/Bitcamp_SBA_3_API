# makeTuple02.py
tuple01 = ('김철수', 40, 50, 60)
tuple02 = ('박영희', 50, 60, 70)

mytuple = (tuple01, tuple02)
print(mytuple)

print('총 인원수 : ', len(mytuple), '명', sep='')

saram = mytuple[0][0]
jumsu = mytuple[0][1:]
print(saram)
print(jumsu)

hap = sum(jumsu)
mylen = len(jumsu)
average = hap/mylen
print('이름 : ', saram, ', 평균 : ', average, '점', sep='')

print('국어의 평균')
kor = mytuple[0][1] + mytuple[1][1]
print(kor/2)











