from typing import List

from board import *


class Piece():
    """
    Put description of the Piece class here
    """

    def __init__(self, color: str, pos: List):
        if color != "W" and color != "B":
            raise Exception("Pieces can only be black, or white.")
        
        if len(pos) != 2 or A < pos[X] or H < pos[X] or 0 < pos[Y] or 7 < pos[Y]:
            raise Exception("Pieces can't be placed here.")

        self.pos = pos
        self.color = color
        

    def getPos(self) -> List:
        return self.pos
    
    def setPos(self, pos: List) -> None:
        self.pos = pos
        
    def is_valid_move(self, target_pos: List) -> bool:
        return False

    def is_white(self) -> bool:
        if self.color == "W":
            return True

        return False

    def __str__(self):
        return ""
        
# I'll add which parameters I generally used for the specific subclasses
# in the following Rook class, but note you may need more or less depending
# on your specific implementation
class Rook(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos) 
        # parrent init function to avoid the same lines of code
        pass

    def is_valid_move(self, board, start, to):
        pass

class Knight(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

class Bishop(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

class Queen(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

class King(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass
    
    # I added an extra method for the King class
    def can_castle(self):
        pass

# Class to represent a pseudo pawn that can be taken when
# en passant is possible
class GhostPawn(Piece):
    def __init__(self, color):
        pass

    def is_valid_move(self):
        return False

class Pawn(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass