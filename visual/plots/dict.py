import matplotlib.pyplot as plt
import random as rnd

def data():
  paths = {}
  print("What type of line would you like?")
  line_style = input()
  print("What colour would you like?")
  colour = input()
  print("What style of marker would you like?")
  marker = input()

  paths['line_style'] = line_style
  paths['colour'] = colour
  paths['marker'] = marker

  return paths

def generate():
  print("How many lines would you like to display?")
  lines = int(input())
  
  for line in range(lines):
    values = data()
    x = rnd.sample(range(1,10), 5)
    y = rnd.sample(range(1,10), 5)
    format = f"{values['colour']}{values['line_style']}{values['marker']}"
    plt.plot(x, y, format)
  plt.show()

def run():
  print("Running...")
  generate()
  print("...Done!")
run()