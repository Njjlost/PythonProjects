class Complex:
    def  __int__(self,r,i):
        self.real=r
        self.img=i


    def __add__(self,c):
        return complex(self.real+c.real,self.img+c.img)

    def __str__(self):
        return f"{self.real}+{self.img}"

    def __mul__(self,c):
        return complex([self.real*c.real-self.img*c.img],[self.real*c.img+self.img*c.real])


ComNum1=complex(3,4)     #Example
ComNum2=complex(5,6)

Op1=ComNum1+ComNum2
op2=ComNum1*ComNum2

print(Op1,"\n",op2)