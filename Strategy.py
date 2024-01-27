"""
Name: Strategy or Policy, type: Behavioral
Problem:
- We are building a complex system which has to deal with a dynamic problem that needs more that one algorithm to be used
- the choice of the algorithm to use depends heavily on the client request -> Different algorithms will be needed
  at different times.
- We need to hard code all the needed algorithms in the part of code used to handle the client's request
- Everytime we need to add a new algorithm or maintain some of them, we need to break the client code.
solution:
- encapsulate every algorithm in a separate class, the encapsulated algorithm is then called a concretestrategy
- make a common interface (called "strategy") available for all the (implemented by) classes that encapsulate the desired algorithms
- The client ( we call it here "context" ) can call the algorithms dynamically ( when it needs to) via the interface
- if the client (context) needs its data to be accessed then it can provide an interface to the Strategy class.
Consequences:
- the algorithms can be easily reused
- The algorithms can be easily upgraded and enriched using inheritance
- the client's code remain clean and easily maintained
- we can implement different behavior of the same algorithm.
- we can easily eliminate if-else and switch statements in the client's code
Drawbacks:
- the client must understand the different strategies so he can call the appropriate one
- we increase the number of objects in the design
- the unneeded amount of communication between the strategy interface and the context: sometimes the client use initiate the
  interface with all needed parameters in order to use a simple concrete strategy that does not need all that data and parameters
  to, avoid this, we need to increase coupling between the client and strategy which is a bad practice.
"""
"""implementation 
- As an example we are going to assume that a client needs different type of sorting algorithms
- We are going implement the sorting algorithms as concrete strategies
- we implement a common interface of the concrete strategies
"""

"""The Strategy interface declares operations common to all supported versions
    of the algorithms below
    The Context uses this interface to call the algorithm defined by a Concrete
    Strategy."""


class Strategy():

    def do_algorithm(self, data):
        pass


"""the first class implement an algorithm that sorts the passed data and return a list """


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)


"""the first class implement an algorithm that sorts the passed data and return a reversed list of it """


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))



class Context:
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy):
        """
        Passing the desired strategy through the constructor.
        """
        self._strategy = strategy


    def get_strategy(self):
        """
        Just a getter.
        """
        return self._strategy


    def strategy(self, strategy):
        """
        Just a setter
        """
        self._strategy = strategy

    def do_some_business_logic(self):
        """
        the point here is that this function delegate the work to the picked strategy
        instead of implementing the all the algorithms here and using a switch statement.
        """
        """at this point we don't know necessarily how the algorithm will handle the data!"""
        print("Context: Sorting data using the strategy")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


if __name__ == "__main__":

    """assuming that the client knows very well the differences between strategies, he can pick 
    a concrete strategy and passes it to the context"""
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()