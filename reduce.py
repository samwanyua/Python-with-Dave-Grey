# reduce() method
from functools import reduce


nums = [1,2,3,4,5,67,7]

total = reduce(lambda  accumulator, current : accumulator + current, nums, 30) # 30 is starting number
print(total)


# alternatively
print(sum(nums, 31)) # 31 is starting number

# complex solution


names = ['Sam Wanyua', 'Akigo Mumias', 'Nebchadnezzar', 'Josiah Juma']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)