#Program to check the number of occurences of each letter in a string
s = str(input("Enter your string here: "))
arr = list(s)
arr.sort()
mydict={}
for char in arr:
    if char not in  mydict.keys():
        mydict[char]=1
    else:
        mydict[char]+=1    
print(mydict)










