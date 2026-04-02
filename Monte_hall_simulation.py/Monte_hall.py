import random

def place_car():
    """Randomly place the car behind one of the 3 doors."""
    doors = ['goat', 'goat', 'goat']
    car_index = random.randint(0, 2)
    doors[car_index] = 'car'
    return doors, car_index


def monty_reveals(doors, player_choice, car_index):
    """Monty opens a door that is not the player's choice and not the car."""
    possible = [i for i in range(3) if i != player_choice and i != car_index]
    return random.choice(possible)


def get_switch_door(player_choice, revealed_door):
    """Return the remaining unopened door (the switch option)."""
    return [i for i in range(3) if i != player_choice and i != revealed_door][0]


def get_valid_input(prompt, valid_options):
    """Keep asking until the user gives a valid input."""
    while True:
        response = input(prompt).strip().lower()
        if response in valid_options:
            return response
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")


def play_game():
    """Run one interactive round of the Monty Hall game."""
    print("\n--- Monty Hall Game ---")
    doors, car_index = place_car()

    choice_str = get_valid_input("Choose a door (1, 2, or 3): ", ['1', '2', '3'])
    player_choice = int(choice_str) - 1
    print(f"You chose door {player_choice + 1}.")

    revealed = monty_reveals(doors, player_choice, car_index)
    print(f"Monty opens door {revealed + 1} — it's a goat!")

    decision = get_valid_input("Do you want to switch? (yes / no): ", ['yes', 'no'])

    if decision == 'yes':
        final_choice = get_switch_door(player_choice, revealed)
        print(f"You switched to door {final_choice + 1}.")
    else:
        final_choice = player_choice
        print(f"You stayed with door {final_choice + 1}.")

    if doors[final_choice] == 'car':
        print("You won the car!")
    else:
        print(f"It was a goat. The car was behind door {car_index + 1}.")


def simulate(num_trials=10000):
    """Simulate the game to prove the statistics."""
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_trials):
        doors, car_index = place_car()
        player_choice = random.randint(0, 2)
        revealed = monty_reveals(doors, player_choice, car_index)

        if doors[player_choice] == 'car':
            stay_wins += 1

        switch_door = get_switch_door(player_choice, revealed)
        if doors[switch_door] == 'car':
            switch_wins += 1

    print(f"\n--- Simulation Results ({num_trials:,} trials) ---")
    print(f"Stay win rate:   {stay_wins / num_trials:.1%}")
    print(f"Switch win rate: {switch_wins / num_trials:.1%}")


play_game()
simulate()