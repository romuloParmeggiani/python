import math
#This is a program to check if the given number is either a prime number or not
#Therefore it should be positive integer greater than 1 and has not more factors other than 1 and itself
#Numbers with more factors are called 'composite numbers'
def isPrimeNumber(n):
    try:
        number = int(n)
        if number > 1:
            #Checks from the range to 2 till the squareroot of the given number (i):+1 to include it within range
            #Same results would be achieved with 'range(2, number)', although with less performance
            for factor in range(2, int(number**0.5+1)):
                if number % factor == 0:
                    print(f'{number} is not a prime number')
                    print(f'For {factor} times {number//factor} is {number}')
                    break
            else:
                print(f'{number} is a prime number!')
        else:
            print(f'{number} is not a prime number for it is less then or equal to 1')
    except ValueError:
        print(f'Value Error: The inputed value \'{n}\' is not a number...')

#Loop to display the result of the prime check for all number under the given range
# for n in range(2,100):
#     isPrimeNumber(n)

#Prompts the user for an input of an integer number to check if its a prime number
#The given input will be casted into an integer to properly handle it as inputs are received as strings
number = input("Please type an integer number to check if its a prime or not:\n")
isPrimeNumber(number)