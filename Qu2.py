#Python program to read two numbers and print their quotient and remainder.

divident = int(input("Enter Divident:"))
divisor = int(input("Enter Divisor:"))

remainder = 0
quotient = 0 

remainder = divident % divisor 
quotient = divident // divisor 
print("Remainder : ", remainder, "Quotient : ", quotient)