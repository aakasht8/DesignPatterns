from Creational.Factory.Chair import Chair
from Creational.Factory.Table import Table


class Factory:

    @staticmethod
    def get_object(user_input):
        if user_input.lower() == 'chair':
            return Chair('Chair', 4).view_product()
        elif user_input.lower() == 'table':
            return Table('Table', 6).view_product()
        return 'The enter user input does not match any of the factory types'

