from datetime import date, datetime
def task1_1():
    x =int(input("X: "))
    y = int(input("Y: "))
    z = int(input("Z: "))

    if x >= 0 or y >= 0 or z >= 0:
        print("true")
    else:
        print("false")

def task1_2():
    x =int(input("X: "))
    y = int(input("Y: "))
    z = int(input("Z: "))

    if x == y == z:
        print("true")
    else:
        print("false")

def task1_3():
    x =int(input("X: "))
    y = int(input("Y: "))
    z = int(input("Z: "))

    if x != y != z:
        print("true")
    else:
        print("false")

def task2_1():
    firstNumber = float(input("First number: "))
    secondNumber = float(input("Second number: "))

    if firstNumber == secondNumber:
        return print("First number and second numbers is equals")
    biggerNumber = "first number" if firstNumber > secondNumber else "second number"

    print(f"The {biggerNumber} is bigger")

def task2_2():
    number = input("Input a two-digit number:")
    firstDigit = int(number[:1])
    secondDigit = int(number[1:2])

    biggerDigit = "first digit" if firstDigit > secondDigit else "second digit"

    print(f"The {biggerDigit} is bigger")

def task2_3():
    number = input("Input a two-digit number:")
    firstDigit = int(number[:1])
    secondDigit = int(number[1:2])

    isEquals = "equals" if firstDigit > secondDigit else "not equals"

    print(f"The sumbers are {isEquals}")

def task4():
    
    day = int(input("Enter a day: "))
    month = int(input("Enter a month: "))
    year = int(input("Enter a year: "))

    userDate = datetime(year,month,day,0)

    print(f"Youre date: {userDate}")
    userDateTimestamp = userDate.timestamp()
    startYearDateTimestamp = datetime(year,1,1,0).timestamp()

    pastDays = (((userDateTimestamp - startYearDateTimestamp) / 60)/60)/24
    print(f"Past days: {pastDays}")


print("Availabled task number: 1_1,1_2,1_3; 2_1,2_2,2_3; 4")
functions = {"1_1": task1_1, "1_2":task1_2, "1_3": task1_3, "2_1": task2_1, "2_2":task2_2, "2_3":task2_3, "4": task4}
functions[ input("Input task number for result output:")]()