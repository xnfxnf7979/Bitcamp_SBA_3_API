<<<<<<< HEAD
import sys
sys.path.insert(0, 'C:/SBAProject')
from titanic.entity import Entity
from titanic.service import Service

"""
####### PassengerId  고객ID,
####### Survived 생존여부,  --> 머신러닝 모델이 맞춰야 할 답 
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
####### Ticket 티켓번호,
Fare 요금,
####### Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
"""

class Controller:
    def __init__(self):
        print('TEST')
        self.entity = Entity()
        self.service = Service()

    def preprocessing(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train) # payload
        this.test = service.new_model(test) # payload
        this.id = this.test['PassengerId']  # 이게 머신의 문제(Question)가 됨
        print(f'드롭 전 변수: {this.train.columns}')
        this = service.drop_feature(this,'Cabin')
        this = service.drop_feature(this,'Ticket')
        print(f'드롭 후 변수: {this.train.columns}')
        this = service.embarked_nominal(this)
        print(f'================================승선한 항구 정제 결과========================')
        print(f'{this.train.head()}')
        this = service.title_nominal(this)
        print(f'================================타이틀 정제 결과============================')
        print(f'{this.train.head()}')
        # name 변수에서 title을 추출했으니 name 은 필요가 없어졌고, str 이니
        # 후에 ML 라이브러리가 이를 인식하는 과정에서 에러를 발생시킬 것이다
        # -> name 을 삭제해야 한다
        this = service.drop_feature(this, 'Name')
        this = service.drop_feature(this, 'PassengerId')
        this = service.age_ordinal(this)
        print(f'================================나이 정제 결과==============================') 
        print(f'{this.train.head()}')
        this = service.sex_nominal(this)
        print(f'================================성별 정제 결과==============================')
        print(f'{this.train.head()}')
        this = service.fareBand_nominal(this)
        print(f'================================요금 정제 결과==============================')
        print(f'{this.train.head()}')
        this = service.drop_feature(this, 'Fare')
        print(f'==============================전체 정제 결과================================ ')
        print(f'{this.train.head()}')
        print(f'==============================train na 체크================================:')
        print(f'{this.train.isnull().sum()}')
        print(f'==============================test na 결과================================= ')
        print(f'{this.train.isnull().sum()}')
        
        return this

    def modeling(self, train, test):
        service = self.service
        this = self.preprocessing(train, test)
        #print(f'훈련 컬럼 : {this.train.columns}')
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def learning(self, train, test):
        service = self.service
        this = self.modeling(train, test)
        print('######################### Learning 결과######################################')
        print(f'결정트리 검증결과: {service.accuracy_by_dtree(this)}')
        print(f'랜덤포리 검증결과: {service.accuracy_by_rforest(this)}')
        print(f'나이브베이즈 검증결과: {service.accuracy_by_nb(this)}')
        print(f'KNN 검증결과: {service.accuracy_by_knn(this)}')
        print(f'SVM 검증결과: {service.accuracy_by_svm(this)}')

    def submit(self):   # 머신이 된다. 이 단계는 케글에게 내 머신을 보내 평가받게 하는 것임
        pass

if __name__ == '__main__':
    ctrl = Controller()
    ctrl.learning('train.csv','test.csv')

=======
from user.entity import Entity
from user.service import Service

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def preprocessing(self):
        pass

    def modeling(self):
        pass
    
    def learning(self):
        pass

    def submit(self):
        pass
>>>>>>> 7d435d24cc64448c886109f024644393c1562b8c
