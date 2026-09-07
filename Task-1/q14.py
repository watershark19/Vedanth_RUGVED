#finding the index of first repeated number
arr=[]
n= int(input("Enter the number of numbers in the array here: "))
for i in range(0,n):
    arr.append((int(input("Enter the numbers here: "))))
print("This is the array : ",arr)



def repeated_number(arr):

    for i in range(0,len(arr)):
        for j in range(i+1,n):
            if arr[j]==arr[i]:
                return i

print("The repeated number is first at index",repeated_number(arr))