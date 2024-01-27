from abc import ABC
import copy  # Python provides its own routine to copy an object



class IComponent(ABC):
    "An interface that each component will implement"


    def notify(self, message):
        "The required notify method"
        pass

    def receive(self, message):
        "The required receive method"
        pass


class Mediator:
    "A Subject whose notify method is mediated"

    def __init__(self):
        self._components = set()

    def add(self, component):
        "Add components"
        self._components.add(component)

    def notify(self, message, originator):
        "Add components except for the originator component"
        for component in self._components:
            if component != originator:
                component.receive(message)


class Component(IComponent):

    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name

    def notify(self, message):
        print(self._name + ": >>> Out >>> : " + message)
        self._mediator.notify(message, self)

    def receive(self, message):
        print(self._name + ": <<< In <<< : " + message)


if __name__ == '__main__':
        MEDIATOR = Mediator()
        COMPONENT1 = Component(MEDIATOR, "Component1")
        COMPONENT2 = Component(MEDIATOR, "Component2")
        COMPONENT3 = Component(MEDIATOR, "Component3")
        MEDIATOR.add(COMPONENT1)
        MEDIATOR.add(COMPONENT2)
        MEDIATOR.add(COMPONENT3)

        COMPONENT1.notify("data A")
        COMPONENT2.notify("data B")
        COMPONENT3.notify("data C")
