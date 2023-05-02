from cattree.services.games.janggi.board import BoardFactory
from cattree.services.games.janggi.commands.command import Command
from cattree.services.games.janggi.enums.colour import Colour
from cattree.services.games.janggi.exceptions.command_exceptions import InvalidCommandException
from cattree.services.games.janggi.exceptions.player_exceptions import InvalidPlayerColourException
from cattree.services.games.janggi.player import Player


class JanggiGame:
    def __init__(self, blue_player: Player, red_player: Player):
        if blue_player.colour != Colour.BLUE or red_player.colour != Colour.RED:
            raise InvalidPlayerColourException()
        self.__blue_player = blue_player
        self.__red_player = red_player
        self.__curr_player_colour = Colour.BLUE
        self.__initialise_board()

    def __initialise_board(self) -> None:
        self.__board = BoardFactory.generate_board(self.__blue_player.elephant_config, self.__red_player.elephant_config)
        # self.__board = BoardFactory.generate_test_board_1()
        # self.__board = BoardFactory.generate_test_board_2()

    def print_board(self) -> None:
        print(self.__board)

    def get_curr_player_movable_positions(self) -> None:
        return self.__board.get_movable_positions(self.__curr_player_colour)

    def execute_command(self, player: Player, command: Command) -> None:
        try:
            self.__is_player_turn(player)
            # TODO
            # the surrender command is also valid under the other player's turn
            self.__validate_command(command)
            command.execute()
            self.__switch_turn()
        except InvalidPlayerColourException:
            pass
        except InvalidCommandException:
            pass
        finally:
            pass

    def print_curr_player_colour(self) -> None:
        print('\033[34m<BLUE TURN>\033[0m' if self.__curr_player_colour == Colour.BLUE else '\033[31m<RED TURN>\033[0m')

    def __switch_turn(self) -> None:
        self.__curr_player_colour = Colour.BLUE if self.__curr_player_colour == Colour.RED else Colour.RED

    def __is_player_turn(self, player: Player) -> bool:
        return player.colour == self.__curr_player_colour

    def __validate_command(self, command: Command) -> None:
        pass
