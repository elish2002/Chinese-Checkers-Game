from game import Game
import sys

def main() -> None:
    try:
        if sys.argv[1] == "--help":
            print("this is a game called CHINESE CHECKERS \n"
                  "the game is played by 2 to 6 players,each player has a color and a name \n"
                  "the goal of the game is to move all your pieces to the opposite side of the board \n"
                  "the board has 6 starting locations, each location has 4 rows each player has 10 pieces \n"
                  "each player can move one piece at a time, to an empty slot. \n"
                  "each piece can move one step in any direction, or jump over a piece to an empty slot"
                  "it can only jump over one piece at a time, and can make multiple jumps in one turn. \n"
                  "every turn the player has to write the location of the piece they want to move"
                  "and the location they want to move it to by writing the row and the column of the piece ( row, column). \n"
                  "the player can also write ! to quit the game at any time. \n"
                  "the player can also decide to continue from the previous game if it hasn't ended"
                  "by writing the name of the file that contains the previous game. \n"
                  "the player can also write --help to get information about the game. \n"
                  "the game ends when one player moves all their pieces to the opposite side of the board. \n")
            return
    except IndexError:
        print("welcome to the game of chinese checkers")
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
























