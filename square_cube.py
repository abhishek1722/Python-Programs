# Program to find the square and cube of n numbers

Number = int(input("Enter the number :"))

Num  = 1

while Num <= Number:
    square = Num * Num
    cube = Num * Num * Num
    print("Square of",Num,"is",square, "and Cube is",cube)
    Num = Num + 1
    
