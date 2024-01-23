from cattree.services.games.janggi.enums import Colour


class Position:
    WIDTH = 9
    HEIGHT = 10
    __adjacency_delta_cache = {}

    def __init__(self, x: int, y: int):
        # uncomment below for debugging
        # if not (0 <= x < self.WIDTH and 0 <= y < self.HEIGHT):
        #     raise PositionOutOfRangeException()
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

    def is_valid(self) -> bool:
        return 0 <= self.__x < self.WIDTH and 0 <= self.__y < self.HEIGHT

    def get_adjacency_deltas(self) -> set[(int, int)] | None:
        if self in self.__adjacency_delta_cache:
            return self.__adjacency_delta_cache[self]
        if not self.is_valid():
            return None
        res = {(0, -1), (0, 1), (-1, 0), (1, 0)}
        if self.__x == 0:
            res.remove((-1, 0))
        elif self.__x == self.WIDTH - 1:
            res.remove((1, 0))
        if self.__y == 0:
            res.remove((0, -1))
        elif self.__y == self.HEIGHT - 1:
            res.remove((0, 1))
        if self == Position(4, 1) or self == Position(4, 8):
            res.update({(1, 1), (1, -1), (-1, 1), (-1, -1)})
        elif self == Position(3, 0) or self == Position(3, 7):
            res.add((1, 1))
        elif self == Position(3, 2) or self == Position(3, 9):
            res.add((1, -1))
        elif self == Position(5, 0) or self == Position(5, 7):
            res.add((-1, 1))
        elif self == Position(5, 2) or self == Position(5, 9):
            res.add((-1, -1))
        self.__adjacency_delta_cache[self] = res
        return res

    def translate_by_delta(self, delta: (int, int)) -> "Position":
        return Position(self.__x + delta[0], self.__y + delta[1])

    def is_in_castle(self, colour: Colour) -> bool:
        y = 1 if colour == Colour.RED else 8
        return 3 <= self.__x <= 5 and y - 1 <= self.__y <= y + 1
