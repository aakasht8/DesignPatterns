from Creational.AbstractFactory.WoodenChair import WoodenChair
from Creational.AbstractFactory.WoodenTable import WoodenTable


class WoodenFactory:
    @staticmethod
    def return_products():
        chair = WoodenChair('Wooden Chair', 4)
        table = WoodenTable('Wooden Table', 6)
        return chair, table
