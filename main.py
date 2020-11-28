import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
    
def animate(frame): 
  global ax
  ax.xlim = (0, 10)
  ax.ylim = (0, 10)
  ax.plot(frame, frame, 'ro')
     
def run():
  some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
  plt.show()
run()








