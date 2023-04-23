from cattree.services.games.janggi.enums.colour import Colour


class Piece:
    def __init__(self, colour: Colour):
        self.__colour = colour

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__colour})"


class General(Piece):
    pass


class Guard(Piece):
    pass


class Chariot(Piece):
    pass


class Cannon(Piece):
    pass


class Horse(Piece):
    pass


class Elephant(Piece):
    pass


class Soldier(Piece):
    pass
