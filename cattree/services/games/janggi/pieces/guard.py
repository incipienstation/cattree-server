from cattree.services.games.janggi.pieces.piece import CastlePiece


class Guard(CastlePiece):
    def __str__(self):
        return super().__str__() + '사' + "\033[0m"
