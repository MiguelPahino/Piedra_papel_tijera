#!/usr/bin/python3

import random
from enum import IntEnum


class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2



class Game:

    def __init__(self):
        # Diccionario: acción del usuario -> acciones que lo vencen
        self.victories = {
            GameAction.Rock: [GameAction.Paper],
            GameAction.Paper: [GameAction.Scissors],
            GameAction.Scissors: [GameAction.Rock]
        }


    def assess_game(self, user_action, computer_action):

        if user_action == computer_action:
            print(f"User and computer picked {user_action.name}. Draw game!")
        elif computer_action in self.victories[user_action]:
            print(f"User picked {user_action.name} and computer picked {computer_action.name}. User loses!")
        else:
            print(f"User picked {user_action.name} and computer picked {computer_action.name}. User wins!")


    def get_computer_action(self):
            
        valores = [accion.value for accion in GameAction]
        computer_action = random.choice(valores)

        return computer_action


    def get_user_action(self):
        # Scalable to more options (beyond rock, paper and scissors...)
        game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
        game_choices_str = ", ".join(game_choices)
        user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
        user_action = GameAction(user_selection)

        return user_action


    def get_random_computer_action(self):
        computer_selection = random.randint(0, len(GameAction) - 1)
        computer_action = GameAction(computer_selection)

        return computer_action


    def get_winner_action(self, game_action):
        return self.victories[game_action]


    def play_another_round(self):
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'y'



def main():
    game = Game()

    play_again = True
    while play_again:
        computer_action = game.get_random_computer_action()

        try:
            user_action = game.get_user_action()

        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        game.assess_game(user_action, computer_action)

        play_again = game.play_another_round()



if __name__ == "__main__":
    main()