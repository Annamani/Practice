num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

sum = num1 + num2 + num3
  
if num1 == num2 and num2 == num3:
    sum = sum * 3

print(sum)