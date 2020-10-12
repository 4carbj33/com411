# Paint direction input
print("Towards which direction should I paint (up, down, left, or right)?")
direction = input()

# Message output for "up"
if (direction == "up"):
  print("\nI am painting in the upward direction!")

# Message output for "down"
elif (direction == "down"):
  print("\nI am painting in the downward direction!")

# Message output for "left"
elif (direction == "left"):
  print("\nI am painting in the left direction!")

# Message output for "right"
else: 
  print("\n I am painting in the right direction!")

# End Message
print("\n Painting complete!")