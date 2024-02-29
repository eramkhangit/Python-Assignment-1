# Python program to print odd numbers within a given range.

userRange = int(input("Enter number :"))
result = 0 

for num in range( 1 , userRange + 1 ) :
    if (num % 2 != 0 ):
        result = num + result 
print("Sum of odd numbers into range :", userRange , "is: ", result )    
