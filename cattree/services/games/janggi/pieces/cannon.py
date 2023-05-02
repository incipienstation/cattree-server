from cattree.services.games.janggi.pieces.piece import Piece
from cattree.services.games.janggi.position import Position


class Cannon(Piece):
    def get_movable_positions(self, curr_pos: Position, state: dict[Position, Piece]) -> list[Position]:
        res = []

        def search_straight(_pos: Position, _delta: (int, int), has_jumped_over: bool = False) -> None:
            translated_pos = _pos.translate_by_delta(_delta)
            is_not_occupied = translated_pos not in state
            if has_jumped_over:
                if is_not_occupied or not self._is_ally_with(state[translated_pos]) \
                        and not isinstance(state[translated_pos], Cannon):
                    res.append(translated_pos)
                if is_not_occupied and _delta in translated_pos.get_adjacency_deltas():
                    search_straight(translated_pos, _delta, True)
            elif _delta in translated_pos.get_adjacency_deltas():
                if is_not_occupied:
                    search_straight(translated_pos, _delta, False)
                elif not isinstance(state[translated_pos], Cannon):
                    search_straight(translated_pos, _delta, True)

        for delta in curr_pos.get_adjacency_deltas():
            search_straight(curr_pos, delta)
        return res
