class Calculator:
     
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2
 
    def sum(self):
        return self.num1 + self.num2
 
    def mul(self):
        return self.num1 * self.num2
 
    def sub(self):
        return self.num1 - self.num2
 
    def div(self):
        return self.num1 / self.num2
    
def main():
    calc = Calculator(int(input("첫번째 수:"))
                      ,int(input("두번째 수:")))
    print("{} + {} = {}"
          .format(calc.num1
                  , calc.num2
                  , calc.sum()))
    print("{} - {} = {}"
          .format(calc.num1
                  , calc.num2
                  , calc.sub()))
    print("{} * {} = {}"
          .format(calc.num1
                  , calc.num2
                  , calc.mul()))
    print("{} / {} = {}"
          .format(calc.num1
                  , calc.num2
                  , calc.div()))
 
if __name__ == '__main__':
    main()