number1 = int(input("Enter number1:"))
number2 = int(input("Enter number2:"))
number3 = int(input("Enter number3:"))

if number1 > number2 and number1 > number3:
    print("number1 is the greatest")
elif number2 > number1 and number2 > number3:
    print("number2 is the greatest")
elif number3 > number1 and number3 > number2:
    print("number3 is the greatest")

if number1 < number2 and number1 < number3:
    print("number1 is the smallest")
elif number2 < number1 and number2 < number3:
    print("number2 is the smallest")
elif number3 < number1 and number3 < number2:
    print("number3 is the smallest")

biggestNumber = number1
smallestNumber = number1
numList = [number1, number2, number3]
for num in range(0, len(numList)):
    if numList[num] > biggestNumber:
        biggestNumber = numList[num]
    if numList[num] < smallestNumber:
        smallestNumber = numList[num]
print(f"{biggestNumber} is the biggest")
print(f"{smallestNumber} is the smallest")