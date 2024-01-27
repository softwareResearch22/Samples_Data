"""
Name: Factory, type: creational
Problem:
-  We provide the client with the possibility of creating an object from a class, but the class itself is not enough
   to create the object
-  We want to alleviate the final user from the task of managing multiple inheritance and interfaces during creating complex
   objects.
-  We have created a library with complex classes and classes relationship and we want to simplify the objects creation
   operations.
solution:
-  one solution is to provide the client with a mechanism (static method) to choose which object he wants to create,
   then handle the object creation using the superclasses and interfaces
-  Expose all the possible object's types (via a data structure) that a client can use to create desired objects
Consequences:
-  Simplicity with objects creation
-  Low coupling between user code and the library: when something changes in the library code the client does not have
   to change his code
-  only the library can decide how to construct the object, the client has only to call a factory method
"""

"""implementation 
1- we are going to design all classes responsible for all type of objects
2- for providing types we are going to use a dictionary
3- we design a factory methode and expose it to the client
"""


class Animal:
    def declare_who_you_are(self):
        print("I am an abstract concept")


class Tiger(Animal):
    def declare_who_you_are(self):
        print("I am a Tiger")


class Cat(Animal):
    def declare_who_you_are(self):
        print("I am a Cat")


class Lion(Animal):
    def declare_who_you_are(self):
        print("I am a Cat")


animals = {
    "tiger": Tiger,
    "cat": Cat,
    "lion": Lion,
}

"""Factory Method"""


class ObjectTypeNotPermitted(Exception):
    """Exception raised for object types errors (objects other than those in the dictionary of animals"""

    def __init__(self, object_type, message="Object not permitted"):
        self.object_type = object_type
        self.message = message
        super().__init__(self.message)


def factory(animal):
    if animal not in animals.keys():
        raise ObjectTypeNotPermitted(animal)  # restricting the list of objects we can create
    return animals[animal]()


if __name__ == '__main__':
    object_1 = factory('cat')  # the user only need to call the factory method
    object_2 = factory('tiger')
    object_1.declare_who_you_are()  # the library dynamically pick the the right method to call
    object_2.declare_who_you_are()
