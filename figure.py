from abc import ABC, abstractmethod
#from functools import total_ordering

class Figure(ABC):

    @abstractmethod
    def dots(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def square():
        pass

    @abstractmethod
    def color():
        pass

