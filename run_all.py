# Group Members: Efehan Aras, Ataberk Akçin, Babak Gasimzade
# This script runs 3 different maze-solving algorithms (Dijkstra, A*, Greedy Best-First)
# on each of the 3 mazes and records the coin costs in results.txt.

from maze_solver import dijkstra
from astar_solver import a_star
from greedy_solver import greedy_best_first
from maze_solver import read_maze  # Reuses the read_maze function from the solver module

# List of input maze files to process
maze_files = ["maze1.txt", "maze2.txt", "maze3.txt"]

def run_all_algorithms():
    # Runs Dijkstra, A*, and Greedy for each maze and collects the results
    results = []

    for maze_file in maze_files:
        maze = read_maze(maze_file)  # Read maze from file

        # Solve using each algorithm
        coins_dijkstra, _ = dijkstra(maze)
        coins_astar, _ = a_star(maze)
        coins_greedy, _ = greedy_best_first(maze)

        # Determine the best result (minimum coins among all)
        best = min(coins_dijkstra, coins_astar, coins_greedy)

        # Append results for this maze to the list
        results.append((maze_file, coins_dijkstra, coins_astar, coins_greedy, best))

    return results

# Main execution: run algorithms and write output to results.txt
if __name__ == "__main__":
    output = run_all_algorithms()

    with open("results.txt", "w") as f:
        f.write("Maze, Dijkstra, A*, Greedy, Best\n")

        # Write individual results for each maze
        for maze, d, a, g, best in output:
            line = f"{maze}, {d}, {a}, {g}, {best}\n"
            print(line.strip())  # Also print result to console
            f.write(line)

        # Write complexity information at the end
        f.write("\nTime and Space Complexity:\n\n")

        f.write("Dijkstra:\n")
        f.write("  - Time: O(V + E log V)\n")
        f.write("  - Space: O(V)\n\n")

        f.write("A* Search:\n")
        f.write("  - Time: O(V log V) (depends on heuristic accuracy)\n")
        f.write("  - Space: O(V)\n\n")

        f.write("Greedy Best-First Search:\n")
        f.write("  - Time: O(V log V)\n")
        f.write("  - Space: O(V)\n")
        f.write("  - Note: Does not guarantee optimal solution (coin total may be higher).\n\n")

        f.write("V = Total number of accessible (non-wall) cells in the maze.\n")
        f.write("E = Total number of possible valid movements between cells. Each cell can have up to 8 connections (including diagonal directions).\n")

    print("\n✅ Results saved to results.txt")
