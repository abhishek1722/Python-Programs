# Program to find the factorial of a number

Number = int(input("Enter the Number you want to find the factorial of :"))

N = 1

while Number > 1:

    N = Number * N
    Number = Number - 1 

print("Factorial is",N)

    
