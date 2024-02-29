# Python program to find simple intrest .

initialPrincipalBalance = int(input("Enter initial principal balance : "))
rate = int(input("Enter annual interest rate : "))
time = int(input("Enter time in year : "))

print("Final Amount is : ", initialPrincipalBalance * ((1+ (rate * time ) ))  )