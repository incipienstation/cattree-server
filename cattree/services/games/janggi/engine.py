from cattree.services.games.janggi import Player, Position
from cattree.services.games.janggi.board import BoardFactory
from cattree.services.games.janggi.enums import Colour
from cattree.services.games.janggi.exceptions import InvalidMovementException


class Engine:
    def __init__(self, blue_player: Player, red_player: Player):
        self.__blue_player = blue_player
        self.__red_player = red_player
        self.__curr_player_colour = Colour.BLUE
        self.__curr_player_movable_positions = None
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

    def save_curr_player_movable_positions(self) -> None:
        self.__curr_player_movable_positions = self.__board.get_movable_positions(self.__curr_player_colour)

    def switch_turn(self) -> None:
        self.__curr_player_colour = Colour.BLUE if self.__curr_player_colour == Colour.RED else Colour.RED

    def is_player_turn(self, player: Player) -> bool:
        return player == self.__get_curr_player()

    def __get_curr_player(self):
        return self.__blue_player if self.__curr_player_colour == Colour.BLUE else self.__red_player

    def __get_next_player(self):
        return self.__red_player if self.__curr_player_colour == Colour.BLUE else self.__blue_player

    def is_position_occupied(self, position: Position) -> bool:
        return self.__board.get_piece(position) is not None

    def move_piece(self, pos_from: Position, pos_to: Position):
        if self.__is_movement_possible(pos_from, pos_to):
            piece = self.__board.get_piece(pos_from)
            self.__board.remove_piece(pos_from)
            self.__board.add_piece(pos_to, piece)
        else:
            raise InvalidMovementException(f"an invalid movement from {pos_from} to {pos_to}")

    def capture_piece(self, pos_from: Position, pos_to: Position):
        if self.__is_movement_possible(pos_from, pos_to):
            piece = self.__board.get_piece(pos_from)
            self.__board.remove_piece(pos_from)
            self.__get_curr_player().add_captive(self.__board.pop_piece(pos_to))
            self.__board.add_piece(pos_to, piece)
        else:
            raise InvalidMovementException(f"an invalid movement from {pos_from} to {pos_to}")

    def __is_movement_possible(self, pos_from: Position, pos_to: Position) -> bool:
        if pos_from not in self.__curr_player_movable_positions:
            return False
        return pos_to in self.__curr_player_movable_positions[pos_from]
