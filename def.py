n=int(input("enter a value :"));
sum=0
while n>0:
    digit=n%10;
    sum+=digit
    n=n//10
print("sum of digits :",sum);

