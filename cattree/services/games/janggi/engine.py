from cattree.services.games.janggi import Player, Position
from cattree.services.games.janggi.board import BoardFactory
from cattree.services.games.janggi.enums import Colour


class Engine:

    def __init__(self, blue_player: Player, red_player: Player):
        self.__blue_player = blue_player
        self.__red_player = red_player
        self.__curr_player_colour = Colour.BLUE
        self.__initialise_board()

    def __initialise_board(self) -> None:
        self.__board = BoardFactory.generate_board(self.__blue_player.elephant_config,
                                                   self.__red_player.elephant_config)

        # self.__board = BoardFactory.generate_test_board_1()
        # self.__board = BoardFactory.generate_test_board_2()

    def print_board(self) -> None:
        print(self.__board)

    def print_curr_player_colour(self) -> None:
        print("\033[34m<BLUE TURN>\033[0m" if self.__curr_player_colour == Colour.BLUE else "\033[31m<RED TURN>\033[0m")

    def get_curr_player_movable_positions(self) -> None:
        return self.__board.get_movable_positions(self.__curr_player_colour)

    def switch_turn(self) -> None:
        self.__curr_player_colour = Colour.BLUE if self.__curr_player_colour == Colour.RED else Colour.RED

    def __is_player_turn(self, player: Player) -> bool:
        return player.colour == self.__curr_player_colour

    # def move_piece(self, pos_from: Position, pos_to: Position):

