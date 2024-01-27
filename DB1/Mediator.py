

class Runway:
    def __init__(self, name: str):
        self.name = name
        self.busy = False
        print(f"Runway {name} is created.\n")

    def is_busy(self) -> bool:
        return self.busy

    def set_busy(self, condition: bool) -> None:
        self.busy = condition

    def get_name(self) -> str:
        return self.name


class APlane(ABC):

    @abstractmethod
    def approach(self):
        """plane approaches"""

    @abstractmethod
    def descend(self):
        """plane descends to land"""

    @abstractmethod
    def slow_down(self):
        """plane slows down to descend"""

    @abstractmethod
    def bypass(self):
        """plane bypasses the runway and laps around the runway"""


class AirMediator(ABC):

    @abstractmethod
    def receive(self, plane: APlane):
        """"""

    @abstractmethod
    def ask_to_land(self, plane: APlane):
        """"""

    @abstractmethod
    def done(self, plane: APlane):
        """"""


class Tower(AirMediator):

    def __init__(self, name: str, runway: Runway):
        self.name = name
        self.runway = runway
        self.plane_list = []
        print(f"Mediator {name} is created.\n")

    def receive(self, plane: APlane):
        plane.slow_down()
        self.plane_list.append(plane)
        print(f"MEDIATOR: {plane.name} is received.\n")

    def ask_to_land(self, plane: APlane):
        print(f"{plane.name} asked for permission to land.")
        if self.runway.is_busy() == False:
            print(f"MEDIATOR: Permission to {plane.name} GRANTED.")
            self.runway.set_busy(True)
            plane.descend()
        else:
            print(f"MEDIATOR: Permission to {plane.name} REJECTED.")
            plane.bypass()

    def done(self, plane: APlane):
        print(f"MEDIATOR: {plane.name} has landed.\n")
        self.plane_list.remove(plane)
        self.runway.set_busy(False)


class Plane(APlane):

    def __init__(self, name: str, runway: Runway, mediator: AirMediator):
        self.name = name
        self.runway = runway
        self.mediator = mediator
        self.approach()
        self.mediator.receive(self)

    def approach(self):
        print(f"PLANE: {self.name} is approaching to {self.runway.get_name()}\n")

    def descend(self):
        descend_time = random.randint(0, 4)
        print(f"PLANE: {self.name} is descending in {descend_time} secs.\n")
        time.sleep(descend_time)
        self.mediator.done(self)

    def slow_down(self):
        print(f"PLANE: {self.name} is slowing down.\n")

    def bypass(self):
        lap_time = random.randint(0, 5)
        print(f"PLANE: {self.name} is bypassing in {lap_time} secs.\n")
        time.sleep(lap_time)
        self.mediator.ask_to_land(self)

    def fly(self):
        print(f"PLANE: {self.name} is flying towards {self.runway.get_name()}\n")
        self.mediator.ask_to_land(self)


def simulate():
    runway = Runway("Istanbul East Runway")
    tower = Tower("Tower Main", runway)

    n_planes = 3
    plane_list = []
    for i in range(n_planes):
        plane = Plane("Plane " + str(i), runway, tower)
        plane_list.append(plane)

    threads = []
    for plane in plane_list:
        thread = threading.Thread(target=plane.fly)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
