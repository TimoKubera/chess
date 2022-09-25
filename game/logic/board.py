import pygame
import os

X, Y = 0, 1

IMG = {}
DIMENSION = 8
WIDTH = 750
SQUARE_SIZE = WIDTH // DIMENSION

class Board():
    """
    Put description of the Board class here
    """
    def __init__(self):
        # replace body with the initialization of a standard
        # chess board with it's pieces placed correctly
        self.board = [
            ["black-rook", "black-knight", "black-bishop", "black-queen", "black-king", "black-knight", "black-bishop", "black-rook"],
            ["black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn"],
            ["#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#"],
            ["white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn"],
            ["white-rook", "white-knight", "white-bishop", "white-queen", "white-king", "white-knight", "white-bishop", "white-rook"]
        ]
        self.load_images()

    def draw_board(self, surface):
        colors = [pygame.Color(205, 165, 105), pygame.Color(73, 53, 35)]

        for x in range(DIMENSION):
            for y in range(DIMENSION):
                color = colors[(x + y) % 2]         # XOR relation for white fields is 0 and for black fields 1
                pygame.draw.rect(surface, color, pygame.Rect(y * SQUARE_SIZE, x * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self, surface):
        colors = [pygame.Color(205, 165, 105), pygame.Color(73, 53, 35)]

        for x in range(DIMENSION):
            for y in range(DIMENSION):
                piece = self.get_pos((x, y))
                if piece != "#":
                    surface.blit(IMG[piece], pygame.Rect(y * SQUARE_SIZE, x * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_gamestate(self, surface):
        self.draw_board(surface)
        self.draw_pieces(surface)

    def load_images(self):
        piece_names = ["white-pawn", "white-rook", "white-knight", "white-bishop", "white-queen", "white-king",
                        "black-pawn", "black-rook", "black-knight", "black-bishop", "black-queen", "black-king"]

        for piece in piece_names:
            curr_path = os.getcwd()
            img_path = os.path.join(curr_path, "game/gui/img/", piece + ".png")
            IMG[piece] = pygame.transform.scale(pygame.image.load(img_path), (SQUARE_SIZE * 0.95, SQUARE_SIZE * 0.95))

    def get_pos(self, pos):
        return self.board[pos[X]][pos[Y]]

    def set_pos(self, pos, piece):
        self.board[pos[X]][pos[Y]] = piece