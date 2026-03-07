import random;
a=random.randrange(1,10);
guess=0
while guess!=a:
  guess=int(input("enter a guess:"));
if guess==a:
    print("well guessed")
else:
    print("next time")
    
    
