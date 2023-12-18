def checkPrime(num):
    flag=False
    if num==1:
        print(num,"is not a Prime number")
    for i in range(2,num+1):
        if num%i==0:
            flag=True
            break
        else:
            flag=False
    
    if flag==True:
        print(num, "is not a Prime number")
    else:
        print(num, " is a Prime number")






number= int(input("Enter the number: "))
checkPrime(number)