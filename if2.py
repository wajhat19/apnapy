
num1=int(input("enter the first numn: ")) 
num2=int(input("enter the se numn: ")) 
num3=int(input("enter the third numn: ")) 
num4=int(input("enter the fourth num: "))

if(num1>=num2 and num1>=num3 and num1>num4):
    print("num1 is greater:",num1)
elif(num2>=num3 and num2>=num4):
    print("num2 is greater:",num2)
elif(num3>=num4):
    print("num3 is greater:",num3)    
else:
    print("num4 is the greater:",num4)    