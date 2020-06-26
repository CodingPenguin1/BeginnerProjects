""" Tic-Tac-Toe Simple

This program is a two-player game of Tic-Tac-Toe.
It is a good introduction to lists and loops.

This program uses basic logic and conditions, which is great for beginners.
The structure of this program is nearly identical to that of the advanced program, but the functions are coded a little more intuitively
"""

def checkWin(board):
    """ Checks to see if the game is over and who won

    Args:
        board (list): A list with 9 string elements. Should be comprised of one-digit integers (as strings), 'X', and 'O'

    Returns:
        Will return 'X' or 'O' according to which player won (if a player won), or False if the game is not over
    """

    # Check for a winner across any of the rows
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]

    # Check for a winner across any of the columns
    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]

    # Check for a winner across the top-left to bottom-right diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    # Check for a winner across the top-right to bottom-left diagonal
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    # If we haven't found a winner yet, the game is not over
    return False


def printBoard(board):
    """ Prints the board in a pretty format

    Args:
        board (list): A list with 9 string elements. Should be comprised of one-digit integers (as strings), 'X', and 'O'
    """

    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print('---+---+---')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('---+---+---')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]}')


if __name__ == '__main__':
    # Initialize the board with numbers so the user can input where they want to move easily
    board = [['0', '1', '2'],
             ['3', '4', '5'],
             ['6', '7', '8']]

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
                ipt = int(ipt)

                # These two lines translate from a single integer to row/columns
                row = ipt // 3
                col = ipt % 3

                # Make the move, then exit the input loop
                board[row][col] = currentTurn
                break

            print('Invalid input')

        # Check if the game is over and store the winner
        winner = checkWin(board)

        # If checkWin returns an 'X' or 'O', print the winner and exit the game loop
        if winner == 'X' or winner == 'O':
            print(f'{winner} wins!')
            break
        # Otherwise switch whose turn it is
        else:
            if currentTurn == 'X':
                currentTurn = 'O'
            else:
                currentTurn = 'X'
