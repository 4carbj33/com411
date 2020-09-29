#User name input
name = input("what is your name human?")
print("")
print("Nice to meet you {}." .format(name))

#User age input
print("")
age = (int(input("How old are you (in years)?")))
print("Your age is {}" .format(age))

#User height input
print("")
height = float(input("How tall are you (in meters)?"))
print("Your height is {}m." .format(height))

#User weight input
print("")
weight = (float(input("How much do you weigh (in kilograms)?")))
print("Your weight is {}kg." .format(weight))

#BMI calculation
print("")
bmi = weight/(height**2)
print(name, "you are: {}" .format(age), " years old", "and your BMI is {}" .format(bmi))