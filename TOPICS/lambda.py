#lambda expression is a single expression that returns a value also called anonymous functions

squared = lambda num : num * num

print(squared(6))

addTwo = lambda num : num +2
print(addTwo(10))

sub = lambda a, b : a -b
print(sub(8,6))

##############


def funcBuilder(x):
    return lambda num : num + x
addTen = funcBuilder(10)
addTwenty =  funcBuilder(20)

print(addTen(7))
print(addTwenty(7))


#higher order functions
#it is a function that takes one or more functions or 
#a function that returns a function as its result

numbers = [3,7,9,12,16,21]
squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

###########filters

odd_nums = filter(lambda num : num % 2 !=0, numbers)
print(list(odd_nums))

##############
from functools import reduce

numbers = [1,2,3,4,5,1]
total = reduce(lambda acc, curr : acc + curr, numbers)
print(total)



names = ['Edna Moraa', 'Ed Edu', 'tghyjuikdosaplkjdhbakl']
char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)
print(char_count)