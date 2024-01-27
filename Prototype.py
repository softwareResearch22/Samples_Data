"""
Name: prototype, type: creational
Problem:
- creating the object is very complex for the client due to the high number of parameters required and
  the complex subclassing and interface implementations
- The client is required to know a lot about the object's composition and characteristics in order to create it
- the object creation is expensive in terms of time and resources
- There are already existed similar objects ( like those that the client wants to create) in the system.
- we need to reduce the number of classes used in the client code
solution:
- one idea to do this is to provide the client with the possibility to copy and use already existed objects
- make the object able to clone itself, we can't let an other class to clone it because it may violate encapsulation
- create a class that creates the objects ( prototypes ) then provide a static parameterized method to dynamically return
  the specific prototype wanted by the client
Consequences:
- Prototyping is another way for specializing a class other than inheritance.
- hiding the complexity of objects creation from the client
- reduced number of classes
- implementing the object is the client's code can be done without specifying the concrete class of the
  object itself , thus the client's code is completely decoupled
Implementation:
lets assume that pentagon and hexagon shapes are hard to create by the client, here we are going to first abstract
our shapes using an interface,then we implement the clone method and the other required methods inside.
next, we implement our concrete classes, then the prototyping class (the prototype manager) to dynamically load,add,remove
and use prototypes.
"""
import abc
import copy  # Python provides its own routine to copy an object


class Shape(abc):
    def __init__(self):  # a shape can be any other shape with and id and type : pentagon or hexagon
        self.id = None
        self.type = None

    """by definition in Python an abstract class is a class that contains at least one abstract method.
                this methode will be left for the concrete classes to define it"""

    @abc.abstractmethod
    def what_shape_are_you(self):
        pass

    """the most important method clone() should not depend on the concrete class defining the object"""

    def clone(self):
        return copy.copy(self)  # return a copy of itself

    """other getters and setters"""

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid


"""now it is time for our concrete classes"""


class Pentagon(Shape):
    def __init__(self):
        super().__init__()  # here we use the superclass constructor to set id to "none"
        self.type = "Pentagon"  # now we set our type

    """implementing the abstract method"""

    def what_shape_are_you(self):
        print('I am a ' + self.type + '!')


"""lets do the same for the hexagonal"""


class Hexagon(Shape):
    def __init__(self):
        super().__init__()  # here we use the superclass constructor to set id to "none"
        self.type = "hexagon"  # now we set our type

    """implementing the abstract method"""

    def what_shape_are_you(self):
        print('I am a ' + self.type + '!')


"""now we implement the prototyping class"""


class PrototypingClass:
    # cache to store prototypes data a dictionary with prototypes' IDs and actual objects per prototype
    cache = {}

    @staticmethod
    def get_a_prototype_clone(id):
        _shape = PrototypingClass.cache.get(id, None)
        return _shape.clone()  # here we use the interface method ( remember decoupling :) )

    @staticmethod
    def load():  # in this methode we create all the might needed prototypes for the client
        hexa = Hexagon()
        hexa.set_id("1")  # we give the prototype an id of 1
        PrototypingClass.cache[hexa.get_id()] = hexa  # we cache the protype with ID

        # the same for the pentagone
        Penta = Pentagon()
        Penta.set_id("2")
        PrototypingClass.cache[Penta.get_id()] = Penta


if __name__ == '__main__':
    PrototypingClass.load()  # load the prototypes

    hexa = PrototypingClass.get_a_prototype_clone("1")  # use the prototype dynamically
    print(hexa.get_type())

    Penta = PrototypingClass.get_a_prototype_clone("2")  # use the prototype dynamically
    print(Penta.get_type())
