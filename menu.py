import pygame
from pygame import font

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chinese checkers")
FPS = 60

step = 0


def how_many_players():
    how_many_player = pygame.draw.rect(WIN, (255, 255, 255), (
        WIDTH // 2 - 150, HEIGHT // 2 - 100, 250, 50))
    two = pygame.draw.rect(WIN, (255, 255, 255),
                           (WIDTH // 2 - 150, HEIGHT // 2, 40, 50))
    three = pygame.draw.rect(WIN, (255, 255, 255),
                             (WIDTH // 2 - 100, HEIGHT // 2, 40, 50))
    four = pygame.draw.rect(WIN, (255, 255, 255),
                            (WIDTH // 2 - 50, HEIGHT // 2, 40, 50))
    five = pygame.draw.rect(WIN, (255, 255, 255),
                            (WIDTH // 2, HEIGHT // 2, 40, 50))
    six = pygame.draw.rect(WIN, (255, 255, 255),
                           (WIDTH // 2 + 50, HEIGHT // 2, 40, 50))
    font = pygame.font.Font(None, 24)
    text_surface1 = font.render("choose how many players?", True, (0, 0, 0))
    text_surface2 = font.render("2", True, (0, 0, 0))
    text_surface3 = font.render("3", True, (0, 0, 0))
    text_surface4 = font.render("4", True, (0, 0, 0))
    text_surface5 = font.render("5", True, (0, 0, 0))
    text_surface6 = font.render("6", True, (0, 0, 0))
    text_width1, text_height1 = font.size("choose how many players?")
    text_width2, text_height2 = font.size("2")
    text_width3, text_height3 = font.size("3")
    text_width4, text_height4 = font.size("4")
    text_width5, text_height5 = font.size("5")
    text_width6, text_height6 = font.size("6")
    text_x1 = how_many_player.centerx - text_width1 // 2
    text_y1 = how_many_player.centery - text_height1 // 2
    text_x2 = two.centerx - text_width2 // 2
    text_y2 = two.centery - text_height2 // 2
    text_x3 = three.centerx - text_width3 // 2
    text_y3 = three.centery - text_height3 // 2
    text_x4 = four.centerx - text_width4 // 2
    text_y4 = four.centery - text_height4 // 2
    text_x5 = five.centerx - text_width5 // 2
    text_y5 = five.centery - text_height5 // 2
    text_x6 = six.centerx - text_width6 // 2
    text_y6 = six.centery - text_height6 // 2
    WIN.blit(text_surface1, (text_x1, text_y1))
    WIN.blit(text_surface2, (text_x2, text_y2))
    WIN.blit(text_surface3, (text_x3, text_y3))
    WIN.blit(text_surface4, (text_x4, text_y4))
    WIN.blit(text_surface5, (text_x5, text_y5))
    WIN.blit(text_surface6, (text_x6, text_y6))


def how_many_computer_players():
    how_many_players = pygame.draw.rect(WIN, (255, 255, 255), (
        WIDTH // 2 - 150, HEIGHT // 2 - 100, 250, 50))
    two = pygame.draw.rect(WIN, (255, 255, 255),
                           (WIDTH // 2 - 150, HEIGHT // 2, 40, 50))
    three = pygame.draw.rect(WIN, (255, 255, 255),
                             (WIDTH // 2 - 100, HEIGHT // 2, 40, 50))
    four = pygame.draw.rect(WIN, (255, 255, 255),
                            (WIDTH // 2 - 50, HEIGHT // 2, 40, 50))
    five = pygame.draw.rect(WIN, (255, 255, 255),
                            (WIDTH // 2, HEIGHT // 2, 40, 50))
    six = pygame.draw.rect(WIN, (255, 255, 255),
                           (WIDTH // 2 + 50, HEIGHT // 2, 40, 50))
    font = pygame.font.Font(None, 24)
    text_surface1 = font.render("choose how many computer players?", True,
                                (0, 0, 0))
    text_surface2 = font.render("2", True, (0, 0, 0))
    text_surface3 = font.render("3", True, (0, 0, 0))
    text_surface4 = font.render("4", True, (0, 0, 0))
    text_surface5 = font.render("5", True, (0, 0, 0))
    text_surface6 = font.render("6", True, (0, 0, 0))
    text_width1, text_height1 = font.size("choose how many computer players?")
    text_width2, text_height2 = font.size("2")
    text_width3, text_height3 = font.size("3")
    text_width4, text_height4 = font.size("4")
    text_width5, text_height5 = font.size("5")
    text_width6, text_height6 = font.size("6")
    text_x1 = how_many_players.centerx - text_width1 // 2
    text_y1 = how_many_players.centery - text_height1 // 2
    text_x2 = two.centerx - text_width2 // 2
    text_y2 = two.centery - text_height2 // 2
    text_x3 = three.centerx - text_width3 // 2
    text_y3 = three.centery - text_height3 // 2
    text_x4 = four.centerx - text_width4 // 2
    text_y4 = four.centery - text_height4 // 2
    text_x5 = five.centerx - text_width5 // 2
    text_y5 = five.centery - text_height5 // 2
    text_x6 = six.centerx - text_width6 // 2
    text_y6 = six.centery - text_height6 // 2
    WIN.blit(text_surface1, (text_x1, text_y1))
    WIN.blit(text_surface2, (text_x2, text_y2))
    WIN.blit(text_surface3, (text_x3, text_y3))
    WIN.blit(text_surface4, (text_x4, text_y4))
    WIN.blit(text_surface5, (text_x5, text_y5))
    WIN.blit(text_surface6, (text_x6, text_y6))


def add_click():
    pass


def draw_window():
    pygame.init()
    WIN.fill((255, 200, 250))

    match step:
        case 0:
            how_many_players()
        case 1:
            how_many_computer_players()
            
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                two = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2, 40, 50)
                three = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 40, 50)
                four = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2, 40, 50)
                five = pygame.Rect(WIDTH // 2, HEIGHT // 2, 40, 50)
                six = pygame.Rect(WIDTH // 2 + 50, HEIGHT // 2, 40, 50)
                if two.collidepoint(event.pos):
                    how_many_computer_players()
                    pygame.display.update()
                elif three.collidepoint(event.pos):
                    print("Clicked '3'")
                elif four.collidepoint(event.pos):
                    print("Clicked '4'")
                elif five.collidepoint(event.pos):
                    print("Clicked '5'")
                elif six.collidepoint(event.pos):
                    print("Clicked '6'")
        step += 1
        draw_window()
    pygame.quit()

    # def draw_board(self, win) -> None:
    #     win.fill((205, 133, 63))
    #     for row in range(ROWS):
    #         slot = 0
    #         for column in range(COLS):
    #             if ((COLS - 2 * BOARD_SLOTS[row]) / 2) + (slot * 2) == column:
    #                 if self.__grid[row][column].piece is None:
    #                     pygame.draw.circle(win, LIGHT_BROWN, (
    #                     (column + 1) * SQUARE_SIZE,
    #                     (row + 1) * SQUARE_SIZE + 70), SQUARE_SIZE // 2)
    #                 else:
    #                     color = COLORS_RGB[
    #                         self.__grid[row][column].piece.color]
    #                     pygame.draw.circle(win, color, (
    #                     (column + 1) * SQUARE_SIZE,
    #                     (row + 1) * SQUARE_SIZE + 70), SQUARE_SIZE // 2)
    #                 if slot < BOARD_SLOTS[row] - 1:
    #                     slot += 1

    # def countinue_game(self) -> None:
    #     """
    #     checks if the player wants to continue with the same players.
    #     and if the player wants to continue with the same players
    #     the function will continue the game with the same players.
    #     """
    #     same_players = input("would you like to use the same players? (y/n):")
    #     while same_players.lower() not in ["y", "n"]:
    #         same_players = input("please enter y or n: ")
    #     if same_players == "n":
    #         self.set_game()
    #     else:
    #         for player in self.board.players:
    #             self.board.add_player(player)
    #         self.delete_file_text("log_game.txt")
    #         self.add_move_to_log("new_game")

if __name__ == "__main__":
    main()
