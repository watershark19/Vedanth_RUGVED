#Program to divide a string into n equal parts
mystring=str(input("Enter the sentence here: "))
len_part=int(input("Enter the number of parts you want to divide it into here: "))
len_mystring=len(mystring)
n=len(mystring)/len_part
if len_mystring%n!=0:
    print(f"This sentence cannot be made into {n} equal parts")
else:
    for i in range(0,int(n)):
        print(mystring[i*len_part:i*len_part+len_part])



        
        