"""Exercise 5.12-5-16. TicTacToe."""
def get_game_state(board: list) -> str:
    """Check if a player has won the game, if it's a draw, or if it's ongoing.

    :param board: List of lists of strings representing the game board.
    :return: A string which is 'X' if player 'X' won, 'O' if player 'O' has won, 'Draw' if the game is a draw, or '-' if the game is ongoing.
    """
    game_state = ''
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][2] != '-':
            game_state = board[i][0]
        
        elif board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[2][i] != '-':
            game_state = board[0][i]
    
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[2][2] != '-':
        game_state = board[0][0]
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != '-':
        game_state = board[2][0]
    
    if game_state == '':
        if '-' in board[0] or '-' in board[1] or '-' in board[2]:
            game_state = '-'
        else:
            game_state = 'Draw'
    
    return game_state
        


def update_board(board : list, player: str, position: list) -> list:
    """Update the game board with the player's move.

    :param board: List of lists of strings representing the game board.
    :param player: Player making the move ('X' or 'O').
    :param position: List containing two integer indices [row, column] indicating the position to make a move.
    :return: Updated game board after the move.
    """        
    if board[position[0]][position[1]] == '-':
        board[position[0]][position[1]] = player
    else:
        print('Invalid move!')
    
    return board

def print_board(board: list):
    """Print the current state of the game board.
    
    :param board: List of lists of strings representing the game board.
    """
    for i in range(3):
        print(board[i][0] + board[i][1] + board[i][2]) 

def tictactoe(board: list, player: str, position: list) -> list:

    board = update_board(board, player, position)
    print_board(board)

    game_state = get_game_state(board)
    if game_state == "X":
        print('Player X won!')
    
    elif game_state == "O":
        print('Player O won!')
    
    return board

tictactoe([['X','X','-'],['-','O','-'],['O','-','-']],'O',[0,2])