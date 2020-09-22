# nestedDict.py
mylist = [('sale 무료 배송 할인', '스팸'), ('일정 변경', '일반'), ('sale 변경', '일반')]
print(mylist)
print('-'*30)

words = set() # 단어들을 저장할 집합

# 카테고리별 각 단어들의 빈도수를 저장할 중첩 사전
word_dict = {}
category_dict = {} # 카테고리별 빈도수를 저장할 사전

for email, cate in mylist :
    if cate in category_dict:
        category_dict[cate] += 1
    else :
        category_dict[cate] = 1

    # 단어별 분리
    result = email.split(' ')
    for one in result :
        words.add(one)

    if not cate in word_dict:
        word_dict[cate] = {}

    for one in result :
        if one in word_dict[cate]:
            word_dict[cate][one] += 1
        else:
            word_dict[cate][one] = 1

print('words 집합 : ', words)
print('카테고리 사전 :')
print(category_dict)
print('워드 사전 :')
print(word_dict)