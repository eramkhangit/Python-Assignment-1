# Python program to reverse three digits number without using loop.

userInput = input("Enter three digit number: ")
print("Reversed numbers : ", int(userInput[:: -1 ]))