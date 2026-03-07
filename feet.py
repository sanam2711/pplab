a=["inches", "yards", "miles", "millimetres", "centi meters","meters","kilo meters"]
b=[12,1/3,1/5280,304.8,30.48,0.3048,0.0003048]

n=int(input("enter a number: "))
r=int(input("enter a value \n1.inches\n2.yards\n3.miles\n4.millimetres\n5.centi meters\n6.meters\n7.kilo meters\n"))

print("feet :",n*b[r-1])
