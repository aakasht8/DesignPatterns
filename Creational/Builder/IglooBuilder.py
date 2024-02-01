from Creational.Builder.HouseBuilder import HouseBuilder


class IglooBuilder:
    def __init__(self, name):
        self.name = name

    def construct(self):
        return HouseBuilder.construct(self.name)
