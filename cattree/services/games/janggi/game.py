from cattree.services.games.janggi import Player
from cattree.services.games.janggi.commands import Command, SurrenderCommand, BoardCommand, CommandFactory
from cattree.services.games.janggi.engine import Engine
from cattree.services.games.janggi.enums import Colour
from cattree.services.games.janggi.exceptions import InvalidPlayerColourException


class JanggiGame:
    def __init__(self, blue_player: Player, red_player: Player):
        if blue_player.colour != Colour.BLUE or red_player.colour != Colour.RED:
            raise InvalidPlayerColourException()
        self.__engine = Engine(blue_player, red_player)

    def take_turn(self) -> None:
        self.__engine.print_board()
        self.__engine.print_curr_player_colour()
        self.__engine.save_curr_player_movable_positions()

    def finish(self) -> None:
        self.__engine.print_board()

    def execute_command(self, player: Player, command: Command) -> None:
        command = self.__get_validated_command(player, command)
        if command is not None:
            command.execute(self.__engine)

    def __get_validated_command(self, player: Player, command: Command) -> Command | None:
        if isinstance(command, SurrenderCommand):
            return command
        if not self.__engine.is_player_turn(player):
            print("Not your turn\n")
            return None
        if isinstance(command, BoardCommand):
            if self.__engine.is_position_occupied(command.pos_to):
                return CommandFactory.create_capture_command(command.pos_from, command.pos_to)
            else:
                return CommandFactory.create_move_command(command.pos_from, command.pos_to)
        return command
