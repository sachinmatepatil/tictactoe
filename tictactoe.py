# Here’s the structure we’ll follow:
#
# Display the board: We’ll create a function to display the 3x3 grid.
# Player input: Players should be able to choose where to place their mark.
# Win condition check: We’ll check if any player has won.
# Tie condition: We’ll check if the game ends in a tie.
# Main game loop: This will loop until the game is either won or tied.


# Initialize the board (3*3 grid with empty spaces)
board = [" " for _ in range(9)]

# Function to display the board
def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")


#Function to handle player input and making the board
def player_input(player):
    while True:
        try:
            #Ask the player for a position(1-9)
            position = int(input(f"Player {player}, enter your move(1-9):")) - 1
            if position in range(9) and board[position] == " ":
                board[position] = player
                break
            else:
                print("Invalid move, try again")
        except ValueError:
            print("Please enter a number between 1 and 9 ")

#Function to check if a player has won
def check_win(player):
    #Winning combinations(rows, coloumns, diagonals)
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], #Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], #Columns
        [0, 4, 8], [2, 4, 6]             #Diagonals
    ]

    #check if anu win combinations is satisfied
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

#Function to check tie
def check_tie():
    return " " not in board

#Main game loop

def play_game():
    current_player = "X"
    while True:
        display_board() #Show the board
        player_input(current_player) #Ask the current player for move

        # check for win or tie
        if check_win(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break
        elif check_tie():
            display_board()
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = "0" if current_player == "X" else "X"

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe")
    play_game()

