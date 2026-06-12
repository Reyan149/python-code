class Grandpa:
    def __init__ (self, name, money, car):
        self.name = name
        self.money = money
        self.car = car
    
    def display_asset(self):
        return f'{self.name} has {self.money} pounds and a {self.car}'
    
class Grandson(Grandpa):
    pass

gp1 = Grandpa('John', '100,000', 'Toyota Corolla')
gs1 = Grandson('Reyan', '100,000', 'Toyota Corolla')

print(gp1.display_asset())