def func1():
    print("I'm an example of a function")
def cube(x):
    return x * x * x
def power(num, x=1):
    result=1
    for i in range(x):
        result=result*num
    return result
def multiAdd(*args):
    result=0
    for x in args:
        result=result+x
    return result

#func1()
#print(func1())
#print(func1)
#print(cube(3))
#print(power(2))
#print(power(2, 3))
#print(power(x=3, num=2))
print(multiAdd(4,5,10,4,10))