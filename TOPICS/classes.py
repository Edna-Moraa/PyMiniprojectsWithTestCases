#classes are blueprints of classes

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model 

    def moves(self):
        print('Moves along....')

    def get_make_model(self):
        print(f"I am a {self.make} {self.model}.")    


my_car = Vehicle('Tesla', 'Model 3')


# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

our_car = Vehicle('Mercedes', 'Latest')
our_car.get_make_model()
our_car.moves()

##########
#inheritance

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along...')
class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')        
class GolfCart(Vehicle):
    pass
cessna = Airplane('Cessna', 'SKyhawk', 'N-1234r')    
mack = Truck('mack', 'Pinnacle')    
golfwagon = GolfCart('Yahama', 'GC100')    


cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


###polymorphism- same input but behaves differently based on how they were built
print('\n\n')

for v in (my_car,our_car,cessna,mack,golfwagon):
    v.get_make_model()
    v.moves()