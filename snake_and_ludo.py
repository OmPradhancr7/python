import random  # Import the random module to generate random numbers

def play_snake():
    print("Welcome to Snake (text version)!")  # Print welcome message
    print("+-------+-------+")                  # Print table header border
    print("| Turn  | Score |")                 # Print table column names
    print("+-------+-------+")                  # Print table header border
    score = 0                               # Initialize score to 0
    for turn in range(1, 6):                # Loop for 5 turns
        eat = random.choice([True, False])  # Randomly decide if food is eaten
        if eat:
            score += 10                     # Add 10 to score if food is eaten
        print(f"|  {turn:<5}|  {score:<5}|") # Print current turn and score in table row
    print("+-------+-------+")                # Print table footer border
    print("Game over! Final score:", score)  # Print final score

def play_ludo():
    print("Welcome to Ludo (4 Players, text version)!") # Print welcome message
    print("+-------+----------+----------+----------+")   # Print table header border
    print("| Turn  | Player   | Dice Roll| Position |")  # Print table column names
    print("+-------+----------+----------+----------+")   # Print table header border
    players = [
        ("Red", "🔴"),
        ("Blue", "🔵"),
        ("Green", "🟢"),
        ("Yellow", "🟡")
    ]                                               # List of players with their colors and emojis
    positions = {name: 0 for name, _ in players}    # Initialize player positions
    started = {name: False for name, _ in players}  # Track if players have started
    turn = 1                                         # Initialize turn counter
    winner = None                                    # Initialize winner variable

    while not winner:                                # Continue until there is a winner
        for name, emoji in players:
            input(f"{name} {emoji} - Press Enter to roll the dice...") # Wait for user to press Enter
            roll = random.randint(1, 6)              # Generate a random dice roll (1-6)
            if not started[name]:                    # Check if the game has not started for the player
                if roll == 6:                       # Check if the rolled number is 6
                    started[name] = True            # Set started to True to indicate the game has started for the player
                    positions[name] = 1              # Move player to position 1
                else:
                    positions[name] = 0               # Keep player at position 0 if the rolled number is not 6
            else:
                if positions[name] + roll <= 100:  # Check if the new position does not exceed 100
                    positions[name] += roll         # Add dice roll to player position
            print(f"|  {turn:<5}| {name+' '+emoji:<8}|    {roll:<6}|   {positions[name]:<7}|") # Print turn, player, roll, and position
            if positions[name] == 100:              # Check if the player has reached position 100
                winner = f"{name} {emoji}"        # Set the winner
                break
        turn += 1                                    # Increment turn counter
    print("+-------+----------+----------+----------+")   # Print table footer border
    print(f"Congratulations! {winner} wins the Ludo game!") # Print finish message

if __name__ == "__main__":                   # Only run the following if this file is executed directly
    print("Choose a game to play:")           # Print menu
    print("1. Snake")
    print("2. Ludo")
    choice = input("Enter 1 or 2: ")          # Get user choice
    if choice == "1":
        play_snake()                          # Run Snake game if user chose 1
    elif choice == "2":
        play_ludo()                           # Run Ludo game if user chose 2
    else:
        print("Invalid choice.")              # Print error if input is not 1 or 2
