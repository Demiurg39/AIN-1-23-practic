# OOP - Object Oriented Programming - Объектно Ориентированное Программирование

# class Person():
#     def __init__(self, name, age, hobby, car, laptop, advanced_skills):
#         self.name = name
#         self.age = age
#         self.hobby = hobby
#         self.car = car
#         self.laptop = laptop
#         self.adv_skill = advanced_skills

#     def computer_game(self, game):
#         if game == "Metro":
#             return f"Your cruel man)"
#         elif game == "DOTA":
#             return f"Where is you parrents silly?"
#         else:
#             return f"I like {game}"
    
#     def __str__(self):
#         return (f"Имя - {self.name}\nВозраст - {self.age}\n\
# Хобби - {self.hobby}\nНоутбук - {self.laptop}\nОпыт работы - {self.adv_skill}")

# person0 = Person("Amir", 17, "Programming", False, True, None)
# person1 = Person("Ivan", 99, "Kopat kartoshke", True, False, 40.0)

# print(person0)
# print(person1)
# print(person0.computer_game("Minecraft"))


class Car():
    def __init__(self, title, volume, color, date_start, type_kuzov):
        self.title = title
        self.volume = volume
        self.color = color
        self.date_start = date_start
        self.type = type_kuzov

    def drive_on_road(self, comfort):
        if comfort == 5:
            return "Nice car"
        elif comfort == 4:
            return "Average car"
        elif comfort <= 3:
            return "Oomygood thats a piece of crap"
    
    def __str__(self):
        return (f"Brand - {self.title}\nVolume - {self.volume}\n\
color - {self.color}\nDate - {self.date_start}\nType - {self.type}")

car0 = Car("GODDES TOYOTA", 5.0, "Violet", 2023, "racer")

print(car0)
print(car0.drive_on_road(5))

# class ElictricCar(Car):
    