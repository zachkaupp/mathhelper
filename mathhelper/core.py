"""core function of mathhelper"""

import random


def main():
    """main function of the mathhelper package"""
    possibilities = [[i, j] for i in range(1, 21) for j in range(i, 21)]
    while True:
        problem = random.choice(possibilities)
        answer = problem[0] * problem[1]
        print(f"{problem[0]} * {problem[1]}")
        user_input = input("::")
        try:
            if user_input == "stop":
                break
            elif int(user_input) != (answer):
                print(f"incorrect, {answer}")
        except ValueError:
            print("input is not accepted buddy, get less stoopid")
    print("program ending")
