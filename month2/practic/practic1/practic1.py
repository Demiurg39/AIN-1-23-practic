class Animal():
    def __init__(self, hеight:int, age:int, color:str, tail:bool, crawl:bool,):
        """Class for animal"""
        self.height = hеight
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
        return (
f"Animal height - {self.height}\nAnimal age - {self.age}\nAnimal color - {self.color}\n\
Animal has tail - {self.tail}\nAnimal crawl - {self.crawl}"
)

class Mammals(Animal):
    def __init__(self, hair_amount:str, milk:bool,hеight:int, age:int, color:str, tail:bool, crawl:bool,):
        super().__init__(hеight, age, color, tail, crawl,)