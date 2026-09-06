#credit card number being valid or not using luhn's algorithm
c=str(input("Enter your credit card number here: "))
mylist=list(c)
sum=0
for i in range(len(mylist)-2,-1,-2):    
    (mylist[i])=int(mylist[i])*2

    if int(mylist[i])>=10:
        (mylist[i])=int(mylist[i])-9
    else:
        continue
for i in range(0,len(mylist)):
    sum=sum+int(mylist[i])

if sum%10==0:
    print("This is a valid credit card number")
else:
    print("This is not a valid credit card number")    