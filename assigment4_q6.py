a=float(input("Enter First Side : "))
b=float(input("Enter Second Side : "))
c=float(input("Enter Third Side : "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**(0.5)
print("The area of the triangle is",format(area,'.2f'))
