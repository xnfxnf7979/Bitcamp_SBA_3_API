# tojiFrequency.py
# 참조 파일 : tojiText.txt, stopword.txt, alice_color.png
# 토지 파일을 읽어 들여서 워드 클라우드와 막대 그래프 그리기
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image # pillow 설치 요망
from wordcloud import WordCloud # 참고 : pytagcloud
from wordcloud import ImageColorGenerator

plt.rc('font', family='Malgun Gothic')

class Visualization:
    def __init__(self, wordlist):
        self.wordlist = wordlist
        print('워드 리스트')
        print(wordlist)
        self.wordDict = dict(self.wordlist)

    def makeWorCloud(self): #워드 클라우드
        alice_color_file = 'alice_color.png'
        # 이미지를 넘파이 배열로 바꿉니다.
        alice_coloring = np.array(Image.open(alice_color_file))
        fontpath = 'malgun.ttf'
        wordcloud = WordCloud(font_path=fontpath, mask=alice_coloring,
                              relative_scaling = 0.2,background_color='lightyellow')
        wordcloud = wordcloud.generate_from_frequencies(self.wordDict)

        image_colors = ImageColorGenerator(alice_coloring)
        # random_state : 랜덤 상수 지정
        newwc = wordcloud.recolor(color_func=image_colors, random_state=42)

        plt.imshow(newwc)
        plt.axis('off')

        filename = 'tojiWordCloud.png'
        plt.savefig(filename)
        plt.figure(figsize=(16,8))

    def makeBarChart(self): # 막대 그래프
        # result를 이용하여 막대 그래프를 그려 보세요.
        result = self.wordlist[0:10] # 10개 데이터

        barcount = 10  # 막대 갯수 : 10개만 그리겠다.
        xlow, xhigh = - 0.5, barcount - 0.5

        result = self.wordlist[:barcount]
        chartdata = []  # 차트 수치
        xdata = []  # 글씨
        mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#FFF0F0', '#CCFFBB', '#05CCFF', '#11CCFF']

        for idx in range(len(result)):
            chartdata.append(result[idx][1])
            xdata.append(result[idx][0])

            value = str(chartdata[idx]) + '건'  # 예시 : 60건
            # 그래프의 위에 "건수" 표시
            plt.text(x=idx, y=chartdata[idx] - 20, s=value, fontsize=8, horizontalalignment='center')

        plt.xticks(range(barcount), xdata, rotation=45)
        plt.bar(range(barcount), chartdata, align='center', color=mycolor)

        plt.title('상위 ' + str(barcount) + '빈도수')
        plt.xlim([xlow, xhigh])
        plt.xlabel('주요 키워드')
        plt.ylabel('빈도수')

        filename = 'tojiBarChart.png'
        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' 파일이 저장되었습니다.')

filename = 'tojiText.txt'
ko_con_text = open(filename, 'rt', encoding='utf-8').read()

from konlpy.tag import Okt

okt = Okt()
token_ko = okt.nouns(ko_con_text)

# 불용어(stopword) : 빈도 수에 상관없이 분석에서 배제할 단어들
stop_word_file = 'stopword.txt'
stop_file = open(stop_word_file, 'rt', encoding='utf-8')
stop_words = [ word.strip() for word in stop_file.readlines()]
# print(stop_words)

token_ko = [each_word for each_word in token_ko if each_word not in stop_words]

# nltk : national language toolkit
# token : 작은 절편
import nltk
ko = nltk.Text(tokens=token_ko)

wordlist = list() # 튜플(단어, 빈도수)를 저장할 리스트
# 가장 빈도수가 많은 500개만 추출
data = ko.vocab().most_common(500)
# print(data)
for word, count in data :
    if (count >= 50 and len(word) >= 2):
        wordlist.append((word, count))

visual = Visualization(wordlist)
visual.makeWorCloud()
visual.makeBarChart()

print('finished')