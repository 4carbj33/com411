# Ask user number of bars to be charged
print("How many bars should be charged?")
charge = int(input())

# Declare a control variable
charged_bars = 0

# Charged bars
print()
while(charged_bars < charge):
  print("Charging:", end="")
  charged_bars = charged_bars + 1
  print("█" * charged_bars)
print("\nThe battery is fully charged.")