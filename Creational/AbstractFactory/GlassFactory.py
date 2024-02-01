from Creational.AbstractFactory.GlassChair import GlassChair
from Creational.AbstractFactory.GlassTable import GlassTable


class GlassFactory:
    @staticmethod
    def return_products():
        chair = GlassChair('Glass Chair', 4)
        table = GlassTable('Glass Table', 6)
        return chair, table
