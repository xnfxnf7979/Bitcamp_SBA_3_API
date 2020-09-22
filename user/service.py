from user.entity import Entity
'''
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
'''

class Service:
    def __init__(self):
        self.entity = Entity()

    def new_model(self,payload):
        pass
    
    @staticmethod
    def create_train(this):
        pass
    
    @staticmethod
    def create_label(this):
        pass
    
    @staticmethod
    def drop_feature(this):
        pass