from cattree.services.games.janggi.exceptions.board_exceptions import PositionOutOfRangeException


class Position:
    WIDTH = 9
    HEIGHT = 10

    def __init__(self, x: int, y: int):
        if not (0 <= x < self.WIDTH and 0 <= y < self.HEIGHT):
            raise PositionOutOfRangeException()
        self.__x = x
        self.__y = y

    def __hash__(self):
        return hash((self.__x, self.__y))

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.__x == other.__x and self.__y == other.__y
        return False

    def __repr__(self):
        return f"({self.__x}, {self.__y})"
