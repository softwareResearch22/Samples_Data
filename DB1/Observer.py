
class abstractSubject(ABC):
    """
        Abstract Subject - Abstract patient in this demo
    """

    def __init__(self):
        self.__observers = []

    def addObs(self, observer):
        self.__observers.append(observer)

    def removeObs(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, arg=0):
        for o in self.__observers:
            o.update(self, arg)


class abstractObserver(ABC):
    """
        Abstract Observer - Abstract medical device in this demo
    """

    def __init__(self):
        pass

    def update(sel,data,obj):  ## shall be overridden
        pass


class covidPatient(abstractSubject):
    """
        Concrete Subject - Patient in this demo
    """

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.__physioParams = {"temperature": 0.0, "heartrate": 0.0, "oxygen": 0.0, "respiration": 0.0}

    ## function to the observed subject's state
    def setValue(self, measureType, val):
        if measureType in self.__physioParams:
            self.__physioParams[measureType] = val
            # print("{}'s {} set to: {}".format(self.name, measureType, str(val)) )
            self.notifyObservers()
        else:
            print("Parameter type \"{}\" not yet supported.".format(measureType))

    def getValue(self, measureType):
        if measureType in self.__physioParams:
            return self.__physioParams[measureType]
        else:
            return None


class thermometer(abstractObserver):
    """
        Concrete Observer - Thermometer
    """

    def __init__(self):
        super().__init__()


    def update(self, tt, obj):
        if tt.__class__ == covidPatient:
            temp = tt.getValue("temperature")
            if temp > 37.8:
                print("EMCY - " + "Temperature too high: " + str(temp))
            elif temp < 36.0:
                print("EMCY - " + "Temperature too slow: " + str(temp))
            else:
                print("INFO - " + "Temperature normal: " + str(temp))

        else:
            pass

class heartbeatMonitor(abstractObserver):
    """
        Concrete Observer - heartbeat monitor
    """

    def __init__(self):
        super().__init__()

    def update(self, tt, obj):
        if tt.__class__ == covidPatient:
            hr = tt.getValue("heartrate")
            if hr > 120:
                print("EMCY - " + "Heart rate too high: " + str(hr))
            elif hr < 35:
                print("EMCY - " + "Heart rate too slow:  " + str(hr))
            else:
                print("INFO - " + "Heart rate normal: " + str(hr))

        else:
            pass
