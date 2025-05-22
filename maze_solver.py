# Group Members: Efehan Aras, Ataberk Akçin, Babak Gasimzade
# Maze Solver Project - Dijkstra’s Algorithm
# This algorithm finds the shortest path with the minimum coin total from S to G using uniform-cost search.
# Referenced structure and explanation from https://brilliant.org/wiki/dijkstras-short-path-finder/

import heapq  # We use heapq to implement a priority queue (min-heap)

# These are the 8 possible movement directions including diagonals
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

def read_maze(filename):
    # Reads the maze from a text file and stores it as a list of lists.
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def find_position(maze, char):
    # Finds the coordinates of a specific character (e.g., 'S' or 'G') in the maze.
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == char:
                return i, j
    return None  # If not found, return None

def is_valid(maze, x, y):
    # Checks if a position is inside the maze boundaries and is not a wall ('X').
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] != 'X'

def get_coin_value(cell):
    # Returns the numeric coin value of a cell. Non-digit cells like 'S' or 'G' count as 0.
    return int(cell) if cell.isdigit() else 0

def dijkstra(maze):
    # Dijkstra’s algorithm implementation to find the shortest path from S to G with minimum coin cost.
    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')

    visited = set()  # Keeps track of visited positions to avoid revisiting
    heap = [(0, 0, start, [])]  # Priority queue: (steps taken, total coins, current position, path taken)

    while heap:
        steps, coins, (x, y), path = heapq.heappop(heap)  # Take the node with the lowest steps

        if (x, y) in visited:
            continue  # Skip this node if already processed
        visited.add((x, y))  # Mark the current node as visited

        path = path + [(x, y)]  # Add the current position to the path

        if (x, y) == goal:
            return coins, path  # Return total coins and path when goal is reached

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy  # Calculate next position

            if is_valid(maze, nx, ny) and (nx, ny) not in visited:
                coin = get_coin_value(maze[nx][ny])  # Get coin value at the new cell
                heapq.heappush(heap, (steps + 1, coins + coin, (nx, ny), path))  # Push new state to the queue

    return float('inf'), []  # Return infinity if no valid path is found

def display_path(maze, path):
    # (Optional) Visualizes the path in the maze by marking visited cells with '*'.
    result = [row.copy() for row in maze]
    for (x, y) in path:
        if result[x][y] not in ('S', 'G'):
            result[x][y] = '*'
    for row in result:
        print(''.join(result))

# If we run this file directly, it will test Dijkstra on maze1.txt
if __name__ == "__main__":
    maze_file = "maze1.txt"  # You can change this to maze2.txt or maze3.txt
    maze = read_maze(maze_file)
    coin_sum, path = dijkstra(maze)

    print("Dijkstra Solution - Minimum coins:", coin_sum)
    print("Path length:", len(path) - 1)  # Subtract 1 to exclude the start cell
    # Uncomment the line below to visualize the path inside the maze
    # display_path(maze, path)
