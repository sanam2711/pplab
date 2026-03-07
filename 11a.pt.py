import random
numbers = [random.randint(1, 100) for _ in range(20)]
print("Numbers:", numbers)
average = sum(numbers) / len(numbers)
print("Average:", average)
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)
second_largest = float('-inf')
second_smallest = float('inf')
for num in numbers:
    if num != largest and num > second_largest:
        second_largest = num
    if num != smallest and num < second_smallest:
        second_smallest = num
print("Second largest:", second_largest)
print("Second smallest:", second_smallest)
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("Even numbers count:", even_count)
