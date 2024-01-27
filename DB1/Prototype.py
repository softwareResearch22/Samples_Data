

class Cloneclass:
    type = None
    value = None

    def clone(self):
        pass

    def getType(self):
        return self.type

    def getValue(self):
        return self.value


class Type1(Cloneclass):

    def __init__(self, no):
        self.type = "Type1"
        self.value = no

    def clone(self):
        return copy.copy(self)


class Type2(Cloneclass):
    """ Concrete Cloneclass. """

    def __init__(self, no):
        self.type = "Type2"
        self.value = no

    def clone(self):
        return copy.copy(self)


class ObjectGroup:
    """ Manages prototypes.
    It encapsulates prototype
    initialization and then allows instantiation
    of the classes from these prototypes.
    """

    object1 = None
    object2 = None
    object3 = None
    object4 = None


    def initialize():
        ObjectGroup.object1 = Type1(1)
        ObjectGroup.object2 = Type1(2)
        ObjectGroup.object3 = Type2(1)
        ObjectGroup.object4 = Type2(2)

    @staticmethod
    def getObject1():
        return ObjectGroup.object1.clone()

    @staticmethod
    def getObject2():
        return ObjectGroup.object2.clone()

    @staticmethod
    def getObject3():
        return ObjectGroup.object3.clone()

    @staticmethod
    def getObject4():
        return ObjectGroup.object4.clone()
