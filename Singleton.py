"""
Name: singleton, type: creational
Problem:
-  manage concurrent access to a shared resource
-  create a global point of access for a resource
   example: manage concurrent access to resource
-  Global point access to writing log messages
solution:
-  create a global variable inside a module and import it whenever we need to use it
-  allow the creation of only one instance of the class that represents our protected resource
-  In case we want to use inheritance, a shared state between instances should be addressed
Consequences:
-  we have the same drawbacks as global variables.
-  it violates the Single-responsibility principle.
-  it is a subject to Code smells.
-  it hides the dependencies the application's code, instead of exposing them through the interfaces.
"""
# create a global variable inside a module and import it whenever we need to use it
import Singleton


# print(singleton.shared_variable)
# singleton.shared_variable += "(modified by samplemodule1)"


class SingletonClass(object):
    inner_variable = ''

    def __new__(cls):  # supercharging the operator __new__ of the current class
        if not hasattr(cls, 'instance'): # checking if there are any other instances
            cls.instance = super().__new__(cls)  # we use the super constructor's new method to create a new object
            cls.inner_variable = 'the only variable' # following the python culture: not declaring class attributes, just using them directly
        return cls.instance


"""
- Now what happens if I need to use inheritance
"""


class Subclass(SingletonClass):
    pass


if __name__ == '__main__':

    singleton_1 = SingletonClass()
    singleton_2 = SingletonClass()
    singleton_3 = Subclass()

    if singleton_1 is singleton_2:
        print("Nothing new!")

    if singleton_1 is singleton_3:
        print("the child is the same as the parent")

    print(singleton_1.inner_variable)
    print(singleton_2.inner_variable)
    print(singleton_3.inner_variable)
