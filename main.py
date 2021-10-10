from Star import Star
from Atmosphere import Atmosphere
from Planet import Planet
from Composition import Composition

star = Star(name="Sun", radius=1.0)
atmosphere = Atmosphere(name="Oxygen_Rich_Atmosphere", composition= Composition.EARTH, radius=0.01)
planet = Planet(name="Earth", radius=0.1, distance_to_host=1, atmosphere=atmosphere)

print("Planet: " +planet.getName(), "Containing atmosphere "+str(planet.getAtmosphere().getComposition().value)+ " Revolving around the star "
      + star.name + " with a radius of " + str(star.getRadius()) + " At a distance of " + str(planet.getDistanceToHost()))

