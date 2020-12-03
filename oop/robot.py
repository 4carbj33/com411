class Robot:

  # A class attribute
  MAX_ENERGY = 100

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0
    self.energy = 0
  
  # An instance method
  def display(self):
    print(f"I am {self.name}")

  def eat(amount):
    if (self.energy + amount > Robot.MAX_ENERGY):
      self.energy = Robot.MAX_ENERGY
    else:
      self.energy += amount

  def move(distance):
    if (self.energy - distance < 0):
      self.energy = 0
    else:
      self.energy -= distance

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'
  
  def __str__(self):
   return f'My name is {self.__name} and I am {self.age} years old.' 

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()

  print(robot)
  print(repr(robot))



