"""
Name: Facade, Type: Structural
Problem:
- When the system has too many subclasses associated in a complex architectures and logic, we want to make it easier
  for the client to use them.
- The client has to understand all the architecture of the subsystem before he can use it
- Whenever a change is made to the architecture of the subclasses, all the clients need to be notified
- Whenever a change is made to the architecture of the subclasses, a change must be made in the way that the client
  use the system.
solution:
- Provide a simple interface to use the complex architecture of the subsystem
- decouple the complex subsystem's architecture from the client's code
Consequences:
- Only one point of entry is defined, thus, it is simpler for the client to communicate with the subsystem
- A facade can provide a simple default view of the subsystem that is good and easy enough for most clients.
- decoupling the subsystem from clients and other subsystems, thus, promoting subsystem independence and portability.
- The subsystem more reusable and easier to customize
"""

"""implementation 
1- we need to design a simple interface to the complex logic and architecture of all our subsystems
2- the interface should be able to handle the client's requests then delegate the work to the appropriate elements
   of the subsystem
3- Make sure that the client only need to understand the Facade template.   
4- make sure that the client work with the complex subsystems through the simple interface.
"""

"""Facade template"""


class Facade:
    """
    Here we pass all the subsystems we need to provide to the client through the __init__ method
    """

    def __init__(self, subsystem1, subsystem2):
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self):
        """
        The operation method is used for handling client request, then use the subsystems to perform
        the appropriate complex operations.
        """
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.initiate_system())
        results.append(self._subsystem2.initiate_system())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_1())
        results.append(self._subsystem2.operation_2())
        return "\n".join(results)


class Subsystem1:
    """
    The Subsystem can accept requests either from the facade or client directly.
    we may notice here that the facade itself is special type of client to the subsystem.
    """

    def initiate_system(self):
        return "Subsystem1: Ready!"


    def operation_1(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    """
    A second subsystem.
    """
    def initiate_system(self):
        return "Subsystem1: Ready!"

    def operation_2(self) -> str:
        return "Subsystem1: Go!"

def client_code(facade: Facade):
    """
    The client can now perform complex operations using only this function
    Here the client does not need to manage all the subsystems behind.
    """

    print(facade.operation(), end="")


if __name__ == "__main__":
    subsystem1 = Subsystem1() # we can either create the subsystems or let the facade create them
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)