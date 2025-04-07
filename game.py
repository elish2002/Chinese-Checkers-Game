from typing import Union
from player import Player
from board import Board
from constants import NUM_PLAYERS, ROWS, COLS, OPTIONAL_COLORS
import random
import datetime
import os

class Game:
    """
    the class represents a game object.
    chinese checkers game. in this game the player needs to move his pieces
    from one side of the board to the other side of the board. the player
    can move his pieces in 6 different directions and the player can only
    move one piece at a time. the player can also jump over other pieces
    to get to the other side of the board. the player can also move his
    pieces in any direction he wants to. the player can also play with
    other players or against the computer.
    """

    def __init__(self) -> None:
        """
        Initialize a new Game object.
        """
        self.board = Board()
        self.turn = 0
        self.valid_moves = set()

    def reset(self) -> None:
        """
        resets the game.
        """
        self.board = Board()
        self.turn = 0

    def change_turn(self) -> None:
        """
        changes the turn.
        """
        for index in range(len(self.board.players)):
            if index == self.turn:
                if index == len(self.board.players) - 1:
                    self.turn = 0
                else:
                    self.turn = index + 1

    def name_is_in_board(self, name: str) -> bool:
        """
        checks if the name of the player is already in the board.
        """
        for player in self.board.players:
            if player.get_name() == name:
                return True
        return False

    def color_is_in_board(self, color: str) -> bool:
        """
        checks if the color of the player is already in the board.
        """
        for player in self.board.players:
            if player.get_color() == color:
                return True
        return False

    def get_num_total_players(self) -> int:
        """
        :return: the number of players in the game.
        """
        number_of_player = input("enter the number of players you want"
                                 " to add to the game: ")
        while number_of_player not in NUM_PLAYERS:
            number_of_player = input(f"not valid enter again"
                                     f" out of {NUM_PLAYERS}: ")
        return int(number_of_player)

    def get_num_computer_players(self, num_players: int) -> int:
        """
        :return: the number of computer players in the game.
        """
        number_of_computer = input("enter the number of computer"
                                   " players you want have in this game: ")
        valid_num = [str(num) for num in range(num_players)]
        while number_of_computer not in valid_num:
            number_of_computer = input(
                f"enter again, out of {valid_num}: ")
        return int(number_of_computer)

    def is_valid_name(self, name: str) -> bool:
        """
        checks if the name is valid.
        """
        if name == "":
            print("the name can't be empty")
            return False
        if "computer" in name:
            print("the name can't contain the word computer")
            return False
        if "*" in name:
            print("the name can't contain the character '*'")
            return False
        if "+" in name:
            print("the name can't contain the character '+'")
            return False
        for player in self.board.players:
            if player.get_name() == name:
                print("the name is already in the game")
                return False
        space = True
        for char in name:
            if not char.isspace():
                space = False
        if space:
            print("the name can't be only spaces")
            return False
        return True

    def is_valid_color(self, color: str) -> bool:
        """
        checks if the color is valid.
        """
        if color not in OPTIONAL_COLORS:
            print("the color is not valid")
            return False
        if self.color_is_in_board(color):
            print("the color is already in the game")
            return False
        return True

    def add_player_to_list(self, player_num: int) -> None:
        """
        Adds a player to the game.
        :param player_num:
        :return: None
        """
        color = input(
            f"enter the color of the player{player_num + 1} you want to"
            f" add to the game out of {OPTIONAL_COLORS}: ")
        while not self.is_valid_color(color.lower()):
            color = input(
                f"enter a different color for the player{player_num + 1}: ")
        name = input(
            f"enter the name of the player{player_num + 1} you want"
            f" to add to the game: ")
        while not self.is_valid_name(name):
            name = input(
                f"enter a different name for the player{player_num + 1}: ")
        player = Player(name, color.lower())
        self.board.players.append(player)

    def add_computer(self) -> None:
        """
        adds a computer player to the game.
        creates a computer player with a color that is not in the game.
        out of the optional colors.
        """
        options = OPTIONAL_COLORS[:]
        for color in OPTIONAL_COLORS:
            for player in self.board.players:
                if player.get_color() == color:
                    options.remove(color)
        color = options[0]
        name = f"computer{len(self.board.players)}"
        player = Player(name, color)
        self.board.players.append(player)

    def is_valid_row_col_input(self, location: str) -> bool:
        """
        checks if the row and column are valid.
        """
        is_valid = True
        if "!" in location:
            return is_valid
        if "," not in location:
            is_valid = False
            return is_valid
        if location.count(",") > 1:
            is_valid = False
            return is_valid
        if len(location) > 5:
            is_valid = False
            return is_valid
        row, col = location.split(",")
        if not row.isdigit() or not col.isdigit():
            is_valid = False
            return is_valid
        if not (0 <= int(row) < ROWS and 0 <= int(col) < COLS):
            is_valid = False
            return is_valid
        if not self.board.is_in_range((int(row), int(col))):
            is_valid = False
            return is_valid
        return is_valid

    def get_piece_to_move(self, player: Player) -> tuple:
        """
        this function gets the piece the player wants to move.
        """
        piece_to_move = input(
            f"{player.get_name()} enter the location of the piece you want to"
            f" move (row,column): if you want to stop the game enter '!': ")
        while not self.is_valid_row_col_input(piece_to_move):
            piece_to_move = input(
                "you didn't provide the right input (row,column):")
        if "!" in piece_to_move:
            return "!", "!"
        current_row, current_column = piece_to_move.split(",")
        current_row = int(current_row)
        current_column = int(current_column)
        if self.board.is_in_range((current_row, current_column)):
            slot = self.board.get_slot((current_row, current_column))
            if slot.piece is not None:
                if slot.piece.color == player.get_color():
                    if self.board.get_possible_moves(slot):
                        return current_row, current_column
                    else:
                        print("this piece has no possible moves")
                        return self.get_piece_to_move(player)
                else:
                    print("this is not your piece")
                    return self.get_piece_to_move(player)
            else:
                print("this slot is empty")
                return self.get_piece_to_move(player)

    def get_new_place(self, player: Player, current_row: int,
                      current_column: int) -> tuple:
        """
        this function gets the new place the player wants to move the piece to.
        from the player.
        """
        slot = self.board.get_slot((current_row, current_column))
        new_place = input(
            f"Enter target for piece {self.board.get_possible_moves(slot)}:"
            f"if you want to stop the game enter '!': ")
        while not self.is_valid_row_col_input(new_place):
            new_place = input(
                "you didn't provide the right input (row,column):")
        if "!" in new_place:
            return "!", "!"
        new_row, new_column = new_place.split(",")
        new_row = int(new_row)
        new_column = int(new_column)
        if (new_row, new_column) in self.board.get_possible_moves(slot):
            return new_row, new_column
        else:
            print("this is not a valid move")
            return self.get_new_place(player, current_row, current_column)

    def computer_move(self, log_name: str, color: str, player: Player) -> None:
        """
        makes the move for the AI.
        """
        slot = random.choice(self.board.get_all_pieces_slots(color))
        moves = self.board.get_possible_moves(slot)
        while not moves:
            slot = random.choice(self.board.get_all_pieces_slots(color))
            moves = self.board.get_possible_moves(slot)
        move_loc = random.choice(list(moves))
        self.board.move_piece(slot.piece, move_loc)
        self.add_move_to_log(log_name, player, slot.get_location(), move_loc)
        self.change_turn()

    def create_log(self) -> str:
        """
        this function creates a log file.
        """
        name = input("Enter the name of the log file you want to save the game as"
                     "without .txt at the end: ")
        while not name or ".txt" in name or " " in name:
            name = input("Enter a valid name: ")
        with open(f"{name}.txt", "w") as f:
            return name + ".txt"

    def set_game(self)-> str:
        """
        sets the game with the players and the computer players.
        """
        self.reset()
        self.board.players = []
        num_total_players = self.get_num_total_players()
        computer_players = self.get_num_computer_players(num_total_players)
        num_players = num_total_players - computer_players
        log_name = self.create_log()
        for player_num in range(num_players):
            self.add_player_to_list(player_num)
        for computer in range(computer_players):
            self.add_computer()
        for player in self.board.players:
            self.board.add_player(player)
        if log_name:
            self.add_move_to_log(log_name, "new_game")
        return log_name

    def __single_turn(self, log_name: str, player: Player) -> bool:
        """
        this function runs one round of the game
        """
        if "computer" in player.get_name():
            self.computer_move(log_name, player.get_color(), player)
            return True
        print(self.board)
        cur_row, cur_column = self.get_piece_to_move(player)
        if cur_row == "!" and cur_column == "!":
            return False
        new_row, new_column = self.get_new_place(player, cur_row, cur_column)
        if new_row == "!" and new_column == "!":
            return False
        slot = self.board.get_slot((cur_row, cur_column))
        self.board.move_piece(slot.piece, (new_row, new_column))
        self.add_move_to_log(log_name, player, (cur_row, cur_column),
                             (new_row, new_column))
        self.change_turn()
        return True

    def play_one_game(self) -> str:
        """
        The main driver of the Game. Manages the game until completion.
        and returns if the player wants to play again.
        """
        stop_round = False
        winners = []
        continue_game = self.continue_game_from_log()
        if continue_game:
            if not self.load_game_from_log(continue_game):
                continue_game = self.set_game()
        elif not continue_game:
            continue_game = self.set_game()
        while not stop_round:
            for player in self.board.players:
                if not self.__single_turn(continue_game, player):
                    stop_round = True
                    break
                did_win = True
                for location in self.board.target_locations(player):
                    if self.board.cell_content(location) != player.get_color():
                        did_win = False
                        break
                if did_win:
                    winners.append(player.get_name())
                    player.wins = 1
                    stop_round = True
        if winners:
            self.add_move_to_log(continue_game, "game has ended")
            print(f"the winners are {winners}")
            for player in self.board.players:
                if player not in winners:
                    player.loses += 1
        play_again = input("would you like to play again? (y/n): ")
        while play_again.lower() not in ["y", "n"]:
            play_again = input("please enter y or n: ")
        return play_again.lower()

    def play(self) -> None:
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        stop_game = False
        while not stop_game:
            play_again = self.play_one_game()
            if play_again == "n":
                stop_game = True
            elif play_again == "y":
                self.reset()

    def continue_game_from_log(self) -> str:
        """
        checks if the game should continue from the log.
        """
        continue_game = input("would you like to continue the game from"
                              " a previous game? (y/n): ")
        while continue_game.lower() not in ["y", "n"]:
            continue_game = input("please enter y or n: ")
        if continue_game == "y":
            file_name = input("Enter the name of the log file without the ending .txt: ")
            if file_name != "!":
                file_name = file_name + ".txt"
            if file_name == "!":
                return ""
            while not os.path.exists(file_name):
                file_name = input("enter a valid name without .txt , or if you want to start "
                                  "a new game press ! : ")
                if file_name != "!":
                    file_name = file_name + ".txt"
                if file_name == "!":
                    return ""
            return file_name
        return ""

    def add_move_to_log(self, file_name: str, player: Union[Player, str], piece_loc: tuple = None, move: tuple = None) -> None:
        """
        this function adds the move to the log file.
        """
        with open(file_name, 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if player == "new_game":
                f.write(f"{timestamp} + new_game\n")
                return
            if player == "game has ended":
                f.write(f"{timestamp} + game has ended\n")
                return
            f.write(f"{timestamp} + {player.get_name()} * {player.get_color()} * {player.wins} * {player.loses} + {piece_loc} + {move}\n")

    def get_moves_from_log(self, line) -> tuple[Player, tuple, tuple]:
        """
        this function gets the moves from the log file.
        """
        time, player_stats, piece, move = line.split("+")
        name, color, wins, loses = player_stats.split("*")
        color = color.strip()
        name = name.strip()
        player = Player(name, color, int(wins), int(loses))
        row, col = piece.split(",")
        row = int(row[2:])
        col = int(col[1:-2])
        piece_loc = row, col
        move_row, move_col = move.split(",")
        move_row = int(move_row[2:])
        move_col = int(move_col[1:-2])
        move = move_row, move_col
        return player, piece_loc, move

    def load_game_from_log(self, log_file: str) -> bool:
        """
        this function loads the game from the log file.
        """
        continue_from_log = False
        count_lines = 0
        index = -1
        with open(log_file, 'r') as f:
            for line in f:
                count_lines += 1
        with open(log_file, 'r') as f:
            for text in f:
                index += 1
                if "new_game" in text:
                    if count_lines - 1 == index:
                        print("you haven't started a new game yet. starting a new game.")
                        return continue_from_log
                    self.reset()
                elif "game has ended" in text:
                    continue_from_log = False
                else:
                    player, piece_loc, move = self.get_moves_from_log(text)
                    self.board.players.append(player)
                    self.board.add_player(player)
                    self.board.move_piece(
                        self.board.get_slot(piece_loc).piece, move)
                    continue_from_log = True
        if not continue_from_log:
            print("starting a new game.")
        return continue_from_log
