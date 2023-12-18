def checkPrime(num):
    flag=False
    for i in range(1,num+1):
        if num%i==0:
            flag=False
        else:
            flag=True
    if flag==True:
        print(num + "is a Prime number")
    else:
        print(num +" is not a Prime number")







number= int("Enter the number: ")
checkPrime(number)