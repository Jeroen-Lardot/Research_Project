from abc import ABC, abstractmethod
from Object import Object
from Composition import Composition

class Atmosphere(Object):
    """
    Atmosphere object with a certain composition. Required parameter for a Planet, even if no atmosphere is present.
    The effect of the atmosphere is determined using a composition enum that provides the required compositional
    parameters.
    """

    def __init__(self, name: str = "Atmosphere", composition: Composition = Composition.EARTH, radius: float = 0.0):
        super().__init__(name, radius)
        self.composition = composition

    def setComposition(self, composition) -> None:
        self.composition = composition

    def getComposition(self) -> Composition:
        return self.composition