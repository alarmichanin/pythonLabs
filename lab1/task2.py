from sys import argv
from functools import reduce
from operator import add, sub, mul, truediv


operations = {'add': add, 'sub': sub, 'mul': mul, 'div': truediv}
operatorUse = argv[1]
nums = argv[2:]
# next operation give us oppportunity to use for every member of list some operation which user choose
# before it we convert type of member to int
print(reduce(lambda a, b: operations.get(operatorUse)(int(a), int(b)), nums))