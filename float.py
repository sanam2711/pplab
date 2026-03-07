a=float(input("enter no:"))
b=float(input("enter no:"))
c=abs(a-b);
print(c)
if c<0.001:
    print("close")
else:
    print("not close")
