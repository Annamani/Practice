# Input2 variables along with sign
def calculation(a,b,sign):
    if sign=="+":
        return a+b
    elif sign=="-":
        return a-b

print(calculation(3, 5, "+"))


# # Show Employee details
def showEmployee(name,salary):
    print("Employee ",name,"salary is:", salary)

showEmployee("Sam", 9000)

# Inner and outer func
def outerFun(a, b):
    def cal(a,b):
        return a+b
    return cal(a,b)+8
result = outerFun(5, 10)
print(result)