users = ['Edna', 'Moraa', 'Maburi']

data = ['Bry', 6, True]

emptylist = []

print(len(data))
print(users[1:])

users.append('Aggy')
print(users)

users.extend(['Edu', 'Arori'])
print(users)

# users.extend(data)
# print(users)

users.insert(1, 'Eleen')
print(users)

users.remove('Eleen')
print(users)

# print(users.pop())
# print(users)

data.clear()
print(data)

users[1:2]= ['kerush']
users.sort(key=str.lower)
print(users)


nums = [2,4,67,90,3]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
print(numscopy)

#Tuples
mytuple = tuple(('Edna',7, True))
print(mytuple)