from abc import ABC, abstractmethod
from Object import Object

class Star(Object):
    """
    Object represents a star with a certain temperature and size. The corresponding BB spectrum is used
    to calculate its influence at a certain distance.
    """

    def __init__(self, name: str = "Galaxy", radius: float = 0.0):
        super().__init__(name, radius)

