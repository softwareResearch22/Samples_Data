"""
Name: prototype, type: Behavioral
Problem:
- The problem needs to have a lot of objects communicating with each other
- the interdependencies among the objects is complex, unstructured and difficult to understand
- The application's behavior is distributed among multiple classes and need to be dynamically customizable
  but using inheritance/subclassing is impractical
solution:
- The idea here is to encapsulate the communications among objects in a new object called 'mediator' this object acts like
  a router for the other objects
- every object must provide an interface that defines how it communicates with other objects, the mediator object can't provide
  such interface because that will violate the encapsulation principle of those objects
- thus every object can use the mediator to handle communications with the others
Consequences:
- the client's code is decoupled from the concrete objects that communicate with each others
- it increase the usability, since we can reuse the objects in an other application by only customizing the mediator
  which act here a protocol of communication
- the control over communication is centralized, the complexity of communication required by the objets is traded by the
  complexity in the mediator, however the mediator may becomes so hard to maintain.
Implementation:
  - First we need to abstract the communication protocol, which is the mediator, so a concrete protocol can implement it and
  customize it
  - Then we need to abstract the objects/components that want to communicate with each other in order to make them able to use
    the mediator to communicate, thus every component can dynamically use and change the mediator
  - implement the concrete objects in a way that they only use the mediator to communicate
"""
import abc
from abc import ABC


class Mediator(ABC):
    """
    Here we provide an interface for the mediator to implement in order to create any variation we want
    We assume that our future objects will notify each other which certain events
    """

    @abc.abstractmethod
    def notify(self, sender, event):
        pass


class BaseComponent:
    """
    Now we abstract the the objects/components that want to communicate with each other, they need to have the ability to
    change their mediator
    """

    def __init__(self, mediator=None):
        self._mediator = mediator

    @property
    def mediator(self):  # getter
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):  # setter
        self._mediator = mediator


"""now we can create real mediators and real objects that can use the mediator"""


class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A.")
        self._mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self._mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self._mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self._mediator.notify(self, "D")


class Mediator1(Mediator):
    """the mediator take a number of components and uses itself to set the components mediators"""

    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self  # uses itself to set the components mediators
        self._component2 = component2
        self._component2.mediator = self

    # now we define how each component is going to react to events and other components
    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


if __name__ == "__main__":
    # The client code, be careful at specifying events as it can go recursive
    c1 = Component1()
    c2 = Component2()
    mediator = Mediator1(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()
