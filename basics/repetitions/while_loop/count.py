# Ask user for number of cables to avoid
print("How many live cables should I avoid?")
cables = int(input())

# Declare a control variable
cables_to_avoid = 0

# Avoid cables
print()
while(cables_to_avoid < cables):
  print("Avoiding...", end="")
  cables_to_avoid = cables_to_avoid + 1
  print("Done!", cables_to_avoid, "cables avoided.")