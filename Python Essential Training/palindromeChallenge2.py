def isPalindrome(testStr):
    #Using the Slice to trick reverse the string
    if testStr == testStr[::-1]:
        return True
    return False
run = True
while(run):
    testStr = input("Type a string to test if it's a palindrome or 'exit' to close:\n")
    if testStr == "exit":
        print("Exiting execution...")
        run = False
        break
    else:
        newStr = ""
        testStr = testStr.lower()
        for x in testStr:
            if x.isalnum():
                newStr += x
        print("Palindrome test:",isPalindrome(newStr))