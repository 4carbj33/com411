from human import Human
from robot import Robot

class Planet:

  # An initialiser (special instance method)
  def __init__(self):
    self.humans = []
    self.robots = []
  
  def __repr__(self, human):
    return f"Planet(humans={self.humans}, robots={self.robots})"
  
  def __str__(self):
   return f"This Planet has{len(self.humans)}Humans, and {len(self.robots)} Robots" 

  # An instance method
  def add_human(self, human):
    self.humans.append(human)

  def add_robot(self, robot):
    self.robots.append(robot)
  
  def remove_human(self, human):
    self.humans.remove(human)
  
  def remove_robot(self, robot):
    self.robots.remove(robot)

if (__name__ == "__main__"):
  planet = Planet()
  human = Human("human")
  planet.add_human(human)
  print(planet)
  print(repr(planet))