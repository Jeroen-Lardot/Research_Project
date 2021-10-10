from enum import Enum

def earth_atmosphere() -> dict():
    """Earth-like atmosphere"""
    return {"Nitrogen":0.78,"Oxygen":0.21}

class Composition(Enum):
    EARTH = earth_atmosphere()