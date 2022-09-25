import pygame
from board import Board
pygame.init()

MAX_FPS = 15
WIDTH = HEIGHT = 750

class Game():
    """
    Put description of the Chess class here
    """

    def __init__(self):
        # replace `pass` with the desired attributes and add any 
        # additional parameters to the function  
        self.whites_turn = True
        self.board = Board()
        self.move_log = []


    def promotion(self):
        # add any parameters necessary and replace the body with
        # functionality on promoting a Pawn that has reached the 
        # end of the board
        pass

    def move(self):
        # add any parameters necessary and replace the body with
        # functionality of moving a a piece from its current location
        # to a destination
        pass

    def main(self):
        surface = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        
        self.board.draw_gamestate(surface)

        gamesate = ""

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            clock.tick(MAX_FPS)
            pygame.display.flip()


if __name__ == "__main__":
    Game().main()