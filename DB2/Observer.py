from abc import ABC
import copy  # Python provides its own routine to copy an object



class IDataController(ABC):
    "A Subject Interface"

    def subscribe(self, observer):
        "The subscribe method"
        pass

    def unsubscribe(self, observer):
        "The unsubscribe method"
        pass

    def notify(self, data):
        "The notify method"
        pass


class IDataModel(ABC):
    "A Subject Interface"

    def subscribe(self, observer):
        "The subscribe method"
        pass

    def unsubscribe(self, observer):
        "The unsubscribe method"
        pass

    def notify(self, data):
        "The notify method"
        pass


class DataController(IDataController):
    "A Subject (Observable)"

    _observers = set()

    def __init__(self):
        pass

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args):
        for observer in self._observers:
            observer.notify(*args)


class DataModel(IDataModel):
    "A Subject (Observable)"

    def __init__(self):
        self._observers = {}
        self._counter = 0
        # subscribing to an external hypothetical data controller
        self._data_controller = DataController()
        self._data_controller.subscribe(self)

    def subscribe(self, observer):
        self._counter = self._counter + 1
        self._observers[self._counter] = observer
        return self._counter

    def unsubscribe(self, observer_id):
        self._observers.pop(observer_id)

    def notify(self, data):
        for observer in self._observers:
            self._observers[observer].notify(data)


class IDataView(ABC):
    "A method for the Observer to implement"

    def notify(self, data):
        pass

    def draw(self, data):
        pass

    def delete(self):
        pass


class PieGraphView(IDataView):
    "The concrete observer"

    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subscribe(self)

    def notify(self, data):
        print(f"PieGraph, id:{self._id}")
        self.draw(data)

    def draw(self, data):
        print(f"Drawing a Pie graph using data:{data}")

    def delete(self):
        self._observable.unsubscribe(self._id)


class BarGraphView(IDataView):
    "The concrete observer"

    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subscribe(self)

    def notify(self, data):
        print(f"BarGraph, id:{self._id}")
        self.draw(data)

    def draw(self, data):
        print(f"Drawing a Bar graph using data:{data}")

    def delete(self):
        self._observable.unsubscribe(self._id)


class TableView(IDataView):
    "The concrete observer"

    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subscribe(self)

    def notify(self, data):
        print(f"TableView, id:{self._id}")
        self.draw(data)

    def draw(self, data):
        print(f"Drawing a Table view using data:{data}")

    def delete(self):
        self._observable.unsubscribe(self._id)


if __name__ == '__main__':

        DATA_MODEL = DataModel()
        # Add some visualisation that use the dataview
        PIE_GRAPH_VIEW = PieGraphView(DATA_MODEL)
        BAR_GRAPH_VIEW = BarGraphView(DATA_MODEL)
        TABLE_VIEW = TableView(DATA_MODEL)

        # A hypothetical data controller running in a different process
        DATA_CONTROLLER = DataController()

        # The hypothetical external data controller updates some data
        DATA_CONTROLLER.notify([1, 2, 3])

        # Client now removes a local BAR_GRAPH
        BAR_GRAPH_VIEW.delete()

        # The hypothetical external data controller updates the data again
        DATA_CONTROLLER.notify([4, 5, 6])

