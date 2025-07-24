import random
import time
print("Starting Number Adder")
startingNumber = ""
endingNumber = ""
interval = 0
isValid = False
while isValid != True:
    startingNumber = input("what number do you want to start at?\n")
    if startingNumber.isnumeric():
        isValid = True
    else:
        print("not a numeric number")
isValid = False
startingNumber = int(startingNumber)
while isValid != True:
    endingNumber = input("What number do you want to end at?\n")
    if endingNumber.isnumeric():
        isValid = True
    else:
        print("not a numeric number")
isValid = False
endingNumber = int(endingNumber)
while isValid != True:
    interval = input("what do you want the chance to be for the number to increase?(every second, 1/n chance)\n")
    if interval.isnumeric():
        isValid = True
    else:
        print("not a numeric number")
isValid = False
interval = int(interval)

while isValid != True:
    numberIncrease = input("How much do you want the number to jump by when the chance succeeds?\n")
    if numberIncrease.isnumeric():
        isValid = True
    else:
        print("not a numeric number")
isValid = False
numberIncrease = int(numberIncrease)

currentNumber = startingNumber
currentTime = time.time()

randomNumber = 0
while True:
    time.sleep(1)

    randomNumber = random.randint(1,interval)

    if randomNumber == 1:
        currentNumber += numberIncrease
        print(f"number is now {currentNumber}")
        if currentNumber >= endingNumber:
            print("current number is now greater than or equal to end number")
            break
    else:
        print(randomNumber)
print(f"It took {round(time.time() - currentTime)} seconds to complete this")
number1 = endingNumber - startingNumber
number2 = number1/numberIncrease
number3 = number2*interval
print(f"it would have taken a median of {number3} seconds to reach the number!")
