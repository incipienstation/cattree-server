from cattree.services.games.janggi.enums.colour import Colour
from cattree.services.games.janggi.pieces.piece import Piece
from cattree.services.games.janggi.position import Position


class Soldier(Piece):
    def __str__(self):
        return super().__str__() + "졸" + "\033[0m"

    def get_movable_positions(self, curr_pos: Position, state: dict[Position, Piece]) -> set[Position]:
        def handle_filter(_delta: (int, int)) -> bool:
            is_non_backward_movement = self._colour == Colour.BLUE and _delta[1] <= 0 \
                                       or self._colour == Colour.RED and _delta[1] >= 0
            if not is_non_backward_movement:
                return False
            translated_pos = curr_pos.translate_by_delta(_delta)
            is_not_occupied_by_ally = translated_pos not in state or not self._is_ally_with(state[translated_pos])
            return is_non_backward_movement and is_not_occupied_by_ally

        filtered_deltas = filter(handle_filter, curr_pos.get_adjacency_deltas())
        return set(map(lambda delta: curr_pos.translate_by_delta(delta), filtered_deltas))
