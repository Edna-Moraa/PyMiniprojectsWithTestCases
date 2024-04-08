#global scope
name = "Edna"
count = 1

#local scope

def again():
    color = "red"
    # global count 
    # count +=2
    print(count)

    def greeting(name):
        nonlocal color
        color = "blue"
        print(color)
        print(name)

    greeting("Maburi")

again()   
