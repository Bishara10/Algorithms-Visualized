import sys
import pygame
from collections import deque
from components import *
from functions import *

WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 800
GRID_ROWS = 20
GRID_COLS = 20
VIS_SPEED = 100
grid_node_width = grid_node_height = 40  # cell dimensions 

# grid = generate_grid(GRID_ROWS, GRID_COLS)
# print_grid(grid)


def createSquare(x, y, color, value):
    global SCREEN
    cell = Cell(x, y, grid_node_width, grid_node_height, color, value)
    cell.draw(SCREEN)

    return cell


def drawGrid(grid) -> dict:
    global SCREEN
    cells = {} # Group to store cells

    y = 0  # start at the top of the screen
    for r in range(GRID_ROWS):
        x = 0 # for every row, start at the left of the screen
        for c in range(GRID_COLS):
            if grid[r][c] == 0:
                cells[(r, c)] = (createSquare(x, y, WHITE, (r, c)))

            x += grid_node_width # for ever item/number in that row we move one "step" to the right
        y += grid_node_height   # for every new row we move one "step" downwards

    pygame.display.update()

    return cells


def drawPath(cells: dict[tuple, Cell], path):
    global SCREEN
    for p in path:
        cells[p].updateColor(SCREEN, GREEN)

def resetColors(cells: dict[tuple, Cell]):
    global SCREEN
    for cell in cells.values():
        cell.resetColor(SCREEN)

def main():
    global SCREEN, CLOCK
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Algorithms Visaulized")
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(BLACK)
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.SysFont('Arial', 50)

    grid = generate_grid(GRID_ROWS, GRID_COLS)
    textplace = grid_node_width*GRID_COLS + 50

    start = (0, 0)
    target = (GRID_ROWS-1, GRID_COLS-1)

    graph = get_adjacency_list(grid)
    # path = DFS(graph=graph, node=start, target=target)
    # pathset = set(path) if path is not None else set()
    visited = set()
    stop = False
    cells = drawGrid(grid)
    calc_time = True

    queue = deque([(start, [start])])
    SCREEN.blit(FONT.render("BFS", False, WHITE), (textplace, 50))
    s = pygame.time.get_ticks()
    while True:
        CLOCK.tick(VIS_SPEED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if queue and not stop:
            vertex, path = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                cells[vertex].updateColor(SCREEN, GREEN)

                if vertex == target:
                    stop = True
                    SCREEN.fill(BLACK)
                    drawGrid(grid)
                    resetColors(cells)
                    drawPath(cells, path)
                    SCREEN.blit(FONT.render("BFS", False, WHITE), (textplace, 50))

            
                else:
                    for n in graph[vertex]:
                        queue.append((n, path+[n]))

        else:
            if target not in path:
                SCREEN.blit(FONT.render('No paths found.', False, WHITE), (textplace, 100))
            else:
                SCREEN.blit(FONT.render('Shortest path found!', False, WHITE), (textplace, 100))

            # if stop and calc_time:
            #     calc_time = False
            #     end_time = pygame.time.get_ticks() - s
            #     SCREEN.blit(FONT.render(f'{end_time/1000:.2f}s', False, WHITE), (textplace, 150))

        pygame.display.update()


main()


