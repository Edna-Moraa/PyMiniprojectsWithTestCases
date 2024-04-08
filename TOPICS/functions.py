def hello():
    print("hey Edna")
hello()    

def sum(num1, num2):
    if(type(num1)is not int or type(num2)is not int):
        return
    return num1+num2
total2 = sum("e", -8)
print(total2)


def multiple_items(*args):
    print(args)
    print(type(args))
multiple_items("EDNA",4, True)    


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
mult_named_items(first="Edna", last="Maburi")    


