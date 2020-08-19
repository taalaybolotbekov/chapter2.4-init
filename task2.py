def count(func):
    def wrapper(*a, **b):
        print('Ваш Результат: ')
        func(*a, **b)
    return wrapper

@count
def plus(num1,num2):
  print(num1+num2)

@count
def minus(num1, num2):
  print(num1-num2)
        

plus(2, 1)
minus(2, 1)
