# lamda functions
squared = lambda num: num * num

print(squared(2))

addTwo = lambda num : num + 200
print(addTwo(322))

# with two parameters
sum = lambda a, b : a * b
print(sum(32, 29))

##################################################
def funcBUilder(x):
    return lambda num : num + x

addTen = funcBUilder(10) # x = 10

addTwenty = funcBUilder(20) # x = 20

print(addTwenty(2)) # num = 2