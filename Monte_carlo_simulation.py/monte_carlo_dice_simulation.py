import random
import matplotlib.pyplot as plt

# --- 1. Define the simulation function (rolling two dice) ---
def roll_dice():
    """Simulates rolling two six-sided dice and checks if they are the same."""
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    return die_1 == die_2

# --- 2. Set up inputs and tracking variables ---
num_simulations = 10000
max_num_rolls = 1000
initial_balance = 1000
bet_amount = 1
payout_multiplier = 4 # House pays 4 times the bet for a win

end_balances = []

# Optional: Set up figure for plotting
# fig = plt.figure()
# plt.title(f"Monte Carlo Dice Game [{num_simulations} simulations]")
# plt.xlabel("Roll Number")
# plt.ylabel("Balance [$]")
# plt.xlim([0, max_num_rolls])

# --- 3. Run the Monte Carlo simulation ---
for i in range(num_simulations):
    balance = [initial_balance]
    num_rolls = [0]
    # num_wins = 0 # Optional: track wins
    while num_rolls[-1] < max_num_rolls:
        same = roll_dice()
        if same:
            balance.append(balance[-1] + payout_multiplier * bet_amount)
            # num_wins += 1
        else:
            balance.append(balance[-1] - bet_amount)
        num_rolls.append(num_rolls[-1] + 1)
    
    end_balances.append(balance[-1])
    # plt.plot(num_rolls, balance) # Plot each simulation run

# --- 4. Analyze and display results ---
# plt.show() # Display the plot of all balance paths
average_end_balance = sum(end_balances) / len(end_balances)

print(f"Average ending balance after {num_simulations} runs (each with {max_num_rolls} rolls): ${average_end_balance:.2f}")

# The average win probability can also be calculated and displayed
