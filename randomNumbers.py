import random
from typing import Set

# numbers = []
# for i in range(6):
#     randomNumber = random.randint(1,61)
#     numbers.append(randomNumber)
# print(numbers)

newNumbers = set()
while (len(newNumbers) < 6):
    randomNumber = random.randint(1,60)
    newNumbers.add(randomNumber)
print(sorted(newNumbers))