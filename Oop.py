# classes - blue print for object

class Vehicle:
    def __init__(self,make, model):
        self.make = make #referring an object to itself
        self.model = model

    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f" I am a {self.make} {self.model}.")



my_car = Vehicle('Tesla', 'Model3')
# print(my_car.make) # retrieving values
# print(my_car.model)

my_car.get_make_model()
my_car.moves()

car_2 = Vehicle('BMW', 'x5')
car_2.get_make_model()

class Airplane(Vehicle):
    def __init__(self,make, model, faa_id):
        super().__init__(make,model)
        self.faa_id = faa_id

    def get_make_model(self):
        print(f"I am {self.make} {self.model} {self.faa_id}")
    
    def moves(self):
        print('Flies along..')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')

class GolfCart(Vehicle):
    pass

cessna = Airplane('Cessa', 'Skyhawk', 'EER3422')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')


cessna.get_make_model()
cessna.moves()


mack.get_make_model()
mack.moves()


golfwagon.get_make_model()
golfwagon.moves()

