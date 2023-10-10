import pprint

class Animal():
    def __init__(self, height: int, age: int, color: str, tail: bool, crawl: bool):
        """Class for animal"""
        self.height = height
        self.age = age
        self.color = color
        self.tail = tail
        self.crawl = crawl

    def crawl(self):
        """Crawl might method"""
        if self.crawl:
            return self.crawl
        else:
            return False
    
    def __str__(self):
        """Return info about animal"""
        return (
            f"Animal height - {self.height}\nAnimal age - {self.age}\nAnimal color - {self.color}\n"
            f"Animal has tail - {self.tail}\nAnimal crawl - {self.crawl}"
        )

class Mammals(Animal):
    """Animal subclass for mammals animals"""
    def __init__(self, hair_amount: str, milk: bool, height: int, age: int, color: str, tail: bool, crawl: bool):
        super().__init__(height, age, color, tail, crawl)
        self.hair_amount = hair_amount
        self.milk = milk
        
    def __str__(self):
        """Return info about mammal """
        animal_info = super().__str__()
        return f"{animal_info}\nHair amount - {self.hair_amount}\nProduces milk - {self.milk}"

class WaterCreatures(Animal):
    """Animal subclass for water creatures"""
    def __init__(self, height: int, age: int, color: str, tail: bool, swim_speed: int):
        super().__init__(height, age, color, tail, False)  # Водные существа не ползают, поэтому crawl=False
        self.swim_speed = swim_speed
    
    def __str__(self):
        """Return info about creature"""
        animal_info = super().__str__()
        return f"{animal_info}\nSwim speed - {self.swim_speed}"

# class objects
mammal = Mammals("Thick", True, 150, 5, "Brown", True, True)
# print("Mammal:")
# print(mammal)

water_creature = WaterCreatures(50, 2, "Blue", True, 10)
# print("\nWater Creature:")
# print(water_creature)

class ZooShow():
    def __init__(self, zoo_shows: dict, ticket_price: float):
        self.shows = zoo_shows
        self.ticket_price = ticket_price  # Добавляем атрибут для цены билета

    def available_shows(self):
        pprint.pprint(self.shows)
        if input(f"Do you want a ticket for {', '.join(self.shows.keys())}? (y/N)\n> ").lower().startswith("y"):
            print(f"You got a ticket for {', '.join(self.shows.keys())} for ${self.ticket_price:.2f}")
            
        else:
            print("No ticket for you!")

# Пример использования классов и объектов
zoo_shows_data = {
    "Lion Show": "10:00 AM",
    "Dolphin Show": "2:00 PM",
    "Elephant Show": "4:00 PM"
}

ticket_price = 10.0  # Устанавливаем цену билета

zoo_shows = ZooShow(zoo_shows_data, ticket_price)
zoo_shows.available_shows()