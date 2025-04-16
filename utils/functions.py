from random import sample, randint
from collections import defaultdict

def generate_grid(rows: int, cols: int):
    grid = [[0] * cols for _ in range(rows)]

    for row in range(rows):
        walls_indexes = sample(range(0, cols), randint(1, cols//2))
        for wall_index in walls_indexes:
            grid[row][wall_index] = 1
    
    grid[0][0] = 0
    grid[rows-1][cols-1] = 0
    return grid


def print_grid(grid):
    for i in range(len(grid)):
        print(grid[i])


def valid_bounds(row, col, w, h):
    return 0 <= row < h and 0 <= col < w


def get_adjacency_list(grid):
    height = len(grid)
    width = len(grid[0])
    adj_cells = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    adj_list = defaultdict(list)

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 1:
                adj_list[(row, col)] = []

                for adj_r, adj_c in adj_cells:
                    curr_r = adj_r + row
                    curr_c = adj_c + col
                    if (valid_bounds(curr_r, curr_c, width, height) and grid[curr_r][curr_c] == 0):
                        adj_list[(row, col)].append((curr_r, curr_c))
    
    return adj_list
    

def DFS(graph: dict, node: tuple[(int, int)], target: tuple[(int, int)], visited: set=set()):
    stack = [(node, [node])]

    while(stack):
        vertex, path = stack.pop()
        if vertex not in visited:
            if vertex == target:
                return path
            
            visited.add(vertex)
            for n in graph[vertex]:
                stack.append((n, path+[n]))
    
    return None

    