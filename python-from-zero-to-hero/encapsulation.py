# coding=utf-8
# Encapsulation 封装 just convention 只是约定，实际还是能访问的


class Person:

    address = 'test'  # class attribute

    def __init__(self, name, age):
        self.name = name
        self._age = age  # non-public instance variables 实例变量

    # public method
    def show_age(self):
        return self._age

    def get_age(self):
        return self._get_age()

    # non-public method
    def _get_age(self):
        return self._age


p = Person('Pawn', 26)
print (p.address)
print (p.name, p._age)
print (p.show_age())
print (p._get_age())
