class HotelBusiness:

    def __init__(self, name, rooms, floors):
        self.name = name
        self.rooms = rooms
        self.floors = floors
        print(f"{self.name} has {self.rooms} rooms and {self.floors} floors.")

    def display(self):
        print(f"{self.name} has {self.rooms} rooms and {self.floors} floors.")

ParisHotel = HotelBusiness("Paris Hotel", 100, 5)
LondonHotel = HotelBusiness("London Hotel", 150, 10)
DelhiHotel = HotelBusiness("Delhi Hotel", 200, 15)      

ParisHotel.display()
LondonHotel.display()
DelhiHotel.display()
