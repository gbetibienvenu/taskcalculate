import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    john = 3
    boy= 4

paulies = {
    Action.Scissors: [Action.john, Action.Paper],
    Action.Paper: [Action.boy, Action.Rock],
    Action.Rock: [Action.john, Action.Scissors],
    Action.john: [Action.boy, Action.Paper],
    Action.boy: [Action.Scissors, Action.Rock]
}

def get_user_option():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(option)
    return action

def get_computer_option():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    defeats = pauliers[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")

while True:
    try:
        user_action = get_user_option()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_option()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (x/z): ")
    if play_again.lower() != "x":
        break
