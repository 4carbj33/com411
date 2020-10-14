# Ask user how many cables to remove
print("How many cables should I remove?")
cables = int(input())

# Declare a variable
cables_removed = 0

# Remove cables
print()
while (cables_removed < cables):
  print("Removed cable.")
  cables_removed = cables_removed + 1