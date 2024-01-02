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

# Palindrome string
def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True

print(isPalindrome('aza'))
