from abc import ABC, abstractmethod
from Object import Object
from Atmosphere import Atmosphere

class Planet(Object):
    """
    A Planet object.
    """
    def __init__(self, name: str = "Planet", radius: float = 0.0, distance_to_host: float = 0.0,
                 atmosphere: Atmosphere = Atmosphere()):
        super().__init__(name, radius)
        self.distance_to_host = distance_to_host
        self.atmosphere = atmosphere

    def setDistanceToHost(self, distance_to_host: float) -> None:
        self.distance_to_host = distance_to_host

    def getDistanceToHost(self) -> float:
        return self.distance_to_host

    def setAtmosphere(self, atmosphere: Atmosphere) -> None:
        self.atmosphere = atmosphere

    def getAtmosphere(self) -> Atmosphere:
        return self.atmosphere

    def isHabitable(self) -> bool:
        return True