import random
# import matplotlib.pylot as plt

# Placing the car inside the list at a random number
for i in range(1):
    # Doors for the simulation
    behind_gate = ['goat', 'goat', 'goat']
    
    # Logic to put car at a random spot in list
    car = random.randint(0,2)
    behind_gate[car] = 'car'

# Taking the input from the user and opening the door with the gate
choice = int(input("Choose the door from 1-3: "))
print(f"You have chosen the gate number: {choice}")

# Opening the door which has goat behind it
print(f"\nThere is a goat behind the door {behind_gate.index('goat')+1}")
second_choice = input('\nWould you like the switch the door, if yes please enter ' \
'the new door number if not enter the earlier door number: ')
second_input = int(second_choice) - 1

if behind_gate[second_input] == 'car':
    print('You won the car')
else:
    print(f"The car was behind door {behind_gate.index('car')}")