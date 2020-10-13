# Ask user where to look
print("\n-----Beep has lost his battery----- \n \nWhere should I look? \n(bedroom/bathroom/lab)")
where = input()

# User input - bedroom
if (where == "bedroom"):
  # Ask user where to look in bedroom
  print("\nWhere in the bedroom should I look? \n(under the bed/in the wardrobe)")
  bedroom_area = input()
  if (bedroom_area == "under the bed"):
    print("\nFound some shoes but no battery")
  else:
    print("\nFound mess but no battery")

# User input - bathroom
elif (where == "bathroom"):
  # Ask user where to look in bathroom
  print("\nWhere in the bathroom should I look? \n(in the bathtub/on the sink)")
  bathroom_area = input()
  if (bathroom_area == "in the bathtub"):
    print("\nFound a rubber duck but no battery")
  else:
    print("\nFound a wet surface but no battery")

# User input - lab
elif (where == "lab"):
  # Ask User where to look in lab
  print("Where in the lab should I look? \n(on the table/on the chair)")
  lab_area = input()
  if (lab_area == "on the table"):
    print("\nYes! I found my battery!")
  else:
    print("\nFound some tools but no battery")

# User input - elsewhere
else:
  print("\nI do not know where that is but I will keep looking.")