# program to print out fibonacci sequence
n = int(input("Enter n here: "))
fib=[0,1]
for i in range(2,n):
    next=fib[-1]+fib[-2]
    fib.append(next)

print(fib)