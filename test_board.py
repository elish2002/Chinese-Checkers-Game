import pytest
from board import Board
from player import Player
from piece import Piece

def test_get_direction_options():
    """this function tests the get_direction_options function in the board class
    it checks if the function returns the correct direction options for the player
    and if it doesn't return the correct direction options for the player if the
    player is not in the board or if the player has no possible moves"""
    board = Board()
    player1 = Player("elvis", "RED")
    board.add_player(player1)
    player2 = Player("sara", "BLUE")
    board.add_player(player2)
    assert board.get_direction_options(board.get_slot((0, 0))) == [None, None, None, None, None, None]
    assert board.get_direction_options(board.get_slot((13, 13))) == [board.get_slot((13,11)), board.get_slot((13,15)),
                                                                     board.get_slot((12,14)), board.get_slot((12,12)),
                                                                     board.get_slot((14,14)), board.get_slot((14,12))]
    assert board.get_direction_options(board.get_slot((13, 14))) == [None, None, None, None, None, None]
    assert board.get_direction_options(board.get_slot((16,12))) == [None, None, board.get_slot((15,13)),board.get_slot((15,11)), None, None]
    assert board.get_direction_options(board.get_slot((4,24))) == [board.get_slot((4,22)), None, None, None, None, board.get_slot((5,23))]

def test_next_is_free():
    """this function tests the next_is_free function in the board class
    it checks if the function returns the correct boolean value if the next slot
    is free or not and if it doesn't return the correct boolean value if the next
    slot is not free or if the next slot is not in the board"""
    board = Board()
    player1 = Player("elvis", "RED")
    board.add_player(player1)
    player2 = Player("sara", "BLUE")
    board.add_player(player2)
    assert board.next_is_free(board.get_slot((0, 0)), 0) == False
    assert board.next_is_free(board.get_slot((4, 20)), 0) == True
    assert board.next_is_free(board.get_slot((12,22)), 0) == True
    assert board.next_is_free(board.get_slot((12,22)), 1) == True


def test_move_piece():
    """this function tests the move_piece function in the board class
    it checks if the function moves the piece to the new location"""
    board = Board()
    player1 = Player("elvis", "magenta")
    board.add_player(player1)
    player2 = Player("sara", "red")
    board.add_player(player2)
    board.move_piece(board.get_slot((0, 12)).piece, (1, 12))
    assert board.get_slot((1, 12)).piece.color == "magenta"
    board.move_piece(board.get_slot((1, 12)).piece, (2, 12))
    assert board.get_slot((2, 12)).piece.color == "magenta"
    board.move_piece(board.get_slot((16, 12)).piece, (3, 12))
    assert board.get_slot((3, 12)).piece.color == "red"
    board.move_piece(board.get_slot((3, 12)).piece, (4, 12))
    assert board.get_slot((4, 12)).piece.color == "red"


def test_add_player():
    """this function tests the add_player function in the board class
    it checks if the function adds the player to the board and if it
    doesn't add the player to the board if the player is already in the board
    or if the board is full, or if the player's name is empty, or if the player's
    color is not valid. or if the player's name is already in the board. or if the
    player's color is already in the board."""
    board = Board()
    player1 = Player("elvis", "RED")
    player2 = Player("sara", "BLUE")
    player3 = Player("elvis", "RED")
    player4 = Player("sara", "BLUE")
    player5 = Player("", "RED")
    player6 = Player("el", "")
    player7 = Player("elvis", "pink")
    assert board.add_player(player1)
    assert board.add_player(player2)
    assert board.add_player(player3)
    assert board.add_player(player4)
    assert board.add_player(player5)
    assert board.add_player(player6)
    assert not board.add_player(player7)

def test_target_locations():
    """this function tests the target_locations function in the board class
    it checks if the function returns the target locations of the player in the board
    and if it doesn't return the target locations of a player in the board if the
    player is not in the board or if the player has no possible moves"""
    board = Board()
    player1 = Player("elvis", "red")
    board.add_player(player1)
    player2 = Player("sara", "blue")
    board.add_player(player2)
    assert board.target_locations(player2) == [(0,12), (1,11), (1,13), (2,10), (2,12), (2,14), (3,9), (3,11), (3,13), (3,15)]
    assert board.target_locations(player1) == [(16,12), (15,11), (15,13), (14,10), (14,12), (14,14), (13,9), (13,11), (13,13), (13,15)]

def init_place_taken():
    """"this function tests the place_taken function in the board class
    it checks if the function returns the correct boolean value if the place is taken
    or not and if it doesn't return the correct boolean value if the place is not taken
    """
    board = Board()
    player1 = Player("elvis", "red")
    board.add_player(player1)
    player2 = Player("sara", "blue")
    board.add_player(player2)
    assert board.init_place_taken(0,(0, 12)) == True
    assert board.init_place_taken(1, (16, 12)) == True
    assert board.init_place_taken(2, (9, 21)) == False

def test_possible_moves():
    """this function tests the get_possible_moves function in the board class
    it checks if the function returns the possible moves of a player in the board
    and if it doesn't return the possible moves of a player in the board if the
    player is not in the board or if the player has no possible moves"""
    board = Board()
    player1 = Player("elvis", "RED")
    board.add_player(player1)
    player2 = Player("sara", "BLUE")
    board.add_player(player2)
    board.get_slot((12,14)).place_piece(Piece("BLUE", (12, 14)))
    board.get_slot((10,12)).place_piece(Piece("BLUE", (10, 12)))
    board.get_slot((8,10)).place_piece(Piece("BLUE", (8, 10)))
    board.get_slot((8,12)).place_piece(Piece("BLUE", (8, 12)))
    board.get_slot((6,14)).place_piece(Piece("BLUE", (6, 14)))
    assert board.get_possible_moves(board.get_slot((13,15))) == {(5, 15), (11, 13), (12, 16), (7, 13), (7, 9), (9, 11)}
    assert board.get_possible_moves(board.get_slot((13,13))) == {(12, 12), (11, 15)}
    assert board.get_possible_moves(board.get_slot((13,14))) == set()

