# bs4Exam02.py
# 카페 400번 문서에서
# 첨부(2주차).zip 파일, 파이썬 Konlpy 설정하기.txt 파일 다운로드하기
# 첨부(2주차).zip 파일 압축 해제하시고, 파일 추가
# 참조 파일(fruits.html)을 이용하여 필요한 정보를 추출해 보도록 합니다.
# BeautifulSoup 패키지 : html 문서에서 데이터를 추출하고자 할 때 사용하는 패키지

from bs4 import BeautifulSoup
# open 함수 : 운영체제 내의 파일을 열고자 할때 사용하는 내장 함수
# 파일 이름 : 'fruits.html', 'r'는 read(읽기)
html = open('fruits.html', 'r', encoding='utf-8') # fruits.html

# 파서 : html 문서가 제대로 잘 만들어진것인지를 검증하는 객체
# soup = BeautifulSoup(해당문서, '파싱문자열')
soup = BeautifulSoup(html, 'html.parser')
# print(type(soup))

body = soup.select_one('body')
ptag = body.find('p')

# 읽기
print(ptag)
print(ptag['class'])
print(ptag['align'])

# 쓰기
# print(ptag['id'])
ptag['id'] = 'apple'
print(ptag['id'])
print(ptag)

body_tag = soup.find('body')
print(body_tag)
print('-'*30)

idx = 0
# white character : 눈에 보이지 않는 글자들
for child in body_tag.children:
    idx += 1
    print(str(idx) + '번째 요소 :', child)
    print('#'*20)
print('-'*30)

mydiv = soup.find('div')
print(mydiv)
print('나의 부모는')
print(mydiv.parent)
print('-'*30)

# attrs 매개 변수는 속성(attribute)을 이용하여 찾고자 할 때 사용합니다.
mytag = soup.find('p', attrs={'class':'hard'})
print(mytag)
print('-'*30)

print(mytag.find_parent())
print('-'*30)

print('mytag 태그 모든 상위 부모 태그들의 이름')
parents = mytag.find_parents()
for p in parents :
    print(p.name)
