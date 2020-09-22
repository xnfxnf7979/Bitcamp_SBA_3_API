# word2vecTest.py
# 문재인대통령신년사.txt
from bs4 import BeautifulSoup
from konlpy.tag import Okt

print('파일이 생성됩니다... 잠시만 기다려 주십시요.')
myencoding = 'utf-8'
filename = '문재인대통령신년사.txt'
myfile = open(filename, 'rt', encoding=myencoding)
soup = BeautifulSoup(myfile, 'html.parser')
mydata = soup.text
# print(mydata)

results = [] # 결과 저장소
okt = Okt()

datalines = mydata.split('\n')
print(len(datalines))

for oneline in datalines :
    mypos = okt.pos(oneline, norm = True, stem = True)
    # print(mypos)

    imsi = []# 임시 리스트
    for word in mypos :
        if not word[1] in ['Josa', 'Eomi', 'Punctuation', 'Verb']:
            if len(word[0]) >= 2 :
                imsi.append(word[0])

    temp = (' '.join(imsi)).strip()
    results.append(temp)
    # break # 차후 삭제 예정

# print(results)

# 정제된 파일로 저장하기
prepro_file = 'word2vec.prepro'
with open(prepro_file, 'wt', encoding=myencoding) as myfile :
    myfile.write('\n'.join(results))

print(prepro_file + ' 파일 생성됨')

# word2vec : word(단어)들을 벡터로 만드는 알고리즘
# vector(벡터) : 크기와 방향을 가지고 있는 단위
# 스칼라 : only 값
# 단어들의 유사도 : 코싸인 유사도, 유클리디언 유사도, 맨하탄 유사도

from gensim.models import word2vec

# LineSentence : 분석을 하기 위한 sentence를 만들어 주는 함수
data = word2vec.LineSentence(prepro_file)
print(type(data))

# Word2Vec : 해당 sentence를 사용하여 word2vec에 대한 모델을 생성해줍니다.
# size : 벡터의 차원수, window : 윈도우 사이즈, min_count : 버리고자 하는 최소 빈도수
# sg : 1(skipgram), 0(cbow)
model = word2vec.Word2Vec(data, size=200, window=10, min_count=2, sg=1)
print(type(model))

model_filename = 'word2vec.model'

# 모델을 저장할 때는 save 함수를 사용합니다.
# 모델 파일은 바이트 형식의 파일입니다.
model.save(model_filename)
print(model_filename + ' 파일 생성됨')

print('finished')