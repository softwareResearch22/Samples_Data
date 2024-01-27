"""
Name: Proxy, Type: Structural
Problem:
-  We need to protect the access (creation or modification) of a certain object because of its high cost
-  we want to give the client the possibility of access certain behaviors/resources only if he "really" needs to,
   for example, accessing a database.
-  we want make the implementation less heavy in term of execution by providing replacements of resource-intensive
   objects and behaviors.
solution:
-  one solution is to use a certain object (proxy object) to manage the access and manipulation of our object of concern.
-  encapsulate all the necessary logic in the proxy object.
-  make the communication between the proxy object and the real object happens only if it is "really" needed.
Consequences:
-  the implementation is generally faster
-  the real resources are protected & the communication is more secure due to the proxy object interface.
-  we can provide access to the real object based the user context ( OS, access rights...)
-  it works also better when memory access is expensive or limited.
-  Without changing the client code, we can easily introduce the new proxies in our application.
-  The proxy that we create works even when the service object is not ready or is not available ( a database connection for example )
"""

"""implementation 
we are going to protect the access to our database: in the following examples we only approve bank cards of type VISA to be associated
with the client bank account
1- we create an object that is responsible of finding and associate the client account with the card
2- create a proxy object to handle the user request, then decide if the user "really" need to access the database.
"""


class DatabaseAccess():
    def __init__(self, request, direct=True):
        # Should not allow anyone to directly call DatabaseAccess()
        # but proxy can call it
        if direct:
            raise ValueError
        print("processing the request and updating the database...")
        """"more complex handling..."""
        pass


class OperationNotPermitted(Exception):
    """Exception raised for operation type errors"""

    def __init__(self, card_type, message="Operation is not permitted"):
        self.card_type = card_type
        self.message = message
        super().__init__(self.message)


class DatabaseProxy:
    __possible_cards = ["visa"] # the prefix __ makes the variable only accessible by the class's methods

    def request_access(self, card_type, userId):

        if card_type not in self.__possible_cards:
            raise OperationNotPermitted(card_type)
        else:
            #  proxy can call the real object
            return DatabaseAccess(card_type + userId, direct=False)


""""more complex handling methods goes here..."""

if __name__ == '__main__':
      #db = DatabaseAccess("my request") #error
      proxy = DatabaseProxy()
      access_1 = proxy.request_access('visa','user01')
      access_2 = proxy.request_access('mastercard', 'user01')
      #print (proxy.__possible_cards) # error
