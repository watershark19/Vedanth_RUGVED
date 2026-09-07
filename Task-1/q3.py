#checking if a number is a hill number
mystring=str(input("Enter your number here: "))
n=len(mystring)
numbers=[]
value=1
i=0
for num in mystring:
    numbers.append(int((num)))
while i in range(0,n-1) and numbers[i]<numbers[i+1]:
    i=i+1
if i==0 or i==n-1:
    value=0
while i<n-1 and numbers[i]==numbers[i+1]:
    i=i+1
if i==n-1:
    value=0
while i<n-1 and numbers[i]>numbers[i+1]:
    i=i+1
if i!=n-1:
    value=0
if value==1:
    print("This is a valid hill number")
else:
    print("This is not a valid hill number")        

    