"""
Implementing the Builder design pattern in Python
Builder DP is used when we need to do complex things while building an object...
Ex: Igloo or House Builder
"""
from Creational.Builder.CastleBuilder import CastleBuilder
from Creational.Builder.IglooBuilder import IglooBuilder

if __name__ == '__main__':
    print('Implementing the Builder design pattern in Python')
    user_input = input('Enter the builder type (Igloo / Castle): ')
    if user_input == 'Igloo':
        igloo = IglooBuilder('Igloo')
        print(igloo.construct())
    elif user_input == 'Castle':
        castle = CastleBuilder('Castle')
        print(castle.construct())
    else:
        print('Entered user input cannot be built...')
