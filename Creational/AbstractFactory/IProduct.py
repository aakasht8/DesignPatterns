from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def print_items():
        # This needs to be implemented in the child classes
        pass
