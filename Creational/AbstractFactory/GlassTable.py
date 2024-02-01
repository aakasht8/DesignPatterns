from Creational.AbstractFactory.IProduct import Product


class GlassTable(Product):

    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def print_items(self):
        return f'{self.name} has {self.legs} legs'
