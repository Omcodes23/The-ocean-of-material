Amount = int(input("Please Enter Amount for Withdraw :"))

if Amount%5==0:
    print("Notes of 50,100,500,2000 required to fullfill the Amount :")
    print("****#****#****")
    print("notes of 50 : ",Amount/50)   
    print("notes of 100 :",Amount/100)
    print("notes of 500 : ",Amount/500)
    print("notes of 2000 : ",Amount/2000)
else:
    print("Notes of 100 and other required to fullfill the Amount : ")
    print("****#****#****")
    print ("Required notes of 100 is : ",(Amount/100))
    print ("Required notes of 50 is : " , (Amount%100)/50)
    print ("Required notes of 10 is : " , (((Amount%100)%50)/10))
    print ("Amount still remaining is : " , (((Amount%100)%50)%10))

