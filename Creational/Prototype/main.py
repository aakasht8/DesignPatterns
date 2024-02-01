"""
Implementing the prototype design pattern in Python
This pattern is used when obj creation takes time so we can use the same object that has been stored in the memory
"""
import copy


class MyList:
    def __init__(self, my_list):
        self.my_list = my_list

    def clone(self, mode):
        if mode == 0:
            return type(self)(self.my_list)
        elif mode == 1:
            # Shallow copy
            return type(self)(self.my_list.copy())
        elif mode == 2:
            # Deep copy
            return type(self)(copy.deepcopy(self.my_list))

    def __str__(self):
        return f'{self.my_list}'


def main():
    l1 = [10, 20, 30]
    m1 = MyList(l1)
    m2 = m1.clone(0)
    m2.my_list[0] = 30
    print(m2)
    print(m1)

    l1 = [10, 20, 30]

    m1 = MyList(l1)
    m2 = m1.clone(1)
    m2.my_list[0] = 30
    print(m2)
    print(m1)

    l1 = [10, 20, 30]

    m1 = MyList(l1)
    m2 = m1.clone(2)
    m2.my_list[0] = 30
    print(m2)
    print(m1)



if __name__ == '__main__':
    print('Implementing the prototype design pattern in Python')
    main()