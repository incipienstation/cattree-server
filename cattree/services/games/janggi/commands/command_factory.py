from cattree.services.games.janggi.position import Position
from cattree.services.games.janggi.commands import Command, BreakCommand, SurrenderCommand, CaptureCommand, MoveCommand


class CommandFactory:
    @staticmethod
    def create_move_command(pos_from: Position, pos_to: Position) -> Command:
        return MoveCommand(pos_from, pos_to)

    @staticmethod
    def create_capture_command(pos_from: Position, pos_to: Position) -> Command:
        return CaptureCommand(pos_from, pos_to)

    @staticmethod
    def create_surrender_command() -> Command:
        return SurrenderCommand()

    @staticmethod
    def create_break_command() -> Command:
        return BreakCommand()
