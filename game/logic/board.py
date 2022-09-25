import pygame

X, Y = 0, 1

IMG = {}
MAX_FPS = 15
DIMENSION = 8
WIDTH = HEIGHT = 512
SQUARE_SIZE = WIDTH // DIMENSION

class Board():
    """
    Put description of the Board class here
    """
    def __init__(self):
        # replace body with the initialization of a standard
        # chess board with it's pieces placed correctly
        self.board = [
            ["black-rook", "black-knight", "black-bishop", "black-queen", "black-knight", "black-bishop"],
            ["black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn"],
            ["#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#"],
            ["white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn"],
            ["white-rook", "white-knight", "white-bishop", "white-queen", "white-knight", "white-bishop"]
        ]

    def draw_board(self, surface):
        colors = [pygame.Color(100, 89, 80), pygame.Color(73, 53, 35)]

        for x in range(DIMENSION):
            for y in range(DIMENSION):
                color = colors[(x + y) % 2]         # XOR relation for white fields is 0 and for black fields 1
                pygame.draw.rect(surface, color, pygame.Rect(y * SQUARE_SIZE, x * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def get_pos(self, pos):
        return self.board[pos[X]][pos[Y]]

    def set_pos(self, pos, piece):
        self.board[pos[X]][pos[Y]] = piece