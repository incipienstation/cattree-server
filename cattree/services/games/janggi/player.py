from cattree.services.games.janggi.enums import Colour, ElephantConfig
from cattree.services.games.janggi.pieces import Piece


class Player:
    def __init__(self, colour: Colour):
        self.__colour = colour
        self.__elephant_config = ElephantConfig.RIGHT
        self.__is_online = True
        self.__score = 73.5 if colour == Colour.RED else 72
        self.__captives = []

    def set_elephant_config(self, elephant_config: ElephantConfig) -> None:
        self.__elephant_config = elephant_config

    def login(self) -> None:
        self.__is_online = True

    def logout(self) -> None:
        self.__is_online = False

    def add_captive(self, piece: Piece):
        self.__captives.append(piece)

    def get_captives(self):
        return self.__captives

    @property
    def is_online(self) -> bool:
        return self.__is_online

    @property
    def colour(self) -> Colour:
        return self.__colour

    @property
    def elephant_config(self) -> ElephantConfig:
        return self.__elephant_config
