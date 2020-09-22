# mnistResult.py
test_acc = [0.9225, 0.9224, 0.9779, 0.9782, 0.9779]
test_loss= [0.2809, 0.2788, 0.0807, 0.0983, 0.0843]
comments = ['테스트01', '테스트02', '테스트03', '테스트04', '테스트05']

mycolor = ['b', 'g', 'r', 'c', 'b']

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
###############################################
plt.title('테스트 케이스별 정확도')
plt.xlabel('테스트 케이스')
plt.ylabel('정확도')
plt.bar(comments, test_acc, color=mycolor)

filename = 'mnist accuracy graph.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')
###############################################
plt.title('테스트 케이스별 비용 함수')
plt.xlabel('테스트 케이스')
plt.ylabel('비용 함수')
plt.bar(comments, test_loss, color=mycolor)

filename = 'mnist loss graph.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')

print('finished')