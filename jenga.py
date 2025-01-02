import random

def display_tower(tower):
    """Display the current state of the tower."""
    print("\nCurrent Tower:")
    for level in tower:
        print(" | ".join(level))
    print()

def remove_block(tower):
    """Remove a block from a specified row and column."""
    while True:
        try:
            row = int(input(f"Enter the row number (1-{len(tower)}) to remove a block: ")) - 1
            if row < 0 or row >= len(tower):
                print("Invalid row. Try again.")
                continue

            available_blocks = [i for i, block in enumerate(tower[row]) if block != " "]
            if not available_blocks:
                print("No blocks available in this row. Try another row.")
                continue

            column = int(input(f"Enter the column number (1-3) to remove a block: ")) - 1
            if column in available_blocks:
                tower[row][column] = " "
                break
            else:
                print("Invalid column. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def check_stability(tower):
    """Check if the tower is still stable."""
    for i in range(len(tower) - 1):
        if tower[i] == [" ", " ", " "]:
            return False
    return True

def main():
    print("Welcome to Terminal Jenga!")
    tower = [["X", "X", "X"] for _ in range(6)]  # Build a tower with 6 levels
    game_over = False

    display_tower(tower)

    while not game_over:
        remove_block(tower)
        display_tower(tower)

        if not check_stability(tower):
            print("Oh no! The tower collapsed!")
            game_over = True
        else:
            if random.random() < 0.1:  # Add random instability
                print("The tower is wobbling dangerously...")
                if random.random() < 0.3:
                    print("The tower has collapsed!")
                    game_over = True

    print("Game Over. Thanks for playing!")

if __name__ == "__main__":
    main()