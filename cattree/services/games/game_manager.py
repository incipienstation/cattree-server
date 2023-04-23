from cattree.services.games.janggi.game import JanggiGame
from cattree.services.games.janggi.player import Player
from cattree.services.games.janggi.enums.colour import Colour
from cattree.services.games.janggi.enums.elephant_config import ElephantConfig


blue_player = Player(Colour.BLUE)
red_player = Player(Colour.RED)
blue_player.set_elephant_config(ElephantConfig.INNER)

game = JanggiGame(blue_player, red_player)
