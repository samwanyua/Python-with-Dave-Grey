# filter() method
numbers = [3,7,12,18,21,20, 34,23,15]

odd_num = filter(lambda num : num % 2 != 0,numbers)
print(list(odd_num))