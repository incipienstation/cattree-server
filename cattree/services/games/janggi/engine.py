from cattree.services.games.janggi import Player, Position
from cattree.services.games.janggi.board import BoardFactory
from cattree.services.games.janggi.enums import Colour
from cattree.services.games.janggi.exceptions import InvalidMovementException


class Engine:
    def __init__(self, blue_player: Player, red_player: Player):
        self.__blue_player = blue_player
        self.__red_player = red_player
        self.__curr_player_colour = Colour.BLUE
        self.__curr_player_movable_positions = {}
        self.__initialise_board()

    def print_board(self) -> None:
        print(self.__board)

    def print_curr_player_colour(self) -> None:
        print(
            "\033[34m<BLUE TURN>\033[0m\n" if self.__curr_player_colour == Colour.BLUE else "\033[31m<RED TURN>\033[0m\n")

    def print_message(self) -> None:
        if self.__is_curr_player_in_check():
            if self.__is_curr_player_in_checkmate():
                print("외통수!!!\n")
            else:
                print("장군~~~\n")

    def store_curr_player_movable_positions(self) -> None:
        self.__curr_player_movable_positions = self.__board.get_movable_positions(self.__curr_player_colour)
        if not self.__curr_player_movable_positions:
            self.switch_turn()

    def switch_turn(self) -> None:
        self.__curr_player_colour = self.__get_next_player_colour()

    def is_player_turn(self, player: Player) -> bool:
        return player == self.__get_curr_player()

    def is_position_occupied(self, position: Position) -> bool:
        return self.__board.get_piece(position) is not None

    def move_piece(self, pos_from: Position, pos_to: Position):
        if self.__is_movement_possible(pos_from, pos_to):
            piece = self.__board.pop_piece(pos_from)
            self.__board.add_piece(pos_to, piece)
        else:
            raise InvalidMovementException(f"an invalid movement from {pos_from} to {pos_to}")

    def capture_piece(self, pos_from: Position, pos_to: Position):
        if self.__is_movement_possible(pos_from, pos_to):
            captive = self.__board.pop_piece(pos_to)
            self.__get_curr_player().add_captive(captive)
            piece = self.__board.pop_piece(pos_from)
            self.__board.add_piece(pos_to, piece)
        else:
            raise InvalidMovementException(f"an invalid movement from {pos_from} to {pos_to}")

    def __initialise_board(self) -> None:
        self.__board = BoardFactory.generate_board(self.__blue_player.elephant_config,
                                                   self.__red_player.elephant_config)
        # self.__board = BoardFactory.generate_test_board_1()
        # self.__board = BoardFactory.generate_test_board_2()

    def __get_next_player_colour(self) -> Colour:
        return Colour.RED if self.__curr_player_colour == Colour.BLUE else Colour.BLUE

    def __get_curr_player(self) -> Player:
        return self.__blue_player if self.__curr_player_colour == Colour.BLUE else self.__red_player

    def __is_movement_possible(self, pos_from: Position, pos_to: Position) -> bool:
        if pos_from not in self.__curr_player_movable_positions:
            return False
        if pos_to not in self.__curr_player_movable_positions[pos_from]:
            return False
        if self.__is_movement_raising_check(pos_from, pos_to):
            return False
        return True

    def __is_movement_raising_check(self, pos_from: Position, pos_to: Position) -> bool:
        board_copy = BoardFactory.copy_board(self.__board)
        board_copy.remove_piece(pos_to)
        piece = board_copy.pop_piece(pos_from)
        board_copy.add_piece(pos_to, piece)
        return board_copy.is_player_in_check(self.__curr_player_colour)

    def __is_curr_player_in_check(self) -> bool:
        return self.__board.is_player_in_check(self.__curr_player_colour)

    def __is_curr_player_in_checkmate(self) -> bool:
        for pos_from, pos_to_set in self.__curr_player_movable_positions.items():
            for pos_to in pos_to_set:
                if not self.__is_movement_raising_check(pos_from, pos_to):
                    return False
        return True
