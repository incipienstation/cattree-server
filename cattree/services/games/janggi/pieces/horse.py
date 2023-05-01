from cattree.services.games.janggi.pieces.piece import Piece
from cattree.services.games.janggi.position import Position


class Horse(Piece):
    def get_movable_positions(self, curr_pos: Position, state: dict[Position, Piece]) -> list[Position]:
        pass
