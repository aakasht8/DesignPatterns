from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def view_product():
        # This is an interface method that needs to implemented in the child classes
        pass
