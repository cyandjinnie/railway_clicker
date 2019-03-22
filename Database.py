from Singleton import Singleton

class Database(metaclass=Singleton):
    def __init__(self):
        self.__dct = dict()

    def __getitem__(self, item):
        return self.__dct[item]

    def __setitem__(self, key, value):
        self.__dct[key] = value
