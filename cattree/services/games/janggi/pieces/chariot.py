from cattree.services.games.janggi.pieces.piece import Piece
from cattree.services.games.janggi.position import Position


class Chariot(Piece):
    def __str__(self):
        return super().__str__() + '차' + "\033[0m"

    def get_movable_positions(self, curr_pos: Position, state: dict[Position, Piece]) -> set[Position]:
        res = set()

        def search_straight(_pos: Position, _delta: (int, int)) -> None:
            translated_pos = _pos.translate_by_delta(_delta)
            is_not_occupied = translated_pos not in state
            if is_not_occupied or not self._is_ally_with(state[translated_pos]):
                res.add(translated_pos)
            if is_not_occupied and _delta in translated_pos.get_adjacency_deltas():
                search_straight(translated_pos, _delta)

        for delta in curr_pos.get_adjacency_deltas():
            search_straight(curr_pos, delta)
        return res
