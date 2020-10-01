#User input - number of lives
lives = map(int, input("Please enter the number of lives: ").split())
print("")

#User input - energy level
energy = map(int, input("Please enter the energy level: ").split())
print("")

#User input - shield level
shield = map(int, input("Please enter the shield level: ").split())
print("")

#Output
print("Health has been set.")
print("")
for val in lives:
    print("Lives: ",'♥'*val)
for val in energy:
    print("Energy: ",'♦'*val)
for val in shield:
    print("Shield: ",'♦'*val)