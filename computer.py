from player import Player
from board import Board
from constants import OPTIONAL_COLORS

class computer:
    def __init__(self, board, name, color = None):
        self.board = board
        self.computers = []
        self.name = name
        self.color = color



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
        self.color = options[0]
        name = f"computer{len(self.board.players)}"
        player = Player(name, self.color)
        self.board.players.append(player)
        self.computers.append(player)
