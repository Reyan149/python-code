class Grandpa:
    def __init__ (self, name, money, car):
        self.name = name
        self.money = money
        self.car = car
    
    def display_asset(self):
        return f'{self.name} has {self.money} pounds and a {self.car}'
    
class Grandson(Grandpa):
    def __init__ (self, name, money, car, bike, football):
        Grandpa. __init__(self, name, money, car)
        self.bike = bike
        self.football = football

    def display_asset(self):
        base_asset = Grandpa.display_asset(self)
        return (f'{base_asset}, {self.bike}, {self.football}')

gs1 = Grandson('Reyan', '100,000', 'Toyota Corolla', 'Yamaha', 'FIFA_Ball_5')
print(gs1.display_asset())