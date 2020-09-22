# advertisementEx.py
# 회귀 분석 : 광고 지출비에 따른 광고 수익(단순 회귀 분석)
'''
광고 지출비와 광고 수익에 따른 산점도/선 그래프
해당 데이터들이 선형적이라고 가정하고, 가장 이상적인 직선의 방정식을 구하도록 합니다.
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

x = np.array([1, 2, 3, 4]) # 광고 지출비(독립 변수)
y = np.array([30, 70, 90, 115]) # 광고 수익(종속 변수)

plt.figure() # 새 도화지 준비
plt.title('라인이 있는 산점도 그래프')
plt.xlabel('광고 지출비')
plt.ylabel('광고 수익')
plt.ylim([20, 120])
plt.plot(x, y, color='blue', linestyle='solid', marker='o', label='real data')

filename = 'imageTest01.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')
print('finished')

# 최적의 w와 b를 구합니다.
mx = np.mean(x)
my = np.mean(y)
print('x 평균 :', mx)
print('y 평균 :', my)

bunmo = sum([(mx-val)**2 for val in x])

def calc(x, mx, y, my):
    result = 0
    for i in range(len(x)):
        result += (x[i]-mx)*(y[i]-my)
    return result

bunja = calc(x, mx, y, my)

print('분모 :', bunmo)
print('분모 :', bunja)

w = bunja/bunmo
b = my - (mx*w)

print('기울기 w : ', w)
print('y절편 b : ', b)

def prediction(x):
    return w * x + b

pred_y = prediction(x)
plt.title('회귀선과 실제 데이터')
plt.plot(x, pred_y, color='red', linestyle='solid', marker='o', label='best line')

# 실제 데이터(정답_label)와 예측 데이터의 차이를 수직선으로 표현
for idx in range(len(x)):
    xdata = []
    ydata = []

    xdata.append(x[idx])
    ydata.append(y[idx])

    xdata.append(x[idx])
    ydata.append(pred_y[idx])

    plt.plot(xdata, ydata, marker='', color='g', linestyle='solid')


plt.legend(loc='best')
filename = 'imageTest02.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')

# 가장 이상적인 w와 b는 다음과 같다.
# 기울기 w :  27.5
# y절편 b :  7.5

# w를 모른다는 가정하에 w = 25, 27.5, 30, 35라는 값을 이용하여
# 각각의 비용 함수가 얼마가 되는 지 살펴 보도록 하겠습니다.
def myfunction(w, x, b=7.5):
    return w*x+b

b=10
slope1, slope2, slope3 = 25, 30, 35

best=myfunction(w, x)
answer1 = myfunction(slope1, x, b)
answer2 = myfunction(slope2, x, b)
answer3 = myfunction(slope3, x, b)

rmse0 = np.sum((best-y)**2)
rmse1 = np.sum((answer1-y)**2)
rmse2 = np.sum((answer2-y)**2)
rmse3 = np.sum((answer3-y)**2)

plt.figure()

mylabel = 'best slope :' + str(w) + ', rmse : ' + str(rmse0)
plt.plot(x, best, marker='o', color='y', linestyle='None', label=mylabel)

mylabel = 'slope1 :' + str(slope1) + ', rmse : ' + str(rmse1)
plt.plot(x, answer1, marker='o', color='r', linestyle='solid', label=mylabel)

mylabel = 'slope2 :' + str(slope2) + ', rmse : ' + str(rmse2)
plt.plot(x, answer2, marker='o', color='g', linestyle='solid', label=mylabel)

mylabel = 'slope3 :' + str(slope3) + ', rmse : ' + str(rmse3)
plt.plot(x, answer3, marker='o', color='b', linestyle='solid', label=mylabel)

plt.title('기울기별 시각화')
plt.legend(loc='best')
plt.ylim(20, 160)
filename = 'imageTest03.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')

# 위의 그래프를 보면 이상적인 w에서 비용 함수의 값이 최소가 됩니다.
# 이 w의 값이 27.5보다 작아지거나 커지면 비용 함수의 값은 커집니다.
# 이것을 그래프로 그려 보겠습니다.

# w를 20이상 35이하의 범위에서 w에 따른 비용 함수를 시각화 해 봅니다.
cost = [] # 비용 함수 리스트

for idx in range(2000, 3501, 1):
    res01 = myfunction(0.01*idx, x)
    res02 = np.sum((res01-y)**2)
    cost.append((0.01*idx, res02))

print(cost)

# 결론 : x축에 w를 그리고, y축에 비용 함수의 결과 그래프를 확인해보면 이차 함수라는 것은 확인할 수 있습니다.
xdata = [data[0] for data in cost]
ydata = [data[1] for data in cost]

plt.figure()
plt.plot(xdata, ydata, 'b-')
plt.plot(w, min(ydata), 'bo') # 극소점

plt.title('w에 따른 cost의 변화')
filename = 'imageTest04.png'
plt.savefig(filename)
print(filename + ' 파일 저장됨')

'''
선형 회귀 분석 : 종속 변수 1개와 한 개이상의 독립 변수간의 인과 관계를 선형적으로 분석하는 기법
독립 변수의 개수에 따라서
    단순 회귀 분석 : H = w*x + b
    다중 회귀 분석 : H = w1*x1 + w2*x2 + ... + b
    
가설 공식 = 회귀 방정식 = y = H = w*x + b    
회귀선 : 회귀 방정식에 의하여 그려진 선 그래프     
머신 러닝에서 w를 가중치(기울기)라고 하고, b를 bias라고 부릅니다.
회귀 계수 : w와 b

비용 함수(cost function): 회귀 분석의 성능 지표
    총누적((예측값-실제값)**2)
    가장 이상적인 데이터는 0에 가깝다.
    
최소 자승법
비용 함수를 구할 때 제곱을 해서 풀어나가므로 이를 최소 제곱법 또는 최소 자승법이라고 합니다.    
'''
