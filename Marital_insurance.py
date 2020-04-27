Marital_status = input("Marital Status :")
Gender = input("Enter your Gender(M/F):")                       
Age = int(input("Enter the Age in years "))    
                
if Marital_status == 'Married':
    print("Married one Insured")
    
elif Marital_status == 'unmarried' and Gender == 'M' and  Age == 25 :
    print("Unmarried Male is Insured")
          
elif Marital_status == 'unmarried' and Age == 35 and Gender == 'F':
    print("Unmarried Female is Insured") 
    
else:
    print("No one is insured")
