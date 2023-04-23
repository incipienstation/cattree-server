from cattree.services.games.janggi.board import BoardFactory
from cattree.services.games.janggi.exceptions.player_exceptions import InvalidPlayerColourException
from cattree.services.games.janggi.player import Player
from cattree.services.games.janggi.enums.colour import Colour


class JanggiGame:
    def __init__(self, blue_player: Player, red_player: Player):
        if blue_player.colour != Colour.BLUE or red_player.colour != Colour.RED:
            raise InvalidPlayerColourException()
        self.__blue_player = blue_player
        self.__red_player = red_player
        self.__initialise_board()
        self.__print_board()

    def __initialise_board(self) -> None:
        self.__board = BoardFactory.get_board(self.__blue_player.elephant_config, self.__red_player.elephant_config)

    def __print_board(self) -> None:
        self.__board.print_all()
