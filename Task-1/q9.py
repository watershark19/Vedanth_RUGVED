#Caeser's cipher
def ceaser_funct(mysentence,shift):
    mystring=mysentence.lower()
    asc=list()
    enc=list()
    for char in mystring:
        asc.append(ord(char))
    print(asc)    
    for i in range(0,len(asc)):
        asc[i]=asc[i]-97
    print(asc)
    #we have now converted from to 0-25 form and we have to add the shift
    for i in range(0,len(asc)):
        asc[i]=(asc[i]+shift)%26
    print(asc)    
    #now the range is greater than 25 so modulo math    
    #now we add 97 to get the final list of assci
    for i in range(0,len(asc)):
        asc[i]=asc[i]+97
    print(asc)   
    for i in asc:
        enc.append(chr(i))
    print(enc)  
    cytxt="".join(x for x in enc) 
    return cytxt   


print(ceaser_funct("abcz",3))