number1=9
number2=5
total=number1+number2
print(total)

# # Take inputs
# # Store input numbers
# num1 = input('Enter first number: ')
# num2 = input('Enter second number: ')
# sum = float(num1) + float(num2)
# print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# Largest num
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
