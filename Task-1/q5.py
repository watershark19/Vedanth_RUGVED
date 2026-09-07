#fibonacci using recursion 
def fibo_funct(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo_funct(n-2) + fibo_funct(n-1)
print(fibo_funct(9))    