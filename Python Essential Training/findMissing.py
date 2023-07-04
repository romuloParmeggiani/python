numbersDictionary = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5" }
numbersToSearch = ["2","3","1","0","5"]
def findMissing(numbersToSearch):
    #Range of numbers should be from 0 to 5.
    #Script should receive as argument an array containing the numbers to search in dictionary.
    #Script should then scan dictionary and print the number remaining in it.
    for number in numbersToSearch:
        print(f"Searching for number {number}...")
        if(numbersDictionary[number]):
            print(f"Number {number} found, removing it from dictionary...")
            del numbersDictionary[number]
            print(f"Number {number} was removed from dictionary...")
            print(f"Current numbers in dictionary: {list(numbersDictionary)}")
        else:
            print(f"Number {number} was not found, something went wrong...")
    missingNumber = numbersDictionary.values()
    print(f"The only number missing from the provided input is {missingNumber}")
findMissing(numbersToSearch)