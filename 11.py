import random

 
numbers = []
for i in range(20):
    numbers.append(random.randint(1, 100))

 
print("Numbers:", numbers)

average=sum(numbers) / len(numbers)
print("Average:", average)
 
print("Largest:", max(numbers))
print("Smallest:", min(numbers))

 
numbers_sorted = sorted(numbers)
print("Second smallest:", numbers_sorted[1])
print("Second largest:", numbers_sorted[-2])
 
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("Even numbers count:", even_count)
