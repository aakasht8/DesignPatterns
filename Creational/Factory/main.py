"""
Factory design pattern is used for adding an abstract factory layer before creating the actual object of a class
Eg: Client applications can decide at runtime whether they want a chair object or a table object..
"""
from Factory import Factory

if __name__ == '__main__':
    print('Implementing the factory design pattern in python')

    user_input = input('Enter the type of object that you want: (Chair or Table): ')

    obj = Factory.get_object(user_input)
    print(obj)

