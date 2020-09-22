# word2vec_model_test.py
# 이전에 만들어 둔 모델 파일을 읽어 와서 특정 단어와 유사한 단어들을 찾아 봅니다.
# 인접한 유사도를 이용하여 데이터를 시각화 해 봅니다.
import matplotlib.pyplot as plt
from gensim.models import word2vec

plt.rc('font', family='Malgun Gothic')

def showGraph(bargraph):
    length = len(bargraph) # 요소 갯수
    # x축에 보이는 글자
    myticks = list(mydata[0] for mydata in bargraph)
    # 그려질 수치 데이터
    chartdata = list(mydata[1] for mydata in bargraph)
    mycolor = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#56FFCC', '#00CCFF', '#CCDDEE']

    plt.figure()
    plt.barh(myticks, chartdata, color=mycolor, align='center')
    plt.yticks(range(length), myticks, rotation='10')
    plt.xlim(min(chartdata) - 0.02, max(chartdata) + 0.02)
    filename = 'word2vec_model_01.png'
    plt.savefig(filename)
    print(filename + ' 파일 저장됨')

def makePie(piegraph):
    myticks = list(mydata[0] for mydata in piegraph)
    chartdata = list(mydata[1] for mydata in piegraph)
    mycolor = ['b', 'g', 'r', 'c', 'm']

    plt.figure()
    plt.pie(chartdata, colors=mycolor, labels=myticks, startangle=90, shadow=False,
            explode=(0, 0.05, 0, 0, 0), autopct='%1.2f%%', normalize=True)
    filename = 'word2vec_model_02.png'
    plt.savefig(filename)
    print(filename + ' 파일 저장됨')

model_file = 'word2vec.model'

model = word2vec.Word2Vec.load(model_file)
print(type(model))

# most_similar : positive에 명시된 단어에 대하여 유사도가 높은 항목을
# topn 개만 보여 주세요.
bargraph = model.most_similar(positive=['국민'], topn=10)
print(bargraph)

piegraph = model.most_similar(positive=['남북'], topn=5)
print(piegraph)

showGraph(bargraph)

makePie(piegraph)

print('finished')