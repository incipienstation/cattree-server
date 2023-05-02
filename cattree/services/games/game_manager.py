from cattree.services.games.janggi import JanggiGame, Player, Position
from cattree.services.games.janggi.commands import CommandFactory
from cattree.services.games.janggi.enums import Colour, ElephantConfig

blue_player = Player(Colour.BLUE)
red_player = Player(Colour.RED)
blue_player.set_elephant_config(ElephantConfig.LEFT)
red_player.set_elephant_config(ElephantConfig.INNER)

game = JanggiGame(blue_player, red_player)
game.take_turn()
game.execute_command(blue_player, CommandFactory.create_move_command(Position(0, 6), Position(1, 6)))
