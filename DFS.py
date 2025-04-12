import functions as f
import sys
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
GRID_ROWS = 20
GRID_COLS = 20
grid_node_width = grid_node_height = 40  # cell dimensions 

# grid = f.generate_grid(GRID_ROWS, GRID_COLS)
# f.print_grid(grid)


class Cell(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None, w=None, h=None, color=None, value=None):
        super().__init__()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, w, h)
        self.surf = pygame.Surface((w, h))
        self.surf.fill((255, 255,255))
        self.value = value
        self.originalColor = color
        self.color = color
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 8 if self.color != GREEN else 0)
    
    def updateColor(self, surface, color):
        self.color = color
        pygame.draw.rect(surface, self.color, self.rect, 8 if self.color != GREEN else 0)
    
    def resetColor(self, surface):
        self.color = self.originalColor
        pygame.draw.rect(surface, self.color, self.rect, 8 if self.color != GREEN else 0)



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
            # if (r, c) in path:
            #     createSquare(x, y, GREEN, (r, c), cells)
            if grid[r][c] == 0:
                cells[(r, c)] = (createSquare(x, y, GRAY, (r, c)))
            else:
                cells[(r, c)] = createSquare(x, y, WHITE, (r, c))


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

    grid = f.generate_grid(GRID_ROWS, GRID_COLS)
    textplace = grid_node_width*GRID_COLS + 50

    start = (0, 0)
    target = (GRID_ROWS-1, GRID_COLS-1)

    graph = f.get_adjacency_list(grid)
    # path = f.DFS(graph=graph, node=start, target=target)
    # pathset = set(path) if path is not None else set()
    visited = set()
    stop = False
    cells = drawGrid(grid)
    
    calc_time = True
    stack = [((0, 0), [(0, 0)])]
    SCREEN.blit(FONT.render("DFS", False, WHITE), (textplace, 50))
    s = pygame.time.get_ticks()
    while True:
        CLOCK.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if stack and not stop:
            vertex, path = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                cells[vertex].updateColor(SCREEN, GREEN)

                if vertex == target:
                    stop = True
                    

                else:
                    for n in graph[vertex]:
                        stack.append((n, path+[n]))

        else:
            if target not in path:
                SCREEN.blit(FONT.render('No paths found.', False, WHITE), (textplace, 100))
            else:
                SCREEN.blit(FONT.render('Path found!', False, WHITE), (textplace, 100))
                
            # if stop and calc_time:
            #     calc_time = False
            #     end_time = pygame.time.get_ticks() - s
            #     SCREEN.blit(FONT.render(f'{end_time/1000:.2f}s', False, WHITE), (textplace, 150))

        pygame.display.update()


main()


