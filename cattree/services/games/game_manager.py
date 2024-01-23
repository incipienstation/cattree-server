from cattree.services.games.janggi import JanggiGame, Player, Position
from cattree.services.games.janggi.commands import CommandFactory
from cattree.services.games.janggi.enums import Colour, ElephantConfig


def game1():
    blue_player = Player(Colour.BLUE)
    red_player = Player(Colour.RED)
    blue_player.set_elephant_config(ElephantConfig.INNER)
    red_player.set_elephant_config(ElephantConfig.INNER)

    game = JanggiGame(blue_player, red_player)
    game.take_turn()
    game.execute_command(blue_player, CommandFactory.create_move_command(Position(0, 6), Position(1, 6)))
    game.take_turn()
    game.execute_command(red_player, CommandFactory.create_move_command(Position(8, 3), Position(7, 3)))
    game.take_turn()
    game.execute_command(blue_player, CommandFactory.create_capture_command(Position(0, 9), Position(0, 3)))
    game.take_turn()
    game.execute_command(red_player, CommandFactory.create_capture_command(Position(0, 0), Position(0, 3)))
    game.take_turn()
    game.execute_command(blue_player, CommandFactory.create_move_command(Position(1, 7), Position(1, 3)))
    game.take_turn()
    game.execute_command(red_player, CommandFactory.create_capture_command(Position(0, 3), Position(1, 3)))
    game.take_turn()
    game.execute_command(blue_player, CommandFactory.create_capture_command(Position(4, 8), Position(3, 7)))
    game.finish()

    print(blue_player.get_captives())
    print(red_player.get_captives())


def game2():
    blue_player = Player(Colour.BLUE)
    red_player = Player(Colour.RED)
    blue_player.set_elephant_config(ElephantConfig.INNER)
    red_player.set_elephant_config(ElephantConfig.INNER)

    game = JanggiGame(blue_player, red_player)
    game.take_turn()
    game.execute_command(blue_player, CommandFactory.create_move_command(Position(4, 8), Position(3, 7)))
    game.take_turn()
    game.execute_command(red_player, CommandFactory.create_move_command(Position(4, 3), Position(5, 3)))
    game.take_turn()
    game.execute_command(blue_player, CommandFactory.create_move_command(Position(1, 7), Position(4, 7)))
    game.take_turn()
    game.execute_command(red_player, CommandFactory.create_move_command(Position(6, 0), Position(4, 3)))
    game.take_turn()
    game.execute_command(blue_player, CommandFactory.create_move_command(Position(4, 7), Position(4, 4)))
    game.take_turn()
    game.execute_command(red_player, CommandFactory.create_move_command(Position(4, 3), Position(1, 5)))
    game.take_turn()
    game.execute_command(blue_player, CommandFactory.create_move_command(Position(3, 7), Position(4, 8)))
    game.take_turn()
    game.execute_command(red_player, CommandFactory.create_move_command(Position(1, 5), Position(4, 3)))
    game.take_turn()


if __name__ == "__main__":
    game2()
