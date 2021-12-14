from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Triangolo(Figura):
    
    def __init__(self, base, b, c, altezza):
        self.base = base
        self.altezza = altezza
        self.b = b
        self.c = c

    def area(self):
        return (self.base * self.altezza) / 2

    def perimetro(self):
        return self.base + self.b + self.c   

class Circonferenza(Figura):
    pass


lol = Triangolo(2, 2, 2, 4)
print(lol.area(), lol.perimetro())