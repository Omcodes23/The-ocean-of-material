num1=float(input("Enter First Number : "))
num2=float(input("Enter Second number : "))
num3=float(input("Enter Third Number : "))
if(num1>num2)and(num1>num3):
    print("{} is largest".format(num1))
elif(num2>num1)and(num2>num3):
    print("{} is largest".format(num2))
else:
    print("{} is largest".format(num3))
