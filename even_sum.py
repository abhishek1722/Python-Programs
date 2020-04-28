# Program to find the sum of 1st n even numbers

Number = int(input("Maximum limit :"))

Sum = 0

Num = 1

while Num <= Number: 
    if Num % 2 == 0:
        Sum = Sum + Num 
         
    Num = Num + 1  

print("Sum of 1st N even numbers",Sum)
        
        
    
