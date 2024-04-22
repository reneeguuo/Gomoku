import pygame
from pygame import display
from .functions import mouse_operation, draw_chessboard, draw_mouse_indicator, draw_script


class Game:

    def __init__(self) -> None:

        self.chess_arr = []
        self.flag = 1
        self.game_state = 1
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.game_state, self.flag = mouse_operation(
                        self.game_state, self.chess_arr, self.flag)
                elif event.type == pygame.KEYDOWN and self.game_state != 1:
                    if event.key == pygame.K_SPACE:
                        self.flag = 1
                        self.game_state = 1
                        self.chess_arr = list()

            self.screen.fill((206, 163, 134))

            draw_chessboard(self.screen, (30, 35, 12), self.chess_arr)

            draw_script(self.flag, self.screen, self.game_state)

            draw_mouse_indicator(self.screen, self.game_state)
            pygame.display.update()
            self.clock.tick(60)



