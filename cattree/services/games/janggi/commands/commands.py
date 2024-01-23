from abc import ABC, abstractmethod

from cattree.services.games.janggi.engine import Engine
from cattree.services.games.janggi.exceptions import InvalidMovementException
from cattree.services.games.janggi.position import Position


class Command(ABC):
    @abstractmethod
    def execute(self, engine: Engine):
        pass


class BreakCommand(Command):

    def execute(self, engine: Engine):
        pass


class SurrenderCommand(Command):

    def execute(self, engine: Engine):
        pass


class BoardCommand(Command, ABC):
    def __init__(self, pos_from: Position, pos_to: Position):
        self._pos_from = pos_from
        self._pos_to = pos_to

    def __str__(self):
        return f"{self.__class__.__name__}: from {self.pos_from} to {self._pos_to}"

    @property
    def pos_from(self):
        return self._pos_from

    @property
    def pos_to(self):
        return self._pos_to


class MoveCommand(BoardCommand):
    def __init__(self, pos_from: Position, pos_to: Position):
        super().__init__(pos_from, pos_to)

    def execute(self, engine: Engine):
        try:
            engine.move_piece(self._pos_from, self._pos_to)
            engine.switch_turn()
            print(self)
        except InvalidMovementException as e:
            print(e)


class CaptureCommand(BoardCommand):
    def __init__(self, pos_from: Position, pos_to: Position):
        super().__init__(pos_from, pos_to)

    def execute(self, engine: Engine):
        try:
            engine.capture_piece(self._pos_from, self._pos_to)
            engine.switch_turn()
            print(self)
        except InvalidMovementException as e:
            print(e)

