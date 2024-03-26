# reduce() method
from functools import reduce


nums = [1,2,3,4,5,67,7]

total = reduce(lambda  accumulator, current : accumulator + current, nums, 30) # 30 is starting number
print(total)


# alternatively
print(sum(nums, 31)) # 31 is starting number