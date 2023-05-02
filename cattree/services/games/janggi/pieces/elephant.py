from cattree.services.games.janggi.pieces.piece import Piece
from cattree.services.games.janggi.position import Position


class Elephant(Piece):
    __first_deltas = ((1, 0), (1, 0), (-1, 0), (-1, 0), (0, 1), (0, 1), (0, -1), (0, -1))
    __next_deltas = ((1, 1), (1, -1), (-1, 1), (-1, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))

    def __str__(self):
        return super().__str__() + '상' + "\033[0m"

    def get_movable_positions(self, curr_pos: Position, state: dict[Position, Piece]) -> set[Position]:
        res = set()
        for i in range(8):
            first_delta = self.__first_deltas[i]
            second_delta = tuple(sum(e) for e in zip(first_delta, self.__next_deltas[i]))
            third_delta = tuple(sum(e) for e in zip(second_delta, self.__next_deltas[i]))
            first_pos = curr_pos.translate_by_delta(first_delta)
            second_pos = curr_pos.translate_by_delta(second_delta)
            third_pos = curr_pos.translate_by_delta(third_delta)
            if third_pos.is_valid():
                if first_pos not in state and second_pos not in state and (
                        third_pos not in state or not self._is_ally_with(state[third_pos])):
                    res.add(third_pos)
        return res
