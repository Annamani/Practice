def checkFactorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*checkFactorial(num-1)


number=int(input("Enter the number: "))
factorial=checkFactorial(number)
print("Factorial of given number is :",factorial)