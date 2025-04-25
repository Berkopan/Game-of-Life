import pygame
import numpy as np
import sys

WIDTH, HEIGHT = 800, 800
CELL_SIZE = 10

ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRID_COLOR = (40, 40, 40)

grid = np.zeros((ROWS, COLS), dtype=int)

def count_neighbors(grid, x, y):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                total += grid[nx][ny]
    return total

def next_generation(grid):
    new_grid = np.zeros((ROWS, COLS), dtype=int)
    for i in range(ROWS):
        for j in range(COLS):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

def draw_grid(screen, grid):
    screen.fill(BLACK)
    for i in range(ROWS):
        for j in range(COLS):
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[i][j] == 1:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()

    global grid
    running = False

    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                i = mouse_y // CELL_SIZE
                j = mouse_x // CELL_SIZE
                grid[i][j] = 1 - grid[i][j]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running

        if running:
            grid = next_generation(grid)

        draw_grid(screen, grid)
        pygame.display.flip()

if __name__ == "__main__":
    main()