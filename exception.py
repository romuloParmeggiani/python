try:
    print("Please provide me two numbers to be divided:")
    x, y = map(int, input().split())
    print(x/y)
except ZeroDivisionError as e:
    print("You've asked me to divide by 0, which is not supported, please try again with a different number...")
except ValueError as e:
    print("You've provided me a value that's not a number, please try again with a number instead...")
    print(e)
finally:
    print("Have a nice day!")