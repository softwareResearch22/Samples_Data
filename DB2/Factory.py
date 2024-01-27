from abc import ABC, abstractmethod


class IChair(ABC):
    "The Chair Interface (Product)"

    @abstractmethod
    def get_dimensions(self):
        "A static interface method"
        pass


class SmallChair(IChair):
    "The Small Chair Concrete Class implements the IChair interface"

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }


class MediumChair(IChair):
    "The Medium Chair Concrete Class implements the IChair interface"

    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }


class BigChair(IChair):
    "The Big Chair Concrete Class implements the IChair interface"

    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }


class ChairFactory:  # pylint: disable=too-few-public-methods
    "The Factory Class"

    @staticmethod
    def get_chair(chair):
        "A static method to get a chair"
        if chair == 'BigChair':
            return BigChair()
        if chair == 'MediumChair':
            return MediumChair()
        if chair == 'SmallChair':
            return SmallChair()
        return None


if __name__ == '__main__':
        CHAIR = ChairFactory.get_chair("SmallChair")
        print(CHAIR.get_dimensions())
        CHAIR2 = ChairFactory.get_chair("MediumChair")
        CHAIR3 = ChairFactory.get_chair("BigChair")
