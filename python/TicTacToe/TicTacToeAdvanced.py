""" Tic-Tac-Toe Advanced

This program is a two-player game of Tic-Tac-Toe.
It is a good introduction to lists and loops.

Key differences between this program and its simple counterpart are the fact that
the board is stored as a 1-dimensional list instead of two, and we loop through
all the rows and columns when checking for a winner instead of hardcoding each one.
"""

def checkWin(board):
    """ Checks to see if the game is over and who won

    Args:
        board (list): A list with 9 string elements. Should be comprised of one-digit integers (as strings), 'X', and 'O'

    Returns:
        Will return 'X' or 'O' according to which player won (if a player won), or False if the game is not over
    """

    # Check for a winner across any of the rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2]:
            return board[i]

    # Check for a winner across any of the columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6]:
            return board[i]

    # Check for a winner across the top-left to bottom-right diagonal
    if board[0] == board[4] == board[8]:
        return board[0]

    # Check for a winner across the top-right to bottom-left diagonal
    if board[2] == board[4] == board[6]:
        return board[2]

    # If we haven't found a winner yet, the game is not over
    return False


def printBoard(board):
    """ Prints the board in a pretty format

    Args:
        board (list): A list with 9 string elements. Should be comprised of one-digit integers (as strings), 'X', and 'O'
    """

    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]}')


if __name__ == '__main__':
    # Initialize the board with numbers so the user can input where they want to move easily
    board = ['0', '1', '2',
             '3', '4', '5',
             '6', '7', '8']

    # Variable to keep track of whose turn it is
    currentTurn = 'X'

    # Game loop
    while True:
        # Print the board once per turn
        printBoard(board)

        # Get user input, and keep requesting input until they input a valid response
        while True:
            ipt = input(f'{currentTurn}, Enter a number: ')
            if ipt in board and ipt not in ['X', 'O']:
                # Once the user inputs a valid response, change the board at that location, then break out of the input loop
                board[int(ipt)] = currentTurn
                break
            print('Invalid input')

        # Check if the game is over and store the winner
        winner = checkWin(board)

        # 'X' and 'O' have a decimal ASCII value of 88 and 79, respectively
        # Python treates all nonzero integers as True and 0 as False
        # The `winner` variable has 3 possible values:
        #   'X' (which resolves to True)
        #   'O' (which resolves to True)
        #   False (which... well... is False)
        # That's why this `if winner:` line works
        # If there's a winner, regardless of who it is, the condition `winner` resolves to True
        # If there's not a winner, `winner` contains False, so the end game code doesn't run
        if winner:
            # Since there's a winner, print it out and break out of the game loop
            print(f'{winner} wins!')
            break

        # At the end of the turn, switch who's turn it is
        # This line uses something called a ternary operator
        # You can read about them more here: https://book.pythontips.com/en/latest/ternary_operators.html
        # Basically this line equates to this:
        # currentTurn = None
        # if currentTurn == 'X':
        #     currentTurn = 'O'
        # else:
        #     currentTurn = 'X'
        currentTurn = 'O' if currentTurn == 'X' else 'X'
