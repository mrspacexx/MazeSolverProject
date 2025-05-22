# Group Members: Efehan Aras, Ataberk Akçin, Babak Gasimzade
# Maze Solver Project - Greedy Best-First Search
# It is fast but does not guarantee finding the path with the fewest coins.
# Referenced structure and explanation from https://www.geeksforgeeks.org/greedy-best-first-search-algorithm/

import heapq  # We use heapq for implementing the priority queue

# These are the 8 possible movement directions including diagonals
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

def read_maze(filename):
    #Reads a maze from a text file. Each line is turned into a list of characters. The maze is stored as a 2D list of strings.
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def find_position(maze, char):
    #Finds and returns the coordinates (row, col) of a given character (S or G) in the maze.
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == char:
                return i, j
    return None  # If not found, return None

def is_valid(maze, x, y):
    #Checks if a given coordinate is inside the maze and not a wall ('X').
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] != 'X'

def get_coin_value(cell):
    # Returns the coin value of a cell.

    return int(cell) if cell.isdigit() else 0

def chebyshev_dist(x1, y1, x2, y2):
    # Returns the Chebyshev distance between two points. This heuristic is used because diagonal movement is allowed.

    return max(abs(x1 - x2), abs(y1 - y2))

def greedy_best_first(maze):
    #Greedy Best-First Search algorithm implementation. Uses only the heuristic distance to the goal as priority — not coin cost.
    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')

    # Initialize the priority queue (min-heap).
    # Each item is a tuple: (heuristic distance, total coins collected, (x, y), path so far)
    heap = []
    heapq.heappush(heap, (chebyshev_dist(*start, *goal), 0, start, [start]))

    visited = set()  # Keeps track of visited cells to avoid loops

    while heap:
        # Pop the cell with the smallest heuristic distance
        _, coins, (x, y), path = heapq.heappop(heap)

        if (x, y) in visited:
            continue  # Skip already visited cells
        visited.add((x, y))

        # If we reach the goal, return total coins and the path
        if (x, y) == goal:
            return coins, path

        # Check all 8 possible directions
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if is_valid(maze, nx, ny) and (nx, ny) not in visited:
                # Calculate coin cost for the next cell
                new_coins = coins + get_coin_value(maze[nx][ny])
                # Priority is based on how close this new cell is to the goal
                priority = chebyshev_dist(nx, ny, goal[0], goal[1])
                # Push new state to the heap with updated path
                heapq.heappush(heap, (priority, new_coins, (nx, ny), path + [(nx, ny)]))

    # If we exhaust all options without reaching the goal, return infinity
    return float('inf'), []

# If we run this file directly, it will test greedy search on maze1.txt
if __name__ == "__main__":
    maze_file = "maze1.txt"  # We can change to "maze2.txt" or "maze3.txt"
    maze = read_maze(maze_file)
    coin_sum, path = greedy_best_first(maze)

    print("Greedy Solution - Minimum coins:", coin_sum)
    print("Path length:", len(path) - 1)
