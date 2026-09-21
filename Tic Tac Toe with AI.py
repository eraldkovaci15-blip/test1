import random
import time


def user_choice_operator():
    while True:
        u_operator = input("Choose the operator (x/o): ").lower()

        if u_operator == 'x' or u_operator == 'o':
            return u_operator

        print("Invalid input. Please enter x/o")


def computer_choice_operator(u_operator):
    if u_operator == 'x':
        return 'o'

    return 'x'


def user_choice_position():
    while True:
        try:
            column = int(input("Enter the column (1-3): "))
            row = int(input("Enter the row (1-3): "))

            if 1 <= row <= 3 and 1 <= column <= 3:
                return row - 1, column - 1

            print("Please enter numbers between 1 and 3.")

        except ValueError:
            print("Invalid number.")


def computer_choice_position(matrix):
    empty_places = []

    for row in range(3):
        for column in range(3):
            if matrix[row][column] == ' ':
                empty_places.append((row, column))

    return random.choice(empty_places)


def place_is_taken(row, column, matrix):
    return matrix[row][column] != ' '


def display_matrix(matrix):
    print()

    for row in matrix:
        print(" | ".join(row))
        print("---------")

    print()


def the_winner(matrix, operator):
    for row in range(3):
        if (matrix[row][0] == the_operator_playing[operator] and
            matrix[row][1] == the_operator_playing[operator] and
            matrix[row][2] == the_operator_playing[operator]):
            return True

    for column in range(3):
        if (matrix[0][column] == the_operator_playing[operator] and
            matrix[1][column] == the_operator_playing[operator] and
            matrix[2][column] == the_operator_playing[operator]):
            return True

    if (matrix[0][0] == the_operator_playing[operator] and
        matrix[1][1] == the_operator_playing[operator] and
        matrix[2][2] == the_operator_playing[operator]):
        return True

    if (matrix[0][2] == the_operator_playing[operator] and
        matrix[1][1] == the_operator_playing[operator] and
        matrix[2][0] == the_operator_playing[operator]):
        return True

    return False



def board_is_full(matrix):
    for row in matrix:
        if ' ' in row:
            return False

    return True


def continue_to_play():
    while True:
        answer = input("Want to play more (y/n): ").lower()

        if answer == 'y':
            return True

        if answer == 'n':
            return False

        print("Please enter y or n.")

#main
user_wins = 0
computer_wins = 0

the_operator_playing = {
    'x': '✖',
    'o': '⭕'
}


while True:

    matrix = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    user_operator = user_choice_operator()
    computer_operator = computer_choice_operator(user_operator)

    while True:
        #user
        user_row, user_column = user_choice_position()

        if place_is_taken(user_row, user_column, matrix):
            print("You cannot use a place that is already taken!")
            continue

        matrix[user_row][user_column] = the_operator_playing[user_operator]

        display_matrix(matrix)

        time.sleep(0.7)

        if the_winner(matrix, user_operator):
            print("You are the winner!")
            user_wins += 1
            break

        if board_is_full(matrix):
            print("Tie")
            break
        
         #computer
        print("Computer is thinking...")
        
        time.sleep(1)
        
        computer_row, computer_column = computer_choice_position(matrix)
        
        print(
        f"Computer chose: "
        f"row {computer_row + 1}, "
        f"column {computer_column + 1}"
            )
        
        time.sleep(0.5)
        
        matrix[computer_row][computer_column] = the_operator_playing[computer_operator]
        
        display_matrix(matrix)
        
        time.sleep(0.5)

        if the_winner(matrix, computer_operator):
            print("Computer is the winner!")
            computer_wins += 1
            break

        if board_is_full(matrix):
            print("Tie")
            break
        

    print(f"You: {user_wins} | Computer: {computer_wins}")

    if not continue_to_play():
        print("Thanks for playing! 👋")
        break