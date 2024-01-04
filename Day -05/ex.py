num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
sum = num1 + num2 + num3
if num1 == num2 and num2 == num3:
    sum = sum * 3
print(sum)


num_grade = int(input("Grade: "))

if num_grade >= 90:
    print("A")
elif num_grade >= 80:
    print("B")
elif num_grade >= 70:
    print("C")
elif num_grade >= 60:
    print("D")
else:
    print("F")


year = int(input("Input a year: "))

if year%4 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")