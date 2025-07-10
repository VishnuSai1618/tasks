class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b
res=Calculator(int(input("Enter the first number:")),int(input("Enter the second number:")))
res.addition()
print(res.subtraction())
print(res.multiplication())
try:
    print(res.division())
except ZeroDivisionError:
    print("Division by zero")