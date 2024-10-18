class calc():
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
        
    def sum(self):
      return self.n1+self.n2 
    def sub(self):
        return self. n1-self.n2
    def div(self):
        return self. n1/self.n2
    def mul(self):
        return self. n1*self.n2
    
    def power(self):
        return self. n1**self.n2
c1= calc(6,7)
print(c1.sum())    