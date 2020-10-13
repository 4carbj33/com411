# Ask user what they saw and heard
print("What did I hear?")
noise = input()
print("\nWhat did I see?")
view = input()

# User input - grr/two red eyes
if ((noise == "grr") and (view == "two red eyes")):
  print("\nThere is a scary creature. I should get out of here!")

# User input - hoot/some big eyes
else:
  print("\nI am a little scared but I will continue.")