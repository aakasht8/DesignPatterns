from Creational.Builder.HouseBuilder import HouseBuilder


class CastleBuilder:
    def __init__(self, name):
        self.name = name

    def construct(self):
        return HouseBuilder.construct(self.name)
