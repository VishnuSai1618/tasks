def divide(a,b):
    return a/b
a,b=map(int,input("Enter two numbers to divide: ").split())
try:
    print(divide(a,b))
except ZeroDivisionError:
    print("Division by zero")