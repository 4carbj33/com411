import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
    
def animate(frame): 
  global ax
  ax.set_xlim(0, 720)
  ax.set_ylim(-1, 1)
  x_values = np.arange(0, frame)
  x_in_radians = x_values * (np.pi / 180)
  y_values = np.sin(x_in_radians)
  ax.plot(x_values, y_values)
     
def run():
  some_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)
  plt.show()
run()








