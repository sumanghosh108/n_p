# without using '+' operator, add two values
def plus(a,b):
    a1='0'*a
    b1='0'*b
    res=f'{a1}{b1}'
    return len(res)
print(plus(2,3))