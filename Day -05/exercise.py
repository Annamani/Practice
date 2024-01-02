# number=2
# while number<=20:
#     if number%2==0:
#         print(number)
#     number+=1

# For Loop
# for number in range(1,21):
#     if number%2==0:
#         print(number)

num= int(input("Enter number: "))
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
