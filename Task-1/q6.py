#program to check whether two numbers are anagrams of each other
str_1=str(input("Enter your first word here: "))
str_2=str(input("Enter your second word here: "))
list1=list(str_1.lower())
list2=list(str_2.lower())
if len(list1)!=len(list2):
    print("They are not anagrams of each other")
else:
    if list1.sort()==list2.sort():
        print("They are anagrams of each other")