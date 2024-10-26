### Part Four -- your code goes here. 
import random


numbers = [random.randint(1, 100)for i in range(10)]
print("list:", numbers)


i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0: 
        numbers.pop(i)
    else:
        i += 1 

print("Remaining odd numbers:", numbers)
