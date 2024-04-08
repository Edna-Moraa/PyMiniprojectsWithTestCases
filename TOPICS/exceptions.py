class Errors(Exception):
    pass
    

x=2
try:
    # print(x/1)
    # if not type(x) is str:
    #     raise TypeError('Only strings are allowed')
    # raise Exception('I am a custom exception')
    raise Errors("This in not a cool error")
except NameError:
    print('there is an error with definition')    
except ZeroDivisionError:
    print('please do not divide by 0')   
except Exception as error:
    print(error)    
else:
    print('no errors') 

finally: 
    print('will run the finally block')    


