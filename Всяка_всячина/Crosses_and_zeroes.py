import pygame
import sys

# Ініціалізуємо Pygame
pygame.init()

# Filed
window_size = 300
grid_size = 100
line_width = 5

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
line_color = (0, 0, 0)

# Шрифти для тексту
font = pygame.font.Font(None, 80)  # Шрифт розміром 80

# Screen
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Хрестики нолики')

# Clock для контролю FPS
clock = pygame.time.Clock()

# game board
game_board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

def draw_lines():
    """Малюємо лінії сітки."""
    for i in range(1, 3):
        pygame.draw.line(
            screen, line_color,
            (i * grid_size, 0), (i * grid_size, window_size),
            line_width
        )
        pygame.draw.line(
            screen, line_color,
            (0, i * grid_size), (window_size, i * grid_size),
            line_width
        )

def draw_symbols():
    """Малюємо хрестики і нолики на дошці."""
    for row in range(3):
        for col in range(3):
            if game_board[row][col] != " ":
                symbol = font.render(game_board[row][col], True, black)
                symbol_rect = symbol.get_rect(
                    center = (col * grid_size + grid_size // 2,
                              row * grid_size + grid_size // 2)
                )
                screen.blit(symbol, symbol_rect)

# Run game
running = True
game_over = False

while running:
    screen.fill(white)  # Заповнюємо екран білим кольором
    draw_lines()  # Малюємо лінії сітки
    draw_symbols()  # Малюємо хрестики і нолики

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // grid_size, x // grid_size

            if game_board[row][col] == " ":
                game_board[row][col] = current_player

                if check_win(game_board, current_player):
                    print(f"Player {current_player} wins!")
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"

    pygame.display.flip()  # Оновлюємо екран
    clock.tick(60)  # Обмежуємо FPS до 60

pygame.quit()
