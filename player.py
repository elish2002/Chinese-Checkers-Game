class Player:

    def __init__(self, name: str, color: str, wins: int = 0, loses: int = 0) -> None:
        """this function initializes the player object
        :param name: the name of the player
        :param color: the color of the player
        :param wins: the number of wins of the player
        :param loses: the number of loses of the player
        """

        self.__name = name
        self.__color = color.lower()
        self.wins = wins
        self.loses = loses

    def get_name(self):
        """this function returns the name of the player"""
        return self.__name

    def get_color(self):
        """this function returns the color of the player"""
        return self.__color




