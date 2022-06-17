# 2048 back-end
"""
Progress Board;

Spring '22 => took ics 31, coded ICS31_2048 (given an initial framework)
Summer '22 => 
# note: keyboard module requires admin privilage on mac (not useful)
"""


import copy
import random


# Global Variables
version = "summer2022"
#version = "ics31"


def print_board(game_board: [[int, ], ]) -> None:
    """
    Print a formatted version of the game board.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    """
    for row in game_board:
        print("+----+" * 4)
        print(''.join(f"|{cell if cell else '':^4}|" for cell in row))
        print("+----+" * 4)


def generate_piece(game_board: [[int, ], ], user_input=False) -> {str: int, }:
    """
    Generates a value and coordinates for the next number to be placed on the board.
    Will raise error if the provided board is full.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :param user_input: specifies type of piece generation: random or user-specified
    :return: dictionary with the following keys: {'row': int, 'column': int, 'value': int}
    """
    empty_cells = [(y, x) for y, row in enumerate(game_board) for x, cell in enumerate(row) if not cell]
    if not empty_cells:
        raise Exception("Board Full")
    if user_input:
        return dict(zip(('column', 'row',  'value'), (int(i) for i in input("column,row,value:").split(','))))
    return dict(
        zip(('row', 'column', 'value'), (*random.choice(empty_cells), (2 if random.random() * 100 < 90 else 4))))


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    # generate 2 random pieces and locations using the generate_piece function
    # place the piece at the specified location
    for i in range(2):
        # Note: generate_piece function is within the computer_move function
        row, col, val = computer_move(game_board)
    print_board(game_board)



    # Initialize game state trackers
    user_input = input()
    winners_mode = 0
    
    if version == "ics31":
        valid_inputs = ["w", "a", "s", "d", "q"]
    if version == "summer2022":
        # arrow keys follow wasd placement (ex. w = \x1b[A)
        valid_inputs = ["w", "a", "s", "d", "\x1b[A", "\x1b[D", "\x1b[B", "\x1b[C", "q"]


    
    # Game Loop
    while True:
        if user_input in valid_inputs:
            if user_input == 'q':
                # if the user quits the game, print Goodbye and stop the Game Loop
                print("Goodbye")
                break
            else:
                # convert arrow keys -> wasd (preserve code)
                if version == "summer2022":
                    if user_input[0:2] == "\x1b[":
                        for i in range(4):
                            # assigment of arrow key value to wasd value
                            if user_input[2] == valid_inputs[i + 4][2]:
                                user_input = valid_inputs[i]
                                break
                
                # Check if board position changed
                if check_board_moved(game_board, user_input) == False:
                    print("Board hasn't changed. Please enter another move...")
                    user_input = input()
                    continue
                # else, execute the user's move
                game_board = move_board(game_board, user_input)
                # Check if the user wins
                if check_user_win(game_board) and winners_mode == 0:
                    print_board(game_board)
                    print("Congratulations! You have won 2048!")
                    z = 1
                    while z:
                        end_game_input = input("Would you like to continue playing? (Enter yes or no) ")
                        if end_game_input == 'yes':
                            print("you have chosen to continue, Please enter a move...")
                            user_input = input()
                            z = 0
                        elif end_game_input == 'no':
                            user_input = 'q'
                            z = 0
                        else:
                            print("Please enter a proper choice")
                    winners_mode = 1
                    continue
                # place a random piece on the board
                row, col, val = computer_move(game_board)
                # check to see if the game is over using the game_over function
                if game_over(game_board):
                    print("Game Over! You have lost!")
                    user_input = 'q'
                    continue
                # show updated board using the print_board function
                print_board(game_board)
                # take user's turn
                user_input = input()
        else:
            # take input until the user's move is a valid key
            print("bro, invalid input! please try again...")
            user_input = input()
    return game_board


def computer_move(game_board: [[int, ], ]) -> None:
    """
    Make Computer Move

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    """
    dict_piece = generate_piece(game_board)
    computer_row = dict_piece["row"]
    computer_col = dict_piece["column"]
    computer_val = dict_piece["value"]
    game_board[computer_row][computer_col] = computer_val

    return (computer_row, computer_col, computer_val)

