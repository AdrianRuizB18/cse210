# W02 tictactoe - made by Adrián Ruiz on January 2022

def main():
    positions = [1,2,3,4,5,6,7,8,9]
    game_running = finish_game(positions)

    print("Let's play Tic-Tac-Toe!")
    print("")
    print_board(positions)
    print("")

    while game_running:
        positions = x_input(positions)
        print("")
        print_board(positions)        
        print("")
        game_running = finish_game(positions)
        print("")
        if game_running == False:
            break
        positions = o_input(positions)
        print("")
        print_board(positions)
        print("")
        game_running = finish_game(positions)

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
   
    while positions[x_play] == "X" or positions[x_play] == "O":
        x_play = int(input("that square is already occupied, try a different one (1-9): ")) - 1
    
    positions[x_play] = "X"

    return positions

def o_input(positions):
    #Processes where the player with the O puts his symbol
    o_play = int(input("o's turn to choose a square (1-9): ")) - 1
    
    while positions[o_play] == "X" or positions[o_play] == "O":
        o_play = int(input("that square is already occupied, try a different one (1-9): ")) - 1
    
    positions[o_play] = "O"

    return positions


def finish_game(positions):
    #this function handles the actual game logic, if the game should continue, or if it finished in a draw/win
    run_game = True

    #Check if "X" won
    if positions[0] == "X" and positions[1] == "X" and positions[2] == "X":
        print("X wins! Thanks for playing")
        run_game = False
    
    elif positions[3] == "X" and positions[4] == "X" and positions[5] == "X":
        print("X wins! Thanks for playing")
        run_game = False
    
    elif positions[6] == "X" and positions[7] == "X" and positions[8] == "X":
        print("X wins! Thanks for playing")
        run_game = False

    elif positions[0] == "X" and positions[3] == "X" and positions[6] == "X":
        print("X wins! Thanks for playing")
        run_game = False

    elif positions[1] == "X" and positions[4] == "X" and positions[7] == "X":
        print("X wins! Thanks for playing")
        run_game = False
    
    elif positions[2] == "X" and positions[5] == "X" and positions[8] == "X":
        print("X wins! Thanks for playing")
        run_game = False
    
    elif positions[0] == "X" and positions[4] == "X" and positions[8] == "X":
        print("X wins! Thanks for playing")
        run_game = False
    
    elif positions[2] == "X" and positions[4] == "X" and positions[6] == "X":
        print("X wins! Thanks for playing")
        run_game = False

    

    #Check if "O" won.
    elif positions[0] == "O" and positions[1] == "O" and positions[2] == "O":
        print("O wins! Thanks for playing")
        run_game = False

    elif positions[3] == "O" and positions[4] == "O" and positions[5] == "O":
        print("O wins! Thanks for playing")
        run_game = False
    
    elif positions[6] == "O" and positions[7] == "O" and positions[8] == "O":
        print("O wins! Thanks for playing")
        run_game = False

    elif positions[0] == "O" and positions[3] == "O" and positions[6] == "O":
        print("O wins! Thanks for playing")
        run_game = False

    elif positions[1] == "O" and positions[4] == "O" and positions[7] == "O":
        print("O wins! Thanks for playing")
        run_game = False
    
    elif positions[2] == "O" and positions[5] == "O" and positions[8] == "O":
        print("O wins! Thanks for playing")
        run_game = False
    
    elif positions[0] == "O" and positions[4] == "O" and positions[8] == "O":
        print("O wins! Thanks for playing")
        run_game = False
    
    elif positions[2] == "O" and positions[4] == "O" and positions[6] == "O":
        print("O wins! Thanks for playing")
        run_game = False

    #Check for draw.    
    elif all(isinstance(x, str) for x in positions) == True:
        print("Draw! Thanks for Playing")
        run_game = False
    #Continue running the game if no complete state is triggered
    else:
        run_game = True

    return run_game

# Start this program by
# calling the main function.
main()
