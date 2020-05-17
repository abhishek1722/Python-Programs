'''
The highest common factor (H.C.F) or greatest 
common divisor (G.C.D) of two numbers is the largest 
positive integer that perfectly divides the two given
numbers. 

For example, the H.C.F of 12 and 14 is 2.
'''

#program to find HCF of two numbers 
print("Enter two numbers :")
num1=int(input("Enter first number :"))
num2=int(input("Enter Second number :"))
if num1>num2:
    smaller=num2
else:
    smaller=num1
    for i in range(1,smaller+1):
        if ((num1%i==0)and(num2%i==0)):
            hcf=i
print("HCF of ",num1," and ",num2," is ",hcf)


'''
output:
Enter two numbers :
Enter first number :22
Enter Second number :36
HCF of of 12 and 14 is 2.
'''









