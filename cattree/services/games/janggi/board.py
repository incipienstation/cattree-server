import time

from cattree.services.games.janggi import Position
from cattree.services.games.janggi.enums import Colour, ElephantConfig
from cattree.services.games.janggi.exceptions.board_exceptions import PositionAlreadyOccupiedException
from cattree.services.games.janggi.pieces import Piece, Chariot, General, Cannon, Guard, Soldier, Horse, Elephant


class Board:
    def __init__(self):
        self.__state = {}

    def __str__(self):
        board_str = ""
        for y in range(10):
            for x in range(9):
                piece = self.__state.get(Position(x, y))
                if piece is not None:
                    board_str += str(piece)
                else:
                    board_str += "ㅇ"
                board_str += " "
            board_str += "\n"
        return board_str

    def get_piece(self, position: Position) -> Piece | None:
        return self.__state.get(position)

    def add_piece(self, position: Position, piece: Piece) -> None:
        if position in self.__state:
            raise PositionAlreadyOccupiedException()
        self.__state[position] = piece

    def remove_piece(self, position: Position) -> None:
        del self.__state[position]

    def pop_piece(self, position: Position) -> Piece:
        return self.__state.pop(position)

    def get_movable_positions(self, colour: Colour) -> dict[Position, set[Position]]:
        res = {}
        start_time = time.perf_counter()
        for pos, piece in self.__state.items():
            if piece.colour == colour:
                res[pos] = piece.get_movable_positions(pos, self.__state)
        end_time = time.perf_counter()
        print(f"get_movable_positions: {round((end_time - start_time) * 1_000, 4)}ms\n")
        return res


class BoardFactory:
    @staticmethod
    def generate_board(blue_elephant_config: ElephantConfig, red_elephant_config: ElephantConfig) -> Board:
        board = Board()
        BoardFactory.__generate_default(board)
        BoardFactory.__generate_optional_with_colour(board, blue_elephant_config, Colour.BLUE)
        BoardFactory.__generate_optional_with_colour(board, red_elephant_config, Colour.RED)
        return board

    @staticmethod
    def __generate_default(board: Board) -> None:
        # blue pieces
        for x in range(0, Position.WIDTH, 2):
            board.add_piece(Position(x, 6), Soldier(Colour.BLUE))
        board.add_piece(Position(0, 9), Chariot(Colour.BLUE))
        board.add_piece(Position(1, 7), Cannon(Colour.BLUE))
        board.add_piece(Position(3, 9), Guard(Colour.BLUE))
        board.add_piece(Position(4, 8), General(Colour.BLUE))
        board.add_piece(Position(5, 9), Guard(Colour.BLUE))
        board.add_piece(Position(7, 7), Cannon(Colour.BLUE))
        board.add_piece(Position(8, 9), Chariot(Colour.BLUE))

        # red pieces
        for x in range(0, Position.WIDTH, 2):
            board.add_piece(Position(x, 3), Soldier(Colour.RED))
        board.add_piece(Position(0, 0), Chariot(Colour.RED))
        board.add_piece(Position(1, 2), Cannon(Colour.RED))
        board.add_piece(Position(3, 0), Guard(Colour.RED))
        board.add_piece(Position(4, 1), General(Colour.RED))
        board.add_piece(Position(5, 0), Guard(Colour.RED))
        board.add_piece(Position(7, 2), Cannon(Colour.RED))
        board.add_piece(Position(8, 0), Chariot(Colour.RED))

    @staticmethod
    def __generate_optional_with_colour(board: Board, elephant_config: ElephantConfig, colour: Colour) -> None:
        y = 0 if colour == Colour.RED else 9
        if elephant_config == ElephantConfig.INNER:
            board.add_piece(Position(1, y), Horse(colour))
            board.add_piece(Position(2, y), Elephant(colour))
            board.add_piece(Position(6, y), Elephant(colour))
            board.add_piece(Position(7, y), Horse(colour))
        elif elephant_config == ElephantConfig.OUTER:
            board.add_piece(Position(1, y), Elephant(colour))
            board.add_piece(Position(2, y), Horse(colour))
            board.add_piece(Position(6, y), Horse(colour))
            board.add_piece(Position(7, y), Elephant(colour))
        elif elephant_config == ElephantConfig.RIGHT and colour == Colour.BLUE \
                or elephant_config == ElephantConfig.LEFT and colour == Colour.RED:
            board.add_piece(Position(1, y), Horse(colour))
            board.add_piece(Position(2, y), Elephant(colour))
            board.add_piece(Position(6, y), Horse(colour))
            board.add_piece(Position(7, y), Elephant(colour))
        else:
            board.add_piece(Position(1, y), Elephant(colour))
            board.add_piece(Position(2, y), Horse(colour))
            board.add_piece(Position(6, y), Elephant(colour))
            board.add_piece(Position(7, y), Horse(colour))

    @staticmethod
    def generate_test_board_1() -> Board:
        board = Board()
        board.add_piece(Position(4, 8), Chariot(Colour.BLUE))
        board.add_piece(Position(4, 4), Chariot(Colour.BLUE))
        board.add_piece(Position(2, 8), Chariot(Colour.RED))
        print('test 1: Chariot')
        return board

    @staticmethod
    def generate_test_board_2() -> Board:
        board = Board()
        board.add_piece(Position(4, 8), General(Colour.BLUE))
        board.add_piece(Position(3, 7), Cannon(Colour.BLUE))
        board.add_piece(Position(3, 4), Chariot(Colour.RED))
        board.add_piece(Position(3, 1), Cannon(Colour.RED))
        board.add_piece(Position(2, 7), Cannon(Colour.BLUE))
        board.add_piece(Position(4, 7), Guard(Colour.BLUE))
        board.add_piece(Position(6, 7), Soldier(Colour.RED))
        print('test 2: Cannon')
        return board
