from Creational.Factory.IProduct import Product


class Table(Product):
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def view_product(self):
        return f'{self.name} has {self.legs} legs'
