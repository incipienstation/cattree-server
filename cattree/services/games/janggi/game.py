from cattree.services.games.janggi import Player
from cattree.services.games.janggi.commands import Command
from cattree.services.games.janggi.engine import Engine
from cattree.services.games.janggi.enums import Colour
from cattree.services.games.janggi.exceptions import InvalidCommandException, InvalidPlayerColourException


class JanggiGame:
    def __init__(self, blue_player: Player, red_player: Player):
        if blue_player.colour != Colour.BLUE or red_player.colour != Colour.RED:
            raise InvalidPlayerColourException()
        self.__engine = Engine(blue_player, red_player)

    def take_turn(self) -> None:
        self.__engine.print_board()
        self.__engine.print_curr_player_colour()
        self.__engine.get_curr_player_movable_positions()

    def execute_command(self, player: Player, command: Command) -> None:
        try:
            # self.__is_player_turn(player)
            # TODO
            # the surrender command is also valid under the other player's turn
            # command.validate()
            command.execute(self.__engine)
        except InvalidPlayerColourException:
            pass
        except InvalidCommandException:
            pass
        finally:
            pass

    def __validate_command(self, command: Command) -> None:
        pass
