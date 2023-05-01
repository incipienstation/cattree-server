from abc import ABC, abstractmethod

from cattree.services.games.janggi.enums.colour import Colour
from cattree.services.games.janggi.position import Position


class Piece(ABC):
    def __init__(self, colour: Colour):
        self._colour = colour

    def __repr__(self):
        return f"{self.__class__.__name__}({self._colour})"

    @abstractmethod
    def get_movable_positions(self, curr_pos: Position, state: dict[Position, "Piece"]) -> list[Position]:
        pass

    def _is_ally_with(self, other: "Piece") -> bool:
        return self._colour == other._colour

    @property
    def colour(self):
        return self._colour


class CastlePiece(Piece, ABC):
    def get_movable_positions(self, curr_pos: Position, state: dict[Position, Piece]) -> list[Position]:
        def handle_filter(_delta: (int, int)) -> bool:
            translated_pos = curr_pos.translate_by_delta(_delta)
            is_in_castle = translated_pos.is_in_castle(self._colour)
            if not is_in_castle:
                return False
            is_not_occupied_by_ally = translated_pos not in state or not self._is_ally_with(state[translated_pos])
            return is_in_castle and is_not_occupied_by_ally

        filtered_deltas = filter(handle_filter, curr_pos.get_adjacency_deltas())
        return list(map(lambda delta: curr_pos.translate_by_delta(delta), filtered_deltas))
