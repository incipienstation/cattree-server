from cattree.services.games.janggi.commands.command import MoveCommand
from cattree.services.games.janggi.game import JanggiGame
from cattree.services.games.janggi.player import Player
from cattree.services.games.janggi.enums.colour import Colour
from cattree.services.games.janggi.enums.elephant_config import ElephantConfig
from cattree.services.games.janggi.position import Position

blue_player = Player(Colour.BLUE)
red_player = Player(Colour.RED)
blue_player.set_elephant_config(ElephantConfig.LEFT)

game = JanggiGame(blue_player, red_player)
game.print_board()
game.print_curr_player_colour()
game.get_curr_player_movable_positions()
game.execute_command(blue_player, MoveCommand(Position(1, 2), Position(1, 3)))

