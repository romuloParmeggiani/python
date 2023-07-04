import random
from unittest import case

luckyNumber = random.randint(1,100)
fortuneNumber = random.randint(1,3)

fortuneText = ""

if fortuneNumber == 1:
    fortuneText = "You'll have a great day!"
elif fortuneNumber == 2:
    fortuneText = "Today is going to be tough... but in the end you'll be rewarded!"
elif fortuneNumber == 3:
    fortuneText = "You're in danger, watch yourself today!"

print(f"{fortuneText} Your lucky number is: {luckyNumber}")