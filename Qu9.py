# Python program to exchange the value of two numbers without using a temporary variable.

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

temporaryVariable = 0

temporaryVariable = num1
num1  = num2
num2 = temporaryVariable

print("Exchanged Variables - ", "num1 : ",  num1 ,"num2 : " ,num2 )