person = "Edna"
coins = 3


# message = "\n%s has %s coins left." %(person, coins)
# print(message)

# message = "\n{0} has {1} coins left.".format(person, coins)
# print(message)

# message = "\n{} has {} coins left.".format(person, coins)
# print(message)


player = {'person':'Edna', 'coins':3}
message = f"\n{person} has {coins} left."
print(message)
message = f"\n{person} has {2*5} left."
print(message)
message = f"\n{person.lower()} has {2*5} left."
print(message)
message = f"\n{player['person']} has {2*9} left."
print(message)

#passing formating options
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}")
for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")
for num in range(1, 11):
    print(f"{num} divided by 4.25 is {num / 4.25:.2%}")