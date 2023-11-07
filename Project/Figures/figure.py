from abc import ABC, abstractmethod
from functools import total_ordering

@total_ordering
class Figure(ABC):

    def __eq__(self, x: int):
        return self.size == x
    
    def __gt__(self, x: int):
        return self.size > x


    @abstractmethod
    def dots(self):
        pass

    @property
    @abstractmethod
    def size(self):
        pass

    @property
    @abstractmethod
    def square():
        pass

    @abstractmethod
    def color():
        pass

