# onehot_encoding_per_word.py
# 신경망(Neural Net)은 크게 2가지로 나누어 집니다.
# CNN(Convolution NN) : 이미지 처리
# RNN(Recurrent NN) : 순환 신경망, 시계열 데이터(주식 시세, 집값)
# 자연어 처리 :

# 문자열을 숫자화 : 단어 수준의 원핫인코딩
sentences = ['tensorflow makes machine learning easy', 'machine learning is easy']

# 단어 사전(BOW : bag of words)
word_dict = {}

for onedata in sentences :
    for word in onedata.split():
        if word not in word_dict:
            # 번호 0은 내부 처리용으로 사용되므로 1부터 시작한다.
            word_dict[word] = len(word_dict) + 1

print(len(word_dict))
print('-'*30)

print(word_dict)
print('-'*30)

max_length = 10

sentences_length = len(sentences)
dict_size = max(word_dict.values()) + 1 # 사전의 크기

import numpy as np

results = np.zeros((sentences_length, max_length, dict_size))
print(results.shape)
print(results)
print('-'*30)

for ii, sample in enumerate(sentences):
    for kk, word in list(enumerate(sample.split())):
        index = word_dict.get(word)
        results[ii, kk, index] = 1.
    print('#'*30)

print(results)
print('-'*30)