def move_board(game_board: [[int, ], ], direction: str) -> [[int, ], ]:
    """
    Move Game Board to indicated direction
    
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :param direction: specified direction given by user_input
    """
    if direction == 'w':
        # going up is the same as going left in this new form
        # Created a transformed matrix
        new_game_board = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                new_game_board[i].append(game_board[j][i])
        # Copied over 'a' functionality
        for row in new_game_board:
            for index in range(4):
                for i in range(4 - index):
                    if row[index] == 0:
                        row.pop(index)
                        row.insert(3, 0)
            for index in range(3):
                if index < 4 and row[index] == row[index + 1]:
                    removed_value = row.pop(index + 1)
                    row.insert(3, 0)
                    row[index] += removed_value
        # Transformed matrix again back to original form
        updated_game_board = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                updated_game_board[i].append(new_game_board[j][i])
        game_board = updated_game_board
        return game_board
    if direction == 'a':
        for row in game_board:
            for index in range(4):
                for i in range(4 - index):
                    if row[index] == 0:
                        row.pop(index)
                        row.insert(3, 0)
            for index in range(3):
                if index < 4 and row[index] == row[index + 1]:
                    removed_value = row.pop(index + 1)
                    row.insert(3, 0)
                    row[index] += removed_value
        return game_board
    if direction == 's':
        # going down is the same as going right in this new form
        # Created a transformed matrix
        new_game_board = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                new_game_board[i].append(game_board[j][i])
        # Copied over 'd' functionality
        for row in new_game_board:
            # move all 0's to the left side
            for index in range(3, -1, -1):
                for i in range(index):
                    if row[index] == 0:
                        row.pop(index)
                        row.insert(0, 0)
            # add elements together if needed, making sure not to add if already added 
            # Ex. [0, 2, 2, 4] != [0, 0, 0, 8], rather: [0, 0, 4, 4]
            for index in range(3, 0, -1):
                if index > 0 and row[index] == row[index - 1]:
                    removed_value = row.pop(index - 1)
                    row.insert(0, 0)
                    row[index] += removed_value
        # Transformed matrix again back to original form
        updated_game_board = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                updated_game_board[i].append(new_game_board[j][i])
        game_board = updated_game_board
        return game_board
    if direction == 'd':
        for row in game_board:
            # move all 0's to the left side
            for index in range(3, -1, -1):
                for i in range(index):
                    if row[index] == 0:
                        row.pop(index)
                        row.insert(0, 0)
            # add elements together if needed, making sure not to add if already added 
            # Ex. [0, 2, 2, 4] != [0, 0, 0, 8], rather: [0, 0, 4, 4]
            for index in range(3, 0, -1):
                if index > 0 and row[index] == row[index - 1]:
                    removed_value = row.pop(index - 1)
                    row.insert(0, 0)
                    row[index] += removed_value
        return game_board


def check_user_win(game_board: [[int, ], ]) -> bool:
    """
    Check if User has won (1024)
    
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if user has won (True) or not (False)
    """
    for row in game_board:
        for col in row:
            if col  == 2048:
                return True
    return False


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # check if board is full
    #       if (full), continue on to next check; 
    #       else, there is still a move to be made (return False)
    for row in game_board:
        for col in row:
            if col == 0:
                return False
    # if (full), check if any valid moves remain
    valid_moves = ['w', 'a', 's', 'd']
    for move in valid_moves:
        if check_board_moved(game_board, move):
            # game not over, valid move exists
            return False
    # game over, no possible moves remain
    return True


def check_board_moved(game_board: [[int, ], ], user_input) -> bool:
    """
    Check if board position has changed
    
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :param user_input: a string of user's input
    :return: Boolean indicating if the board has changed (True) or not (False)
    """
    old_board = game_board
    possible_board = move_board(copy.deepcopy(game_board), user_input)
    if old_board == possible_board:
        return False
    return True

if __name__ == "__main__":
    print("hello user!")
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])

