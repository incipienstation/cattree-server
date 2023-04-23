from cattree.services.games.janggi.enums.colour import Colour
from cattree.services.games.janggi.enums.elephant_config import ElephantConfig


class Player:
    def __init__(self, colour: Colour):
        self.__colour = colour
        self.__elephant_config = ElephantConfig.RIGHT
        self.__is_online = True
        self.__score = 73.5 if colour == Colour.RED else 72

    def set_elephant_config(self, elephant_config: ElephantConfig) -> None:
        self.__elephant_config = elephant_config

    def login(self) -> None:
        self.__is_online = True

    def logout(self) -> None:
        self.__is_online = False

    @property
    def is_online(self) -> bool:
        return self.__is_online

    @property
    def colour(self) -> Colour:
        return self.__colour

    @property
    def elephant_config(self) -> ElephantConfig:
        return self.__elephant_config
