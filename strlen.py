str1=input("enter str1: ")
str2=input("enter str2: ")
c=""
if len(str1)==len(str2):
     print("both lengths are same: " )
     for i in range (len(str2)):
         c=c+str1[i]+str2[i]
else:
    print("not same length: ")
print(c)    

