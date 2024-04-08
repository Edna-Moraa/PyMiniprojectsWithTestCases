#while loop
# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
        
#     print(value)
# else:
#     print("value is now equal to " + str(value))



#for loop
# names = ["Edna", "Moraa", "Maburi"]
# for x in names:
#     print(x)

# for x in "Dorothy":
#     print(x)    
# for x in names:
#     if x == "Moraa":
#         break
#     print(x)

# for x in names:
#     if x == "Moraa":
#         continue
#     print(x)


# for x in range(4):
#     print(x)

# for x in range(2,4):
#     print(x)

# for x in range(10,100, 5):
#     print(x)
# else:
#     print("done")  


names = ["Edna", "Moraa", "Maburi"]
actions = ["code", "read", "walk"]
# for name in names:

#     for action in actions:
#         print(name + " " + action + ".")


for action in actions:

    for name in names:
        print(name + " " + action + ".")        

  