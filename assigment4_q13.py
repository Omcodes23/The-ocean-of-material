ph=int(input("Enter the marks of Physics : "))
ch=int(input("Enter the marka of Chemistery : "))
bi=int(input("Enter the marks of Biology : "))
ma=int(input("Enter the marks of Mathematics : "))
co=int(input("Enter the marks of Computer : "))
total=ph+ch+bi+ma+co
per=((total/500)*100)
if per>=90 :
    print(" {} is your Percentage and \nyou have Grade A".format(per))
elif per>=80 :
    print("{} is your Percentage and \nyou have Grade B".format(per))
elif per>=70 :
    print("{} is your Percentage and \nyou have Grade C".format(per))
elif per>=60 :
    print("{} is your Percentage and \nyou have Grade D".format(per))
elif per>=40 :
    print("{} is your Percentage and \nyou have Grade E".format(per))
else :
    print("{} is your Percentage and \nyou have Grade F".format(per))