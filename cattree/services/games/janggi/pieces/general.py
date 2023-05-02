from cattree.services.games.janggi.pieces.piece import CastlePiece


class General(CastlePiece):
    def __str__(self):
        return super().__str__() + '궁' + "\033[0m"
