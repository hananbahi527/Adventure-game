
import time
import random

def print_then_pause(line, sec=3):
    """
    Prints a line and then pauses for a specified amount of seconds.

    Args:
        line (str): The line to print.
        sec (int): The number of seconds to pause.
    """
    print(line)
    time.sleep(sec)

def print_pause(text, delay=0.05):
    """
    Prints the provided text with a slight delay between each character.

    Args:
        text (str): The text to print.
        delay (float): The delay between each character.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_user_input(prompt, valid_choices):
    """
    Prompts the user for input until a valid choice is made.

    Args:
        prompt (str): The prompt to display to the user.
        valid_choices (list): A list of valid choices the user can make.

    Returns:
        str: The user's valid input.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_choices:
            return user_input
        else:
            print(f"Invalid choice. Please enter one of {valid_choices}.")

def introduction():
    """
    Introduction to the game, including user input for name and readiness.
    """
    print_pause("Welcome to the Interstellar Journey!")
    time.sleep(1)
    user_name = input("Enter your space captain name: ").strip()
    while not user_name:
        print("Please enter a name.")
        user_name = input("Enter your space captain name: ").strip()
    time.sleep(1)
    print_pause(f"Greetings, Commander {user_name}!")
    return user_name

def handle_distress_call():
    """
    Handles the scenario where the user receives a distress call.
    """
    total_score = 0
    print_then_pause("Starting the launch sequence...", 1)
    print_pause("You are traveling through the cosmos when you receive a distress call from a nearby planet.")
    response = get_user_input("Do you want to investigate the call? (yes/no): ", ["yes", "no"])

    if response == 'yes':
        total_score += 5
        explore_planet(total_score)
    else:
        print_pause("You ignore the call and continue your mission.")
        print_pause("Your score = 0")
        restart_game()

def explore_planet(total_score):
    """
    Manages the exploration of the planet, including different paths and choices.
    """
    print_then_pause("You land on the planet and step out of your spaceship.", 1)
    decision = get_user_input(
        "Do you explore the alien city or the mysterious cave? (city/cave): ",
        ["city", "cave"]
    )

    if decision == "city":
        explore_city(total_score)
    elif decision == "cave":
        explore_cave(total_score)

def explore_city(total_score):
    """
    Handles the scenario when the player chooses to explore the alien city.

    Args:
        total_score (int): The current total score of the player.
    """
    total_score += 5
    print_then_pause("You encounter a friendly alien who offers to guide you.", 0.5)
    print_pause("You have two options: follow the alien or explore on your own.")
    choice = get_user_input(
        "1. Follow the alien\n2. Explore on your own\nChoose 1 or 2: ",
        ["1", "2"]
    )

    if choice == "1":
        total_score = follow_alien(total_score)
    elif choice == "2":
        total_score = explore_alone(total_score)

    print_pause(f"Your total score is: {total_score}")
    restart_game()

def explore_cave(total_score):
    """
    Handles the scenario when the player chooses to explore the mysterious cave.

    Args:
        total_score (int): The current total score of the player.
    """
    total_score -= 1
    print_then_pause("You venture into the cave and find ancient alien technology.", 0.5)
    print_pause("Do you want to take the technology back to your ship? (yes/no): ")
    choice = get_user_input("yes or no: ", ["yes", "no"])

    if choice == "yes":
        total_score += 10
        print_pause("You discover the technology has immense value.")
    else:
        print_pause("You leave the technology and return to your ship.")
        print_pause("game over")

    print_pause(f"Your total score is: {total_score}")
    restart_game()

def follow_alien(total_score):
    """
    Handles the scenario where the user follows the alien.

    Args:
        total_score (int): The current total score of the player.
    """
    print_then_pause("The alien leads you to a hidden treasure chamber.", 0.5)
    total_score += 2
    print_pause("Inside the chamber, you find a precious artifact.")
    choice = get_user_input(
        "1. Take the artifact\n2. Leave it\nChoose 1 or 2: ",
        ["1", "2"]
    )

    if choice == "1":
        total_score += 10
        print_pause("Congratulations, you have found a rare artifact!")
    else:
        print_pause("You leave the artifact and exit the chamber.")
        print_pause("game over")

    return total_score

def explore_alone(total_score):
    """
    Handles the scenario where the user explores the city alone.

    Args:
        total_score (int): The current total score of the player.
    """
    total_score -= 1
    print_then_pause("You wander through the city and get lost.", 0.5)
    print_pause("Suddenly, a hostile alien appears!")
    choice = get_user_input(
        "1. Fight the alien\n2. Run away\nChoose 1 or 2: ",
        ["1", "2"]
    )

    if choice == "1":
        print_pause("The alien overpowers you.")
        print_pause("game over")
    else:
        print_then_pause("You manage to escape back to your spaceship.", 0.5)
        total_score += 1
        choice = get_user_input(
            "Do you want to search for another planet (1) or head back to Earth (2)?: ",
            ["1", "2"]
        )

        if choice == "1":
            total_score += 5
            print_pause("You find a planet rich with resources.")
            print_pause("You became a hero back on Earth!")
        else:
            print_pause("You return to Earth empty-handed.")
            print_pause("game over")

    return total_score

def restart_game():
    """
    Prompts the user to play again or exit.
    """
    restart_choice = get_user_input("Do you want to play again? (yes/no): ", ["yes", "no"])

    if restart_choice == "yes":
        start_game()
    else:
        print_pause("Hope you enjoyed the game!")

def start_game():
    """
    Begins the adventure, gathers user input, and sets up the game flow.
    """
    user_name = introduction()
    user_choice = get_user_input(
        "Ready to embark on your space quest? (yes/no): ",
        ["yes", "no"]
    )

    if user_choice == "yes":
        handle_distress_call()
    else:
        print_pause("Then why did you board the ship?")
        print_pause("Your score = 0")
        restart_game()

# Adding randomness
def random_event():
    events = [
        "You encounter a rogue asteroid field and have to navigate carefully.",
        "You receive a mysterious transmission from an unknown source.",
        "A sudden solar flare disrupts your ship's systems temporarily.",
        "You find a derelict spaceship drifting in space.",
        "A rare cosmic event gives you a spectacular light show."
    ]
    return random.choice(events)

def random_encounter():
    print_then_pause(random_event(), 1)
    print_pause("Do you want to investigate further? (yes/no): ")
    choice = get_user_input("yes or no: ", ["yes", "no"])

    if choice == "yes":
        return random.randint(1, 10)  # Random reward
    else:
        print_pause("You decide to continue your journey.")
        return 0

# Including random events in the game flow
def handle_distress_call():
    total_score = 0
    print_then_pause("Starting the launch sequence...", 1)
    print_pause("You are traveling through the cosmos when you receive a distress call from a nearby planet.")
    response = get_user_input("Do you want to investigate the call? (yes/no): ", ["yes", "no"])

    if response == 'yes':
        total_score += 5
        total_score += random_encounter()
        explore_planet(total_score)
    else:
        print_pause("You ignore the call and continue your mission.")
        print_pause("Your score = 0")
        restart_game()

# Starting the game
if __name__ == "__main__":
    start_game()
