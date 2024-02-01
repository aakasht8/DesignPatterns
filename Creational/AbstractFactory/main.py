"""
Implementing the Abstract Factory design pattern in python
This DP is used to implement the abstract factories that return similar types of products
Eg: Wooden Factory, Plastic Factory
"""
from Creational.AbstractFactory.Factory import Factory

if __name__ == '__main__':
    print('Implementing the Abstract Factory design pattern in python')
    user_input = input('Enter the items type that you want: (Wooden/Glass): ')
    items = Factory.get_items(user_input)
    if isinstance(items, str):
        print(items)
    else:
        print([item.print_items() for item in items])
