# Group Members: Efehan Aras, Ataberk Akçin, Babak Gasimzade
# Maze Solver Project - A* Algorithm
# This algorithm uses both the coin cost and a heuristic (goal distance) to find the optimal path from S to G.
# External help: Heuristic integration adapted from https://www.datacamp.com/tutorial/a-star-algorithm

import heapq  # We use heapq to implement the priority queue (min-heap)

# These are the 8 possible movement directions including diagonals
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

def read_maze(filename):
    # Reads the maze from a text file and stores it as a list of lists.
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def find_position(maze, char):
    # Finds and returns the coordinates (row, col) of a given character (S or G) in the maze.
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == char:
                return i, j
    return None  # If not found, return None

def is_valid(maze, x, y):
    # Checks if a given coordinate is inside the maze and not a wall ('X').
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] != 'X'

def get_coin_value(cell):
    # Returns the numeric coin value of a cell. Non-digit cells like 'S' or 'G' count as 0.
    return int(cell) if cell.isdigit() else 0

def chebyshev_dist(x1, y1, x2, y2):
    # Returns the Chebyshev distance between two points. This heuristic works with diagonal movement.
    return max(abs(x1 - x2), abs(y1 - y2))

def a_star(maze):
    # A* algorithm to find the shortest path from S to G with the lowest coin cost using a heuristic.
    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')

    heap = [(0, 0, start, [])]  # Priority queue: (f = g + h, total coins, current position, path so far)
    visited = {}  # Tracks visited positions and their minimum coin cost

    while heap:
        f, coins, (x, y), path = heapq.heappop(heap)  # Pop the cell with the lowest total estimated cost

        if (x, y) in visited and visited[(x, y)] <= coins:
            continue  # Skip if this position was already visited with fewer coins
        visited[(x, y)] = coins  # Mark current position with coin cost

        path = path + [(x, y)]  # Extend the current path

        if (x, y) == goal:
            return coins, path  # Return total coins and path when goal is reached

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy  # Calculate next position

            if is_valid(maze, nx, ny):
                g = coins + get_coin_value(maze[nx][ny])  # Cost from start to new cell
                h = chebyshev_dist(nx, ny, goal[0], goal[1])  # Estimated cost from new cell to goal
                heapq.heappush(heap, (g + h, g, (nx, ny), path))  # Push new state into the queue

    return float('inf'), []  # Return infinity if no valid path is found

def display_path(maze, path):
    # (Optional) Visualizes the maze by marking the solution path with '*'.
    result = [row.copy() for row in maze]
    for (x, y) in path:
        if result[x][y] not in ('S', 'G'):
            result[x][y] = '*'
    for row in result:
        print(''.join(row))

# If we run this file directly, it will test A* search on maze1.txt
if __name__ == "__main__":
    maze_file = "maze1.txt"  # You can change this to "maze2.txt" or "maze3.txt"
    maze = read_maze(maze_file)
    coin_sum, path = a_star(maze)

    print("A* Solution - Minimum coins:", coin_sum)
    print("Path length:", len(path) - 1)  # Subtract 1 to exclude the start cell
    # Uncomment the line below to visualize the maze with the path
    # display_path(maze, path)
