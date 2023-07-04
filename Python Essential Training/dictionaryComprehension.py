animalsList = [('a', 'alien'),('b', 'bowser'),('c', 'cat'), ('d', 'dog')]
# print(animalsList)
# animalsDict = {animal[0]: animal[1] for animal in animalsList}
# print(animalsDict)

animals = {key: value for key, value in animalsList}
print('Printing animals...\n', animals)
print('Printing animals.items...\n', animals.items())
# print(animals.items())
# print(list(animals.items()))
# print(animals['a']
animals2 = list(animals.items())
print('Printing animals2...\n', animals2)
animals3 = [{'letter': key, 'name': value} for key, value in animals.items()]
print('Printing animals3...\n', animals3)