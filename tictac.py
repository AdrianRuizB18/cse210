# W02 tictactoe - made by Adrián Ruiz on January 2022

def main():
    positions = [1,2,3,4,5,6,7,8,9]
    game_running = finish_game(positions)

    print("Let's play Tic-Tac-Toe!")
    print("")
    print_board(positions)
    print("")


    positions = x_input(positions)
    print("")
    print_board(positions)
    print("")
    positions = o_input(positions)
    print("")
    print_board(positions)

def print_board(positions):
    #Prints the board in its current state
    #Parameters: An array with the positions on the board

    print(f"{positions[0]}|{positions[1]}|{positions[2]}")
    print("-+-+-")
    print(f"{positions[3]}|{positions[4]}|{positions[5]}")
    print("-+-+-")
    print(f"{positions[6]}|{positions[7]}|{positions[8]}")

def x_input(positions):
    #Processes where the player with the X puts his symbol
    x_play = int(input("x's turn to choose a square (1-9): ")) - 1
    positions[x_play] = "X"
    return positions

def o_input(positions):
    #Processes where the player with the O puts his symbol
    o_play = int(input("o's turn to choose a square (1-9): ")) - 1
    positions[o_play] = "O"
    return positions

def finish_game(positions):
    pass



# Start this program by
# calling the main function.
main()
