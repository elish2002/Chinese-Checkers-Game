from piece import Piece


class Slot:
    def __init__(self, is_in_board: bool, location: tuple,
                 piece: Piece = None) -> None:
        """
            A constructor for a Slot object.
            :param is_in_board: A boolean representing whether the slot is in
             the board of the game.
            :param location: A tuple representing the location of the slot.
            :param piece: A Piece object representing the piece in the slot.
            """
        self.piece = piece
        self.__in_board = is_in_board
        self.__location = location

    def is_in_board(self) -> bool:
        return self.__in_board

    def place_piece(self, piece: Piece) -> None:
        self.piece = piece

    def get_location(self) -> tuple[int, int]:
        return self.__location

    def get_location_left_slot(self) -> tuple[int, int]:
        row = self.__location[0]
        column = self.__location[1] - 2
        return row, column

    def get_location_right_slot(self) -> tuple[int, int]:
        row = self.__location[0]
        column = self.__location[1] + 2
        return row, column

    def get_location_up_right_slot(self) -> tuple[int, int]:
        row = self.__location[0] - 1
        column = self.__location[1] + 1
        return row, column

    def get_location_up_left_slot(self) -> tuple[int, int]:
        row = self.__location[0] - 1
        column = self.__location[1] - 1
        return row, column

    def get_location_down_right_slot(self) -> tuple[int, int]:
        row = self.__location[0] + 1
        column = self.__location[1] + 1
        return row, column

    def get_location_down_left_slot(self) -> tuple[int, int]:
        row = self.__location[0] + 1
        column = self.__location[1] - 1
        return row, column
