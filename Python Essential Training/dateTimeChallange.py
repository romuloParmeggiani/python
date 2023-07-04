import calendar
import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def countWeekDaysOccur(year, month, day):
    dayCount = 0
    weekList = calendar.monthcalendar(year, month)
    for week in weekList:
        if week[day] != 0:
            dayCount += 1
    return dayCount

def main():
    execute = True
    while(execute != False):
        try:
            cls()
            print("Type the number for the day of the week that you'd like to count:")
            print("0: Monday")
            print("1: Tuesday")
            print("2: Wednesday")
            print("3: Thursday")
            print("4: Friday")
            print("5: Saturday")
            print("6: Sunday")
            print("Or 'exit to quit")
            answer = input()
            if answer.lower() == "exit":
                cls()
                print("Exiting execution...")
                time.sleep(3)
                execute = False
                break
            day = int(answer)
            cls()
            year = int(input("Type the year of your choice:\n"))
            cls()
            month = int(input("Type the month of your choice:\n"))
            occurrence = countWeekDaysOccur(year, month, day)
            cls()
            print("The chosen day has", occurrence, " occurreces within the chosen month of the chosen year")
            time.sleep(5)
        except Exception as e:
            cls()
            print(e)
            print("It seems you've entered an invalid input, please try again...")
            time.sleep(3)

if __name__ == "__main__":
    main()