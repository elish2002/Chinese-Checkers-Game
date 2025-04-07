class Piece:
    """ 
    the class represents a piece object. the piece object is a piece that
    the player can move around the board. the piece object has a color and
    a location. the piece object can move to a new location.
    """
    def __init__(self, color: str, location: tuple) -> None:
        self.color = color
        self.location = location

    def move(self, new_location: tuple) -> None:
        self.location = new_location


