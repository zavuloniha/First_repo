class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

class Cat(Animal):
    def say(self):
        return "Meow"

class Dog(Animal):
    def say(self):
        return "Woof"

class CatDog(Cat, Dog):
    def say(self):
       pass
    def info(self):
        return f"{self.nickname}-{self.weight}"
        
class DogCat(Dog, Cat):
    def say(self): 
        pass
    def info(self):
        return f"{self.nickname}-{self.weight}"

cat = CatDog("S", 10)

print(cat.nickname)
print(cat.say())
print(cat.info)
