from konlpy.tag import Komoran

sentence = '국정 농단 태블릿 PC, 설진욱, 가나다라'
print('# before user dic')
komo = Komoran()
print(komo.pos(sentence))
''' 
    임시 파일을 만들어서 위의 코딩을 테스트 해주세요. 
'''
'''
결과값 # before user dic
[('국정', 'NNG'), ('농', 'NNG'), 
('단', 'NNG'), ('태블릿 PC', 'NNP'), (',', 'SP'), 
('설', 'NNB'), ('진', 'NNP'), 
('욱', 'NA'), (',', 'SP'), ('가나', 'NNP'), ('다라', 'NNP')]
'''