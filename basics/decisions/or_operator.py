# Ask user to pick an adventure
print("What type of adventure should I have?")
type = input()

# User input - scary/short
if ((type == "scary") or (type == "short")):
  print("\nEntering the dark forest!")

# User input - safe/long
elif ((type == "safe") or (type == "long")):
  print("\nTaking the safe route!")

# User input - other
else:
  print("\nNot sure which route to take.")