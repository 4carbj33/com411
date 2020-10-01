#User input for activating robot
print("##########")
print("#        #")
print("#        #")
print("##########")
print("")
expression = input("Enter a character to activate robot: ")
print("")
print(">>> Robot: Hi, my name is Beep. What is your name human? <<<")
print("")
print("##########")
print("#  {}" .format(expression), " {}  #" .format(expression))
print("#  ----  #")
print("##########")

#User input for name
print("")
name = input("What is your name human?")
print("")
print(">>> Beep: Nice to meet you {}. <<<" .format(name))

#User input for age
print("")
print(">>> Beep: I want to get to know you better. How old are you {}? <<<" .format(name))
age = (int(input("How old are you (in years)?")))
print(">>> Beep: {}, you've aged well human. <<<" .format(age))

