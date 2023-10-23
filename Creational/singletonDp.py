class Borg:
    __shared_data = dict()

    def __init__(self):
        self.__dict__ = self.__shared_data
        self.state = "GeeksForGeeks"

    def __str__(self):
        return self.state


person1 = Borg()
person2 = Borg()
person3 = Borg()

person1.state = "DataStructures"
person2.state = "Algorithms"

print(person1)
print(person2)

person3.state = "Geeks"

print(person1)
print(person2)