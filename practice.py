# WAP to take int input from a student and print his/her grades 
studentNumber = int(input("please enter your number: "))

if (studentNumber >= 80 and studentNumber <=100): 
    print("Congratulations, You have got A+")
elif (studentNumber >= 60 and studentNumber <= 79): 
    print("Congratulations, You have got A")
elif (studentNumber >=40 and studentNumber <= 59): 
    print("Congratulations, You have got B")
else: 
    print("Unfortunately, you have failed")

# WAP to where two floating point numbers are input and print their average

firstNumber = float(input("Please enter first number: "))
secondNumber = float(input("Please enter second number: "))
averageNumber = (firstNumber + secondNumber) / 2
print("Average of the two floating point numbers is: ", averageNumber)


# WAP to take input of two numbers and print true if a >= b otherwise print false

firstNumber = int(input("Please enter first number: "))
secondNumber = int(input("Please enter second number: "))

if (firstNumber >= secondNumber): 
    print(True)
else: 
        print(False)

