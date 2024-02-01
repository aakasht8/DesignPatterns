from WoodenFactory import WoodenFactory
from GlassFactory import GlassFactory


class Factory:
    @staticmethod
    def get_items(factory_type):
        if factory_type == 'Wooden':
            return WoodenFactory.return_products()
        elif factory_type == 'Glass':
            return GlassFactory.return_products()
        return 'The entered items type does not match any of the existing factories..'
