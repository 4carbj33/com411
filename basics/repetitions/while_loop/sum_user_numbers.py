# Ask user for number
print("How many numbers should I sum up?")
no_of_numbers = int(input())

# Declare a control variable
added_numbers = 1

# Total
total = 0
while (added_numbers < no_of_numbers):
  print("Please enter number", added_numbers, "of",no_of_numbers, ":")
  number = int(input())
  total = total + number
  added_numbers = added_numbers + 1

# Result
print("The answer is", total)