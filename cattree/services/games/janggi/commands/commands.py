from abc import ABC, abstractmethod

from cattree.services.games.janggi.position import Position
from cattree.services.games.janggi.engine import Engine


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
        self.__pos_from = pos_from
        self.__pos_to = pos_to


class MoveCommand(BoardCommand):
    def __init__(self, pos_from: Position, pos_to: Position):
        super().__init__(pos_from, pos_to)

    def execute(self, engine: Engine):
        # engine.move
        engine.switch_turn()
        pass


class CaptureCommand(BoardCommand):
    def __init__(self, pos_from: Position, pos_to: Position):
        super().__init__(pos_from, pos_to)

    def execute(self, engine: Engine):
        engine.switch_turn()
        pass
