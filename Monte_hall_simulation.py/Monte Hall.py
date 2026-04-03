import random
# import matplotlib.pylot as plt

def place_car():
    """Randomly place a car behind one of the 3 doors"""
    doors = ['goat', 'goat','goat']
    car_index = random.randint(0,2)
    doors[car_index] = 'car'
    return doors, car_index

def get_valid_input(prompt, valid_options):
    """Keep asking the user until valid input is received"""
    while True:
        response = input(prompt).strip().lower()
        if response in valid_options:
            return response
        print(f"Invalid input. Please enter one of: {','.join(valid_options)}")

def monty_door_reveal(doors, car_index, user_input):
    possible = [i for i in range(3) if i != user_input and i!= car_index]
    return random.choice(possible)

def switch_doors(user_input, revealed_door):
    """Return the unopened door"""
    result = [i for i in range(3) if i != user_input and i != revealed_door]
    return result[0]

def play_game():
    """Run the simulation of Monty Hall game"""
    print("\n----Monty Hall Simulation----")
    doors, car_index = place_car()

    choice_str = get_valid_input("Choose a door (1,2,3): ", ['1','2','3'])
    user_input = int(choice_str) -1
    print(f"You chose door {user_input +1}")

    revealed = monty_door_reveal(doors, car_index, user_input)
    print(f"Monty opens door {revealed +1} it's a {doors[revealed]} ")

    switch_decision = get_valid_input("Do you want to switch (yes/no): ", ['yes','no'])

    if switch_decision == 'yes':
        final_decision = switch_doors(user_input, revealed)
        print(f"You switched to door {final_decision +1}.")
    else:
        final_decision = user_input
        print(f"You stayed with the door {final_decision +1}")

    if doors[final_decision] == 'car':
        print("Congratulation you won the car")
    else:
        print(f"It was a goat. The car was behind {doors.index('car')}")


play_game()