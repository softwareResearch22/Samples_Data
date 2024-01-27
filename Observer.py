"""
Name: Observer, type: Behavioral
Problem:
-  We need to make changes in one object but we also need to notify all of the other objects about
   these changes, moreover, we don't know how many objects should be notified.
-  We need to notify a bunch of objects that a change was made but without making these objects tightly coupled with the
   client's code.
-  We need to dynamically change the objets receiving the notifications without changing the code of any of the objects.
solution:
- Create a publisher object that publishes data ( notifications ) that might be consumed by the other objets.
- provide each of the other objects with a mechanism to subscribe to the publisher object in order to receive
  the data (notifications)
- The publisher dose not have to know what objects are being notified, it just delivers data to them because they
  were subscribed.
Consequences:
- Objects can be reused and updated flexibly, Observers remain the same (loose coupling).
- This pattern provides support for broadcast communication in case we need it
"""

"""implementation 
1- understand the subject template/interface
2- understand the observer template/interface
3- to better understand this concept we are going to implement the magazine-clients model: the magazine producer should 
notify all the magazine's subscribers that a new magazine has been release.
"""

"""Subject template"""


class Subject:
    """The class using this template has information to publish, it manages subscriptions
       and also notify them about any information has been produced"""

    def attach(self, observer):
        """
        Attach an observer to the subject.
        """
        pass

    def detach(self, observer):
        """
        Detach an observer from the subject.
        """
        pass

    def notify(self):
        """
        Notify all observers about an event.
        """
        pass


"""Observer template"""


class Observer:
    """
    the class that implementing the observer reacts to the update made to a certain subject, then
    send notifications about those updates to all the subject's subscribers.
    """

    def update(self, subject):  # here we handle the updates/data
        """
        Receive update from subject.
        """
        pass


"""---------------------------------------------EXAMPLE--------------------------------------------"""


class Magazine(Subject):  # the magazine is the subject
    _title = ""
    _type_of_magazine = ""
    _subscribers = []

    def attach(self, observer):
        self._subscribers.append(observer)

    def detach(self, observer):
        self._subscribers.remove(observer)

    def notify(self):
        print("Magazine: Notifying observers...")
        for observer in self._subscribers:
            observer.update(self)  # calling the update methods of the observers and sent them the subject

    def publish_new_magazine(self, title, type):
        self._title = title
        self._type_of_magazine = type
        self.notify()


"""the clients are all observers, if they are subscribed they can receive data about the update, moreover, they
can react/choose to take data or reject it"""


class Client(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, subject):
        print("Client: " + self.name + " received an update about magazine: " + subject._title)


if __name__ == '__main__':
    client1 = Client("Joe")
    client2 = Client("Sara")
    magazine = Magazine()
    magazine.attach(client2)
    magazine.publish_new_magazine("the runner","sports")

