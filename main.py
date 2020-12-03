class Human:

  # A class attribute
  MAX_ENERGY = 100

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY
  
  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
  def grow(self):
    self.age += 1

  def eat(amount):
    if (self.energy + amount > Human.MAX_ENERGY):
      self.energy = Human.MAX_ENERGY
    else:
      self.energy += amount

  def move(distance):
    if (self.energy - distance < 0):
      self.energy = 0
    else:
      self.energy -= distance

  def __repr__(self):
    return f'human(name={self.name}, age={self.age})'
  
  def __str__(self):
   return f'My name is {self.__name} and I am {self.age} years old.' 

if (__name__ == "__main__"):
  human = Human()
  human.display()

  print(human)
  print(repr(human))