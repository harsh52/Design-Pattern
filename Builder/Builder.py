'''
The Builder pattern is used to construct a complex object step by step. It allows you to create different types and
representations of an object using the same construction process.
'''

from abc import ABC, abstractmethod


class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None
        self.garage = None
        self.swimming_pool = None

    def __str__(self):
        return (f"House with {self.walls} walls, {self.roof} roof, {self.windows} windows, "
                f"{self.doors} doors, {'a garage' if self.garage else 'no garage'}, "
                f"and {'a swimming pool' if self.swimming_pool else 'no swimming pool'}.")


class HouseBuilder(ABC):
    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_garage(self):
        pass

    @abstractmethod
    def build_swimming_pool(self):
        pass

    @abstractmethod
    def get_house(self):
        pass


class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = 'brick'
        return self

    def build_roof(self):
        self.house.roof = 'tile'
        return self

    def build_windows(self):
        self.house.windows = 'double-glazed'
        return self

    def build_doors(self):
        self.house.doors = 'wooden'
        return self

    def build_garage(self):
        self.house.garage = True
        return self

    def build_swimming_pool(self):
        self.house.swimming_pool = True
        return self

    def get_house(self):
        return self.house

class HouseDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_simple_house(self):
        return (self.builder
                .build_walls()
                .build_roof()
                .build_windows()
                .build_doors()
                .get_house())

    def construct_luxury_house(self):
        return (self.builder
                .build_walls()
                .build_roof()
                .build_windows()
                .build_doors()
                .build_garage()
                .build_swimming_pool()
                .get_house())

builder = ConcreteHouseBuilder()
director = HouseDirector(builder)

simple_house = director.construct_simple_house()
print(simple_house)

luxury_house = director.construct_luxury_house()
print(luxury_house)
