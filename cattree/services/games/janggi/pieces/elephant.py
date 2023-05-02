from cattree.services.games.janggi.pieces.piece import Piece
from cattree.services.games.janggi.position import Position


class Elephant(Piece):
    def __str__(self):
        return super().__str__() + '상' + "\033[0m"

    def get_movable_positions(self, curr_pos: Position, state: dict[Position, Piece]) -> list[Position]:
        pass
