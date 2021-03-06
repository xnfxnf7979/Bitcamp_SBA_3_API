import sys
sys.path.insert(0, 'C:/SBAProject')
from titanic.entity import Entity
from titanic.service import Service
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
        return this

    def modeling(self, train, test):
        service = self.service
        this = self.preprocessing(train, test)
        print(f'훈련 컬럼 : {this.train.columns}')
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def learning(self):
        pass

    def submit(self):
        pass

if __name__ == '__main__':
    ctrl = Controller()
    ctrl.modeling('train.csv','test.csv')
    
'''
import sys
sys.path.insert(0, 'C:/SBAProject/')
from titanic.entity import Entity
from titanic.service import Service

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def preprocessing(self,train,test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train) # payload : train, test
        this.test = service.new_model(test) 
        return this

    def modeling(self,train,test):
        service = self.service
        this = self.preprocessing(train,test)
        print(f'훈련 칼럼: {this.train.columns}')
        this.lable = service.create_label(this)
        this.train = service.create_train(this)
        return this
    
    def learning(self):
        pass

    def submit(self):
        pass



if __name__ == '__main__':
    ctr1 = Controller()
    ctr1.modeling('train.csv','test.csv')
'''
