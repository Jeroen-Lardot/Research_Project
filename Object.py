from abc import ABC, abstractmethod

class Object(ABC):
    """General Celestial object with a name and a radius"""
    @abstractmethod
    def __init__(self, name: str, radius: float):
        self.name = name
        self.radius = radius

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getRadius(self) -> float:
        return self.radius

    def setRadius(self, radius: float) -> None:
        self.radius = radius