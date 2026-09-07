#Patterns
n=int(input("Enter the value of n here: "))
mystring =()
def double_pyramid1(n):
    for i in range(0,n):
        for k in range(0,n-i):
            print(" ",end='')
        for j in range(0,i+1):
            print("*",end=' ')
        print("")
def double_pyramid2(n):
    for i in reversed(range(0,n)):
            for k in range(0,n-i):
                print(" ",end='')
            for j in range(0,i+1):
                print("*",end=' ')
            print("")
def double_pyramid(n):   
    double_pyramid1(n)
    double_pyramid2(n)           


def butter_fly(n):
    for i in range(0,n):
        print('*'*(i+1),end='')
        print(' '*(2*(n-i-1)),end='')
        print('*'*(i+1))
    for i in range(n - 2,-1,-1):
        print('*'*(i+1),end='')
        print(' '*(2 *(n-i-1)), end='')
        print('*'*(i+1))



double_pyramid(n) 
butter_fly(n)
          

   