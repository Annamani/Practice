def outerFun(a, b):
    # Inner fucntion
    def cal(a,b):
        return a+b
    return cal(a,b)+8
result = outerFun(5, 10)
print(result)