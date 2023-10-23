class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        self.words = "Meow"


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        self.words = "Woof"


class Pets:
    def __init__(self, pet):
        animals = dict(dog=Dog("Tom"), cat=Cat("Peace"))
        self.pet = animals[pet]

    def pet_speak(self):
        self.pet.speak()
        print("{0.name} says {0.words}".format(self.pet))


d = Pets("dog")
c = Pets("cat")
d.pet_speak()
c.pet_speak()
