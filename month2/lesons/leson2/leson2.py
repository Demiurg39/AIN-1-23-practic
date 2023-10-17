class PhoneUsuall():
    def __init__(self, call:bool, color:str, cost:int):
        self.color = color
        self.call = call
        self.cost = cost

    def number(self, user):
        return user
    
class AndroidPhone(PhoneUsuall):
    def __init__(self, call, color, interface:str, cost, model:str):
        super().__init__(call, color, cost)
        self.interface = interface
        self.model = model

    def loading_time(self, time:int=15):
        return (f"Load time is - {time}")
       
    def __str__(self):
        return f"Phone color - {self.color}\nMight call - {self.call}\n\
Interface - {self.interface}\nModel - {self.model}"

android1 = AndroidPhone(True, "black", "oxygenOS", 50, "OnePlus 11")
# print(android1)
# print(android1.loading_time())
# print(android1.number(88005553535))

class IOSPhone(PhoneUsuall):
    def __init__(self, call, color, interface:str, cost, model:str):
        super().__init__(call, color, cost)
        self.interface = interface
        self.model = model 

    def gift_parents(self, mother, father):
        return f"Present phone to - {mother}\nPresent phone to - {father}"
    
    def __str__(self):
        return f"Phone color - {self.color}\nMight call - {self.call}\n\
Interface - {self.interface}\nModel - {self.model}"

iphone1 = IOSPhone(True, "white", "IOS", float("inf"), "Iphone 15 pro MAX")
print(iphone1)
# print(iphone1.gift_parents("Tanya", "Batya"))




class BankAccount():
    def __init__(self, login, password, id, money_amount):
        self.login = login
        self.__password = password
        self.id = id
        self.money = money_amount
    
    def withdraw(self):
        pass