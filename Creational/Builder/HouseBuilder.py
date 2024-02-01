from Creational.Builder.House import House


class HouseBuilder:
    @staticmethod
    def construct(house_type):
        build = House()
        if house_type == 'Igloo':
            build.set_doors(1)
            build.set_windows(0)
        elif house_type == 'Castle':
            build.set_doors(20)
            build.set_windows(40)
        return build
