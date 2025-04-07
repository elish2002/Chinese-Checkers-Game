from player import Player
from typing import Union
from slot import Slot
from constants import COLORS, ROWS, COLS, BOARD_SLOTS, FIRST_LOC_OF_INIT, INIT_ROWS
from piece import Piece
from termcolor import colored


class Board:
    def __init__(self) -> None:
        """
        A constructor for a Board object.
        this function initializes the board of the game
        """
        init_board = self.create_board()
        self.__grid = init_board
        self.players = []
        self.first_location = {}

    def create_board(self) -> list[list[Slot]]:
        """creates the initial board of the game"""
        init_board = []
        for row in range(ROWS):
            init_board.append([])
            slot = 0
            for column in range(0, COLS):
                if ((COLS - 2 * BOARD_SLOTS[row]) / 2) + (slot * 2) == column:
                    init_board[row].append(Slot(True, (row, column)))
                    if slot < BOARD_SLOTS[row] - 1:
                        slot += 1
                else:
                    init_board[row].append(Slot(False, (row, column)))
        return init_board

    def get_slot(self, location: tuple) -> Slot:
        """
        This function returns the slot in the location provided
        :return: Slot object.
        """
        return self.__grid[location[0]][location[1]]

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string representing the current status of the board.
        """
        view = ""
        for index, row in enumerate(self.__grid):
            if index == 0:
                view += "   "
                for num in range(COLS):
                    if num < 10:
                        view += f"{num}  "
                    else:
                        view += f"{num} "
                view += "\n"
            for index2, column in enumerate(row):
                if index2 == 0:
                    view += f"{index} "
                    if index < 10:
                        view += " "
                if not column.is_in_board():
                    view += "   "
                elif column.piece is not None:
                    color = COLORS[column.piece.color]
                    view += colored(column.piece.color[0].upper(), color, attrs=['bold', 'underline'])
                    view += "  "
                else:
                    view += colored("O  ", 'white')
            view += "\n"
        return view

    def get_direction_options(self, slot: Slot) -> list[Slot]:
        """
        this function returns the direction options of the slot
        the order of the returned list is necessary for the get_possible_moves
        function
        """
        direction_options = []
        options = [slot.get_location_left_slot(),
                   slot.get_location_right_slot(),
                   slot.get_location_up_right_slot(),
                   slot.get_location_up_left_slot(),
                   slot.get_location_down_right_slot(),
                   slot.get_location_down_left_slot()]
        for option in options:
            if not 0 <= option[0] < ROWS or not 0 <= option[1] < COLS:
                direction_options.append(None)
            elif not self.__grid[option[0]][option[1]].is_in_board():
                direction_options.append(None)
            else:
                direction_options.append(self.__grid[option[0]][option[1]])
        return direction_options

    def next_is_free(self, direction_slot: Slot, option: int) -> bool:
        """
        this function checks if the next slot is free
        """
        get_next = [direction_slot.get_location_left_slot(),
                    direction_slot.get_location_right_slot(),
                    direction_slot.get_location_up_right_slot(),
                    direction_slot.get_location_up_left_slot(),
                    direction_slot.get_location_down_right_slot(),
                    direction_slot.get_location_down_left_slot()]
        if get_next[option][0] < 0 or get_next[option][1] < 0:
            return False
        if get_next[option][0] >= ROWS or get_next[option][1] >= COLS:
            return False
        place = self.__grid[get_next[option][0]][get_next[option][1]]
        if place.is_in_board():
            if place.piece is None:
                return True
        return False

    def get_possible_moves(self, slot: Slot) -> set:
        possible_moves = set()
        direction_options = self.get_direction_options(slot)
        for option, direction_slot in enumerate(direction_options):
            if direction_slot is not None:
                prev_places = set()
                if direction_slot.piece is None:
                    possible_moves.add(direction_slot.get_location())
                elif self.next_is_free(direction_slot, option):
                    next_slot = self.get_direction_options(direction_slot)[option]
                    prev_places.add(next_slot.get_location())
                    possible_moves.add(next_slot.get_location())
                    result = self.get_possible_moves_recursion(next_slot, prev_places, possible_moves)
                    possible_moves.update(result)
        return possible_moves

    def get_possible_moves_recursion(self, slot: Slot, prev_places=None, moves=None) -> set:
        """
        This function returns the legal moves of all cars in this board.
        :return: list of tuples of the form (name, move_key, description)
                 representing legal moves. The description should briefly
                 explain what is the movement represented by move_key.
        """
        if prev_places is None:
            prev_places = set()
        if moves is None:
            moves = set()
        possible_moves = moves.copy()
        direction_options = self.get_direction_options(slot)
        for index, direction_slot in enumerate(direction_options):
            if direction_slot is not None:
                if direction_slot.get_location() not in prev_places:
                    if direction_slot.piece is None:
                        if not prev_places:
                            possible_moves.add(direction_slot.get_location())
                    elif self.next_is_free(direction_slot, index):
                        next_slot = self.get_direction_options(direction_slot)[index]
                        possible_moves.add(next_slot.get_location())
                        prev_places.add(direction_slot.get_location())
                        prev_places.add(next_slot.get_location())
                        result = self.get_possible_moves_recursion(next_slot, prev_places, possible_moves)
                        possible_moves.update(result)
        return possible_moves

    def target_locations(self, player: Player) -> list[tuple]:
        """
        This function returns the coordinates of the location that should be
        filled for victory.
        :return: (row, col) of the goal location.
        """
        target_lst = []
        first_loc = self.first_location[player.get_name()]
        for index, loc in enumerate(FIRST_LOC_OF_INIT):
            if loc == first_loc:
                if index % 2 == 0:
                    loc = FIRST_LOC_OF_INIT[index + 1]
                    start_column = 0
                    for row in range(loc[0], loc[0] - INIT_ROWS, -1):
                        start = loc[1] - start_column
                        stop = loc[1] + start_column + 1
                        for column in range(start, stop):
                            if self.__grid[row][column].is_in_board():
                                target_lst.append((row, column))
                        start_column += 1
                else:
                    loc = FIRST_LOC_OF_INIT[index - 1]
                    start_column = 0
                    for row in range(loc[0], loc[0] + INIT_ROWS):
                        start = loc[1] - start_column
                        stop = loc[1] + start_column + 1
                        for column in range(start, stop):
                            if self.__grid[row][column].is_in_board():
                                target_lst.append((row, column))
                        start_column += 1
        return target_lst

    def cell_content(self, coordinates: tuple) -> Union[str, None]:
        cords_loc = self.__grid[coordinates[0]][coordinates[1]].piece
        if cords_loc is None:
            return None
        else:
            return cords_loc.color

    def start_location(self, player: Player, location: tuple) -> None:
        self.first_location[player.get_name()] = location

    def init_place_taken(self, index_place: int, first_location: tuple) -> bool:
        """
        this function checks if the place is taken
        """
        row1 = first_location[0]
        column1 = first_location[1]
        is_taken = False
        if self.get_slot(first_location).piece is None:
            if index_place % 2 == 0:
                start_column = 0
                for row in range(row1, row1 + INIT_ROWS):
                    start = column1 - start_column
                    stop = column1 + start_column + 1
                    for column in range(start, stop):
                        if self.get_slot((row, column)).is_in_board():
                            if self.get_slot((row, column)).piece is not None:
                                is_taken = True
                                break
                    start_column += 1
            else:
                start_column = 0
                for row in range(row1, row1 - INIT_ROWS, -1):
                    start = column1 - start_column
                    stop = column1 + start_column + 1
                    for column in range(start, stop):
                        if self.get_slot((row, column)).is_in_board():
                            if self.get_slot((row, column)).piece is not None:
                                is_taken = True
                                break
                    start_column += 1
        else:
            is_taken = True
        return is_taken

    def add_player(self, player: Player) -> bool:
        """
        this function adds a player to the board and to the list of players
        """
        for index_place, first_location in enumerate(FIRST_LOC_OF_INIT):
            # goes through all the places to put the player piece
            row1 = first_location[0]
            column1 = first_location[1]
            if self.init_place_taken(index_place, first_location):
                continue
            else:
                if index_place % 2 == 0:
                    start_column = 0
                    for row in range(row1, row1 + INIT_ROWS):
                        start = column1 - start_column
                        stop = column1 + start_column + 1
                        for column in range(start, stop):
                            if self.get_slot((row, column)).is_in_board():
                                color = player.get_color()
                                piece = Piece(color, (row, column))
                                self.__grid[row][column].piece = piece
                        start_column += 1
                else:
                    start_column = 0
                    for row in range(row1, row1 - INIT_ROWS, -1):
                        start = column1 - start_column
                        stop = column1 + start_column + 1
                        for column in range(start, stop):
                            if self.get_slot((row, column)).is_in_board():
                                color = player.get_color()
                                piece = Piece(color, (row, column))
                                self.__grid[row][column].piece = piece
                        start_column += 1
                self.start_location(player, first_location)
                return True
        return False

    def is_in_range(self, place_loc: tuple) -> bool:
        """
        this function checks that the location the player provided is in range
         of the board
         """
        if self.__grid[place_loc[0]][place_loc[1]].is_in_board():
            return True
        return False

    def move_piece(self, piece: Piece, move_loc: tuple) -> None:
        """
        this function moves the piece to the new location
        :param piece:
        :param move_loc:
        """
        self.__grid[piece.location[0]][piece.location[1]].piece = None
        self.__grid[move_loc[0]][move_loc[1]].piece = piece
        piece.move(move_loc)

    def get_all_pieces_slots(self, color: str) -> list[Slot]:
        """this function returns all the pieces of a certain color on the board
        """
        slots_with_pieces = []
        for row in self.__grid:
            for slot in row:
                if slot.piece is not None:
                    if slot.piece.color == color:
                        slots_with_pieces.append(slot)
        return slots_with_pieces



