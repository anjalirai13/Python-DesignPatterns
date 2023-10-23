class ProducingAPI1:
    def produce_cuboid(self, length, breadth, height):
        print("ProducingAPI1 Produces Cuboid with length {} breadth {} and height {}".format(length, breadth, height))


class ProducingAPI2:
    def produce_cuboid(self, length, breadth, height):
        print("ProducingAPI2 Produces Cuboid with length {} breadth {} and height {}".format(length, breadth, height))


class Cuboid:
    def __init__(self, length, breadth, height, producingAPI):
        self._length = length
        self._breadth = breadth
        self._height = height
        self._producingAPI = producingAPI

    def produce(self):
        self._producingAPI.produce_cuboid(self._length, self._breadth, self._height)

    def expand(self, times):
        self._length = self._length * times
        self._breadth = self._breadth * times
        self._height = self._height * times


cube1 = Cuboid(1,3, 5, ProducingAPI1())
cube1.produce()

cube2 = Cuboid(15,10, 7, ProducingAPI2())
cube2.produce()