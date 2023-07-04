import re
def main():
    answer=""
    while(answer != "exit"):
        answer = str(input("Please type a word or phrase to check if it's a palindrome:\n"))
        answer = re.sub('[^A-Za-z0-9]+', '', answer)
        answer = answer.lower()
        reversedAnswer = answer[::-1]
        if(reversedAnswer==answer):
            print("The provided input is a palindrome")
        else:
            print("The provided input is not a palindrome")
main()
