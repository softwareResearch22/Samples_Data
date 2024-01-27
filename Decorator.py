"""
Name: Decorator, type: structural
Problem:
- We want to add an extended functionality to certain objects but without affecting the whole class: one way to do this
  is by using inheritance/subclassing but this will end up with every subclass having having the new functionality.
- The required new functionality is not fundamental enough to dictate a significant design change like adding subclasses
- The new functionality might be removed anytime soon, that's why it is better to use an other dynamic way to add it,
  other than affecting the design permanently.
- once we have added the new functionality we might need to add an other one, in order not to start from the beginning
  the extended objects need also to accept being re-extended by the same mechanism
solution:
- The idea here is to create a new object that implement the same interface as the object we want to extend, so the new
  object can override the existing methods, note that this is not an inheritance.
- but one problem here is that the new created object cannot override itself as required in the problem section, to address
  this problem, the new class that implements the common interface with the real object, should not be responsible for
  overriding the real objects, it should instead provide an interface to an other class that will be responsible for overriding
  the real objects, as a result of this, a new object can override itself since, it implement both the real object interface and the interface
  of the overrider itself
Consequences:
- More flexibility than a static inheritance
- pay-as-you-go approach to modify the architecture, features are added only if we need them
As drawbacks we could find:
- a lot of little objects
"""

import abc
from abc import ABC


class Component(ABC):
    """
    The common interface that should be implemented by both the real objects (that we want extend) and the new extended objects
    """
    """some kind of operation that needs to be replace or extended"""

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    """
    this class represent a real object that needs to be extended.
    """
    """the default operation implementation"""

    def operation(self):
        return "Default Operation"


class Decorator(Component):
    """
    To make the required recursive effect, this class can get and set its component and then delegate the operation overriding
    to a subclass
    """
    _component: Component = None

    def __init__(self, component: Component):
        self._component = component

    def component(self):
        return self._component

    def operation(self):
        """
        By default The Decorator delegates all work to the component to be extended (for the moment).
        """
        return self._component.operation()


"""now it is time finally to override real objects and also other Decorator"""


class ConcreteDecoratorA(Decorator):
    """
    Concrete Decorators override a real object or a decorator.
    """

    def operation(self):
        """
        we can either use the parent's implementation of real object/decorator or alter it!.
        """
        return f"ConcreteDecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):

    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"


def client_code(component: Component):
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """

    # ...

    print(f"RESULT: {component.operation()}", end="")

    # ...


if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    decorator1 = ConcreteDecoratorA(simple)  # extend "simple" using the ConcreteDecoratorA
    client_code(decorator1)
    decorator2 = ConcreteDecoratorB(decorator1)  # extend "decorator1" using the ConcreteDecoratorB
    client_code(decorator2)
    # print("Client: Now I've got a decorated component:")
    # client_code(decorator2)
