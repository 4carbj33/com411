# Ask user to enter book cover type
print("What type of cover does the book have? (hard/soft)")
type = input()

# If soft, ask user to elaborate
if (type == "soft"):
  
  # Ask user if book is perfect bound
  print("\nIs the book perfect bound?")
  cover = input()
  # Book is perfect bound
  if (cover == "yes"):
    print("\nSoft cover, perfect bound books are very popular!")
  # Book is not perfect bound
  else:
    print("\nSoft covers with coils or stitches are great for short books")
else:
  print("\nBooks with hard covers can be more expensive!")